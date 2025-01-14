import copy
from typing import Any
from typing import Dict
from typing import List
from typing import Set


async def run_present(
    hub,
    ctx,
    resource_idem_path: str,
    api_version: str,
    name: str,
    resource_id: str,
    resource_id_format: str,
    path_properties: Dict,
    query_properties: Dict,
    body_properties: Dict,
) -> Dict[str, Any]:
    result = {
        "name": name,
        "result": True,
        "old_state": None,
        "new_state": None,
        "comment": [],
    }

    if not path_properties.get("subscription_id"):
        path_properties = copy.deepcopy(path_properties)
        path_properties["subscription_id"] = ctx.acct.subscription_id

    if resource_id is None:
        resource_id = resource_id_format.format(**path_properties)

    get_method = getattr(hub.exec, f"{resource_idem_path}.get")
    response_get = await get_method(ctx, resource_id=resource_id)

    if response_get["result"]:
        path_properties = {k: v for k, v in path_properties.items() if v is not None}
        query_properties = {k: v for k, v in query_properties.items() if v is not None}
        body_properties = {k: v for k, v in body_properties.items() if v is not None}

        if response_get["ret"] is None:
            if ctx.get("test", False):
                # Return a proposed state by Idem state --test
                result[
                    "new_state"
                ] = hub.tool.azure.test_state_utils.generate_test_state(
                    enforced_state={},
                    desired_state={
                        "name": name,
                        "resource_id": resource_id,
                        **path_properties,
                        **query_properties,
                        **body_properties,
                    },
                )

                result["comment"].append(
                    hub.tool.azure.comment_utils.would_create_comment(
                        resource_idem_path, name
                    )
                )
                return result
            else:
                # PUT operation to create a resource
                raw_body_payload = getattr(
                    hub.tool, f"{resource_idem_path}.convert_present_to_raw_state"
                )(body_properties)

                request_result = await hub.tool.azure.generic.run_put_request(
                    ctx,
                    resource_id,
                    path_properties,
                    query_properties,
                    api_version,
                    raw_body_payload,
                    resource_idem_path,
                    name,
                    "create",
                )
                result["result"] = request_result["result"]
                result["comment"] += request_result["comment"]
                result["new_state"] = request_result["new_state"]
                return result

        else:
            result["old_state"] = response_get["ret"]
            result["old_state"]["name"] = name
            present_update_payload = hub.tool.azure.generic.get_update_payload(
                response_get["ret"], body_properties, path_properties, query_properties
            )
            if present_update_payload:
                if ctx.get("test", False):
                    # Return a proposed state by Idem state --test
                    result[
                        "new_state"
                    ] = hub.tool.azure.test_state_utils.generate_test_state(
                        enforced_state={},
                        desired_state={
                            "name": name,
                            "resource_id": resource_id,
                            **path_properties,
                            **query_properties,
                            **body_properties,
                        },
                    )

                    result["comment"].append(
                        hub.tool.azure.comment_utils.would_update_comment(
                            resource_idem_path, name
                        )
                    )
                    return result

                # PUT operation to update a resource
                update_payload = getattr(
                    hub.tool, f"{resource_idem_path}.convert_present_to_raw_state"
                )(present_update_payload)
                request_result = await hub.tool.azure.generic.run_put_request(
                    ctx,
                    resource_id,
                    path_properties,
                    query_properties,
                    api_version,
                    update_payload,
                    resource_idem_path,
                    name,
                    "update",
                )
                result["result"] = request_result["result"]
                result["comment"] += request_result["comment"]
                result["new_state"] = request_result["new_state"]
            else:
                result["new_state"] = copy.deepcopy(result["old_state"])
                result["comment"].append(
                    hub.tool.azure.comment_utils.no_property_to_be_updated_comment(
                        resource_idem_path, name
                    )
                )
                return result

            return result

    else:
        hub.log.debug(
            f"{hub.tool.azure.comment_utils.could_not_get_comment(resource_idem_path, name)} {response_get['comment']} {response_get['ret']}"
        )
        result["result"] = False
        result["comment"] = [response_get["comment"], response_get["ret"]]
        return result


