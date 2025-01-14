"""
Autogenerated using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__


"""
from collections import OrderedDict
from typing import Any
from typing import Dict

__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    resource_group_name: str,
    public_ip_address_name: str,
    parameters: dict = None,
    force_update: bool = False,
):
    r"""
    **Autogenerated function**

    Create or update Public IP Addresses

    Args:
        name(str): The identifier for this state.
        resource_group_name(str): The name of the resource group.
        public_ip_address_name(str): The name of the public IP address.
        parameters(dict, optional): API request payload parameters. Defaults to {}.
        force_update(bool, optional): If PUT operation should be used instead of PATCH operation during resource update. Defaults to False.

    Returns:
        dict

    Examples:

        .. code-block:: sls

            resource_is_present:
              azure.virtual_networks.public_ip_addresses.present:
                - name: value
                - resource_group_name: value
                - public_ip_address_name: value
    """
    if parameters is None:
        parameters = {}

    subscription_id = ctx.acct.subscription_id
    response_get = await hub.exec.request.json.get(
        ctx,
        url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}?api-version=2021-03-01",
        success_codes=[200],
    )

    if force_update:
        if ctx.get("test", False):
            return dict(
                name=name,
                result=True,
                comment="Would force to update azure.virtual_networks.public_ip_addresses",
            )
        response_force_put = await hub.exec.request.json.put(
            ctx,
            url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}?api-version=2021-03-01",
            success_codes=[200, 201],
            json=parameters,
        )
        if response_force_put["result"]:
            old_resource = response_get["ret"] if response_get["result"] else None
            return dict(
                name=name,
                result=True,
                old_state=old_resource,
                new_state=response_force_put["ret"],
                comment=response_force_put["comment"],
            )
        else:
            hub.log.debug(
                f"Could not force to update Public IP Addresses {response_force_put['comment']} {response_force_put['ret']}"
            )
            return dict(
                name=name,
                result=False,
                comment=response_force_put["comment"],
                error=response_force_put["ret"],
            )

    if not response_get["result"]:
        if ctx.get("test", False):
            return dict(
                name=name,
                result=True,
                comment="Would create azure.virtual_networks.public_ip_addresses",
            )

        if response_get["status"] == 404:
            # PUT operation to create a resource
            response_put = await hub.exec.request.json.put(
                ctx,
                url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}?api-version=2021-03-01",
                success_codes=[200, 201],
                json=parameters,
            )

            if not response_put["result"]:
                hub.log.debug(
                    f"Could not create Public IP Addresses {response_put['comment']} {response_put['ret']}"
                )
                return dict(
                    name=name,
                    result=False,
                    comment=response_put["comment"],
                    error=response_put["ret"],
                )

            return dict(
                name=name,
                result=True,
                old_state=None,
                new_state=response_put["ret"],
                comment=response_put["comment"],
            )
        else:
            hub.log.debug(
                f"Could not get Public IP Addresses {response_get['comment']} {response_get['ret']}"
            )
            return dict(
                name=name,
                result=False,
                comment=response_get["comment"],
                error=response_get["ret"],
            )
    else:
        # PATCH operation to update a resource
        patch_parameters = {"tags": "tags"}
        existing_resource = response_get["ret"]
        new_parameters = hub.tool.azure.request.patch_json_content(
            patch_parameters, existing_resource, parameters
        )
        if ctx.get("test", False):
            return dict(
                name=name,
                result=True,
                comment=f"Would update azure.virtual_networks.public_ip_addresses with parameters: {new_parameters}",
            )

        if not new_parameters:
            return dict(
                name=name,
                result=True,
                old_state=existing_resource,
                new_state=existing_resource,
                comment=f"'{name}' has no property need to be updated.",
            )

        response_patch = await hub.exec.request.json.patch(
            ctx,
            url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}?api-version=2021-03-01",
            success_codes=[200],
            json=new_parameters,
        )

        if not response_patch["result"]:
            hub.log.debug(
                f"Could not update Public IP Addresses {response_patch['comment']} {response_patch['ret']}"
            )
            return dict(
                name=name,
                result=False,
                comment=response_patch["comment"],
                error=response_patch["ret"],
            )

        return dict(
            name=name,
            result=True,
            old_state=existing_resource,
            new_state=response_patch["ret"],
            comment=response_patch["comment"],
        )


async def absent(
    hub, ctx, name: str, resource_group_name: str, public_ip_address_name: str
) -> dict:
    r"""
    **Autogenerated function**

    Delete Public IP Addresses

    Args:
        name(str): The identifier for this state.
        resource_group_name(str): The name of the resource group.
        public_ip_address_name(str): The name of the public IP address.

    Returns:
        dict

    Examples:

        .. code-block:: sls

            resource_is_absent:
              azure.virtual_networks.public_ip_addresses.absent:
                - name: value
                - resource_group_name: value
                - public_ip_address_name: value
    """

    subscription_id = ctx.acct.subscription_id
    response_get = await hub.exec.request.json.get(
        ctx,
        url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}?api-version=2021-03-01",
        success_codes=[200],
    )
    if response_get["result"]:
        if ctx.get("test", False):
            return dict(
                name=name,
                result=True,
                comment="Would delete azure.virtual_networks.public_ip_addresses",
            )

        existing_resource = response_get["ret"]
        response_delete = await hub.exec.request.raw.delete(
            ctx,
            url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}?api-version=2021-03-01",
            success_codes=[200, 202, 204],
        )

        if not response_delete["result"]:
            hub.log.debug(
                f"Could not delete Public IP Addresses {response_delete['comment']} {response_delete['ret']}"
            )
            return dict(
                name=name,
                result=False,
                comment=response_delete["comment"],
                error=response_delete["ret"],
            )

        return dict(
            name=name,
            result=True,
            old_state=existing_resource,
            new_state={},
            comment=response_delete["comment"],
        )
    elif response_get["status"] == 404:
        # If Azure returns 'Not Found' error, it means the resource has been absent.
        return dict(
            name=name,
            result=True,
            old_state=None,
            new_state=None,
            comment=f"'{name}' already absent",
        )
    else:
        hub.log.debug(
            f"Could not get Public IP Addresses {response_get['comment']} {response_get['ret']}"
        )
        return dict(
            name=name,
            result=False,
            comment=response_get["comment"],
            error=response_get["ret"],
        )


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""
    **Autogenerated function**

    Describe the resource in a way that can be recreated/managed with the corresponding "present" function


    List all Public IP Addresses under the same subscription


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe azure_auto.virtual_networks.public_ip_addresses
    """

    result = {}
    subscription_id = ctx.acct.subscription_id
    uri_parameters = OrderedDict(
        {
            "resourceGroups": "resource_group_name",
            "publicIPAddresses": "public_ip_address_name",
        }
    )
    async for page_result in hub.tool.azure.request.paginate(
        ctx,
        url=f"{ctx.acct.endpoint_url}/subscriptions/{subscription_id}/providers/Microsoft.Network/publicIPAddresses?api-version=2021-03-01",
        success_codes=[200],
    ):
        resource_list = page_result.get("value", None)
        if resource_list:
            for resource in resource_list:
                uri_parameter_values = hub.tool.azure.uri.get_parameter_value(
                    resource["id"], uri_parameters
                )
                result[resource["id"]] = {
                    f"azure.virtual_networks.public_ip_addresses.present": uri_parameter_values
                    + [{"parameters": resource}]
                }
    return result