async def run_absent(
    hub,
    ctx,
    resource_idem_path: str,
    api_version: str,
    name: str,
    resource_id_format: str,
    resource_id: str,
    path_properties: Dict,
    query_properties: Dict,
) -> Dict[str, Any]:
    result = dict(name=name, result=True, comment=[], old_state=None, new_state=None)

    if not path_properties.get("subscription_id"):
        path_properties = copy.deepcopy(path_properties)
        path_properties["subscription_id"] = ctx.acct.subscription_id

    if resource_id is None:
        resource_id = resource_id_format.format(**path_properties)

    get_method = getattr(hub.exec, f"{resource_idem_path}.get")
    response_get = await get_method(ctx, resource_id=resource_id)
    if response_get["result"]:
        if response_get["ret"]:
            result["old_state"] = response_get["ret"]
            result["old_state"]["name"] = name
            if ctx.get("test", False):
                result["comment"].append(
                    hub.tool.azure.comment_utils.would_delete_comment(
                        resource_idem_path, name
                    )
                )
                return result
            query_properties_url = "&".join(
                [
                    f"{prop_name}={prop_val}"
                    for prop_name, prop_val in query_properties.items()
                ]
            )
            url = f"{ctx.acct.endpoint_url}{resource_id}?api-version={api_version}"
            if query_properties_url:
                url = f"{url}&{query_properties_url}"
            response_delete = await hub.exec.request.raw.delete(
                ctx,
                url=url,
                success_codes=[200, 202, 204],
            )

            if not response_delete["result"]:
                hub.log.debug(
                    f"{hub.tool.azure.comment_utils.could_not_delete_comment(resource_idem_path, name)} {response_delete['comment']} {response_delete['ret']}"
                )
                result["result"] = False
                result["comment"] = [response_delete["comment"], response_delete["ret"]]
                return result

            result["comment"].append(
                hub.tool.azure.comment_utils.delete_comment(resource_idem_path, name)
            )
            return result
        else:
            # If Azure returns 'Not Found' error, it means the resource has been absent.
            result["comment"].append(
                hub.tool.azure.comment_utils.already_absent_comment(
                    resource_idem_path, name
                )
            )
            return result
    else:
        hub.log.debug(
            f"{hub.tool.azure.comment_utils.could_not_get_comment(resource_idem_path, name)}' {response_get['comment']} {response_get['ret']}"
        )
        result["result"] = False
        result["comment"] = [response_get["comment"], response_get["ret"]]
    return result


async def run_put_request(
    hub,
    ctx,
    resource_id: str,
    path_properties: str,
    query_properties: Dict,
    api_version: str,
    raw_payload: Dict,
    resource_idem_path: str,
    name: str,
    mode: str,
) -> Dict[str, Any]:
    fail_comment = ""
    success_comment = ""
    if mode == "create":
        fail_comment = hub.tool.azure.comment_utils.could_not_create_comment(
            resource_idem_path, name
        )
        success_comment = hub.tool.azure.comment_utils.create_comment(
            resource_idem_path, name
        )
    elif mode == "update":
        fail_comment = hub.tool.azure.comment_utils.could_not_update_comment(
            resource_idem_path, name
        )
        success_comment = hub.tool.azure.comment_utils.update_comment(
            resource_idem_path, name
        )

    result = await _run_json_request(
        hub,
        ctx,
        resource_id=resource_id,
        request_method="put",
        api_version=api_version,
        resource_idem_path=resource_idem_path,
        success_codes=[200, 201, 202],
        success_comment=success_comment,
        fail_comment=fail_comment,
        query_params=query_properties,
        raw_payload=raw_payload,
    )

    if result["result"]:
        result["new_state"].update(path_properties)
        result["new_state"].update(query_properties)
        result["new_state"].update({"name": name, "resource_id": resource_id})

    return result


def compute_update_payload_for_key_subset(
    hub, old_values: Dict[str, Any], new_values: Dict[str, Any], key_subset: Set[str]
) -> Dict[str, Any]:
    old_values_generic = {k: v for (k, v) in old_values.items() if k in key_subset}
    new_values_generic = {k: v for (k, v) in new_values.items() if k in key_subset}
    update_payload = hub.tool.azure.generic.get_update_payload(
        old_values_generic, new_values_generic
    )
    return update_payload


def get_update_payload(
    hub,
    old_state: Dict,
    new_body_properties: Dict,
    path_properties: Dict = None,
    query_properties: Dict = None,
) -> Dict[str, Any]:
    # Exclude the path and query properties from the diff
    old_body_properties = copy.deepcopy(old_state)
    for prop_name in old_state:
        if (path_properties and prop_name in path_properties) or (
            query_properties and prop_name in query_properties
        ):
            old_body_properties.pop(prop_name, None)

    has_change = hub.tool.azure.compare.compare_exact_matches(
        old_state=old_body_properties,
        plan_state=new_body_properties,
    )

    if has_change:
        cleaned_up_new_body_props = hub.tool.azure.utils.cleanup_none_values(
            new_body_properties
        )
        changed_props_payload = copy.deepcopy(cleaned_up_new_body_props)
        for old_body_prop_name, old_body_prop_value in old_body_properties.items():
            if old_body_prop_name not in changed_props_payload:
                changed_props_payload[old_body_prop_name] = old_body_prop_value

        return changed_props_payload

    return {}


def convert_state_format(
    hub, state: Any, formatting_map: Any, list_items_indexes: Dict = None
) -> Any:
    """
    Converts a state from one format to another, e.g. present (snake case) to raw (camel case) format or vice versa.
    The conversion can change the property names and the structure of the resulting state, e.g. flatten
    deeply nested properties. Works with nested lists and dicts.

    Args:
        hub: The redistributed pop central hub.
        state: the current state of a resource.
        formatting_map: a mapping from one format to another. E.g.:
            "virtualNetworkPeerings": [
                {
                    "$list_refs": ["virtual_network_peerings"],
                    "name": "virtual_network_peerings.name",
                    "type": "virtual_network_peerings.type",
                    "properties": {
                        "allowVirtualNetworkAccess": "virtual_network_peerings.allow_virtual_network_access",
                        "allowForwardedTraffic": "virtual_network_peerings.allow_forwarded_traffic",
                        "allowGatewayTransit": "virtual_network_peerings.allow_gateway_transit",
                        "useRemoteGateways": "virtual_network_peerings.use_remote_gateways",
                        "remoteVirtualNetwork": "virtual_network_peerings.remote_virtual_network",
                        "remoteAddressSpace": {
                            "addressPrefixes": "virtual_network_peerings.remote_address_space.address_prefixes"
                        },
                        "remoteVirtualNetworkAddressSpace": {
                            "addressPrefixes": "virtual_network_peerings.remote_virtual_network_address_space.address_prefixes"
                        },
                        "remoteBgpCommunities": {
                            "virtualNetworkCommunity": "virtual_network_peerings.remote_bgp_communities.virtual_network_community"
                        },
                        "peeringState": "virtual_network_peerings.peering_state",
                        "peeringSyncLevel": "virtual_network_peerings.peering_sync_level",
                        "doNotVerifyRemoteGateways": "virtual_network_peerings.do_not_verify_remote_gateways",
                    },
                }
            ]
            $list_refs is a special reserved property in the mapping. Use it to specify which lists from the original
            state should be tracked at the current nesting level
        list_items_indexes: ignore, used internally by this recursive method.
            This property keeps track of the nested lists indexes

    Returns:
        The state in the new format
    """
    formatted_state = {}

    if isinstance(formatting_map, dict):
        for formatted_name, formatting_map_for_item in formatting_map.items():
            if formatted_name == "$list_refs":
                continue

            converted_value = hub.tool.azure.generic.convert_state_format(
                state, formatting_map_for_item, list_items_indexes
            )
            if (
                isinstance(formatting_map_for_item, str) and converted_value is not None
            ) or (
                isinstance(formatting_map_for_item, (dict, list)) and converted_value
            ):
                formatted_state[formatted_name] = converted_value
        return formatted_state
    elif isinstance(formatting_map, list):
        ref_lists_names = formatting_map[0]["$list_refs"]
        if not isinstance(ref_lists_names, list):
            ref_lists_names = [ref_lists_names]
        ref_lists = [
            _get_element_from_state(state, ref_list_name, list_items_indexes)
            for ref_list_name in ref_lists_names
        ]
        ref_lists = [el for el in ref_lists if el is not None]
        longest_ref_list = max(ref_lists, key=len) if ref_lists else []
        formatted_list = []
        for i, item in enumerate(longest_ref_list):
            if list_items_indexes is None:
                list_items_indexes = {}
            for ref_list_name in ref_lists_names:
                list_items_indexes[ref_list_name] = i
            formatted_list.append(
                hub.tool.azure.generic.convert_state_format(
                    state, formatting_map[0], list_items_indexes
                )
            )

        if list_items_indexes:
            for ref_list_name in ref_lists_names:
                list_items_indexes.pop(ref_list_name, None)

        return formatted_list
    elif isinstance(formatting_map, str):
        return _get_element_from_state(state, formatting_map, list_items_indexes)

    return formatted_state


def _get_element_from_state(
    state: Any, path: str, list_item_indexes: Dict = None
) -> Any:
    path_segments = path.split(".")
    partial_path = None
    element = state
    for path_segment in path_segments:
        if element.get(path_segment) is None:
            return None
        element = element[path_segment]
        partial_path = (
            f"{partial_path}.{path_segment}" if partial_path else path_segment
        )
        if list_item_indexes and partial_path in list_item_indexes:
            i = list_item_indexes[partial_path]
            if i < len(element):
                element = element[i]
            else:
                return None

    return element


async def _run_json_request(
    hub,
    ctx,
    resource_id: str,
    request_method: str,
    api_version: str,
    resource_idem_path: str,
    success_comment: str,
    fail_comment: str,
    success_codes: List,
    api_method: str = None,
    query_params: Dict = None,
    raw_payload: Dict = None,
):
    result = {"comment": [], "result": True, "new_state": None}

    if api_method:
        url = f"{ctx.acct.endpoint_url}{resource_id}/{api_method}?api-version={api_version}"
    else:
        url = f"{ctx.acct.endpoint_url}{resource_id}?api-version={api_version}"

    if query_params:
        query_params_url = "&".join(
            [f"{prop_name}={prop_val}" for prop_name, prop_val in query_params.items()]
        )
        if query_params_url:
            url = f"{url}&{query_params_url}"

    request_body = {
        "url": url,
        "success_codes": success_codes,
    }
    if raw_payload:
        request_body.update(
            **{
                "json": raw_payload,
            }
        )

    response = await getattr(hub.exec.request.json, request_method)(
        ctx,
        **request_body,
    )

    if response["status"] == 202:
        response = await hub.tool.azure.operation_utils.await_operation(
            ctx,
            operation_headers=response.get("headers"),
            resource_url=f"{ctx.acct.endpoint_url}{resource_id}?api-version={api_version}",
        )

    if not response["result"]:
        hub.log.debug(f"{fail_comment} {response['comment']} {response['ret']}")
        result["comment"] = [response["comment"], response["ret"]]
        result["result"] = False
        return result

    result["new_state"] = getattr(
        hub.tool, f"{resource_idem_path}.convert_raw_to_present_state"
    )(response["ret"])
    result["comment"].append(success_comment)
    return result


async def exec_request(
    hub,
    ctx,
    resource_id: str,
    request_method: str,
    api_method: str,
    api_version: str,
    resource_idem_path: str,
    query_params: Dict = None,
    raw_payload: Dict = None,
) -> Dict[str, Any]:
    success_comment = hub.tool.azure.comment_utils.executed_request_comment(
        resource_idem_path, resource_id, api_method
    )
    fail_comment = hub.tool.azure.comment_utils.could_not_execute_request_comment(
        resource_idem_path, resource_id, api_method
    )
    return await _run_json_request(
        hub,
        ctx,
        resource_id=resource_id,
        request_method=request_method,
        api_method=api_method,
        api_version=api_version,
        resource_idem_path=resource_idem_path,
        success_codes=[200],
        success_comment=success_comment,
        fail_comment=fail_comment,
        query_params=query_params,
        raw_payload=raw_payload,
    )
