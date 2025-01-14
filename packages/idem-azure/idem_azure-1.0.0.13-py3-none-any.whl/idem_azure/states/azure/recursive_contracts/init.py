import uuid

RESOURCES_WITH_PRESENT_WRAPPER = [
    "azure.sql_database.databases",
]

LIST_RESOURCES_WITH_ABSENT_WRAPPER = [
    "azure.sql_database.databases",
]


async def call_present(hub, ctx):
    r"""Wrapper for present function."""

    name = ctx.kwargs.get("name", None)
    state_ctx = ctx.kwargs.get("ctx") or ctx.args[1]
    assert state_ctx, f"state context is missing: {state_ctx}"

    azure_service_resource_type = state_ctx.get("tag").split("_|")[0]

    # TODO: This needs to be removed once all resources follow the contract
    if azure_service_resource_type not in RESOURCES_WITH_PRESENT_WRAPPER:
        return await ctx.func(*ctx.args, **ctx.kwargs)

    result = {
        "result": True,
        "old_state": None,
        "new_state": None,
        "name": name,
        "comment": [],
    }

    ctx.kwargs[
        "subscription_id"
    ] = hub.tool.azure.resource_utils.get_subscription_id_from_account(
        state_ctx, ctx.kwargs.get("subscription_id")
    )

    service_resource_type = azure_service_resource_type.replace("azure.", "")

    hub_ref_exec = hub.exec.azure
    for resource_path_segment in service_resource_type.split("."):
        hub_ref_exec = hub_ref_exec[resource_path_segment]

    resource_id = ctx.kwargs.get("resource_id") or (
        state_ctx.get("rerun_data") or {}
    ).get("resource_id")
    local_params = {**ctx.kwargs}

    get_resource_only_with_resource_id = hub.OPT.idem.get(
        "get_resource_only_with_resource_id", False
    )

    if state_ctx.get("rerun_data"):
        handle_operation_ret = await hub.tool.azure.operation_utils.handle_operation(
            state_ctx,
            state_ctx.get("rerun_data"),
            service_resource_type,
        )

        if not handle_operation_ret["result"]:
            result["comment"] += handle_operation_ret["comment"]
            if handle_operation_ret.get("rerun_data"):
                result["rerun_data"] = handle_operation_ret["rerun_data"]
                if handle_operation_ret["rerun_data"].get("has_error", False):
                    result["result"] = False
            else:
                result["result"] = False

            return result

        resource_id = handle_operation_ret["resource_id"]

    if resource_id:
        response_get = await hub_ref_exec.get(state_ctx, resource_id=resource_id)

        if not response_get["result"] or (
            not response_get["ret"] and get_resource_only_with_resource_id
        ):
            result["result"] = False
            result["comment"] += response_get["comment"]
            return result

        # long-running operation has succeeded - both update and create
        if state_ctx.get("rerun_data"):
            result["new_state"] = response_get["ret"]
            result["old_state"] = state_ctx.get("rerun_data").get("old_state")

            if result["old_state"]:
                result["comment"].append(
                    hub.tool.azure.comment_utils.update_comment(
                        azure_service_resource_type, name
                    )
                )
            else:
                result["comment"].append(
                    hub.tool.azure.comment_utils.create_comment(
                        azure_service_resource_type, name
                    )
                )

            return result

        result["old_state"] = response_get["ret"]
    elif not get_resource_only_with_resource_id:
        resource_id = hub.tool.azure.resource_utils.construct_resource_id(
            service_resource_type, local_params
        )

        if not resource_id:
            result["result"] = False
            result["comment"].append(
                f"Could not construct resource ID of {azure_service_resource_type} from input arguments."
            )
            return result

        response_get = await hub_ref_exec.get(state_ctx, resource_id=resource_id)

        if not response_get["result"]:
            result["result"] = False
            result["comment"] += response_get["comment"]
            return result

        if response_get["ret"]:
            result["old_state"] = response_get["ret"]

    state_ctx["wrapper_result"] = result
    state_ctx["computed"] = {
        "resource_url": hub.tool.azure.resource_utils.construct_resource_url(
            state_ctx, service_resource_type, local_params
        ),
    }
    return await ctx.func(*ctx.args, **{**ctx.kwargs, "resource_id": resource_id})


async def call_absent(hub, ctx):
    r"""Wrapper for absent function.

    This method handles the parameters given in the ctx and deletes a resource only if
    the parameters are valid and the resource can be found using them.

    As with the call_present method, here in call_absent we also rely on having rerun_data in order to decide
    whether delete API call needs to be done or we just have to reconcile and wait until for the delete
    operation to complete.

    Steps:
        1. Construct resource_id if it is missing and get_resource_only_with_resource_id flag is NOT set.
            If resource_id is NOT provided and cannot be constructed, then it is directly assumed that the
            resource does not exist in the Cloud. We then return result["result"]=True and result["comment"]
            that the resource is already absent.
        2. Using resource_id check for resource existence by getting the resource current state from the Cloud.
            If the resource is found then delete it or return already absent comment.

    Args:
        hub:
            The redistributed pop central hub. The root of the namespace that pop operates on.
        ctx:
            Invocation context for this command.


    Returns: The result of a resource deletion state.

    """

    state_ctx = ctx.kwargs.get("ctx") or ctx.args[1]
    assert state_ctx, f"state context is missing: {state_ctx}"

    azure_service_resource_type = state_ctx.get("tag").split("_|")[0]
    service_resource_type = azure_service_resource_type.replace("azure.", "")

    if azure_service_resource_type not in LIST_RESOURCES_WITH_ABSENT_WRAPPER:
        return await ctx.func(*ctx.args, **ctx.kwargs)

    name = ctx.kwargs.get("name", None)

    result = {
        "comment": [],
        "old_state": state_ctx.get("old_state"),
        "new_state": None,
        "name": name,
        "result": True,
    }

    ctx.kwargs[
        "subscription_id"
    ] = hub.tool.azure.resource_utils.get_subscription_id_from_account(
        state_ctx, ctx.kwargs.get("subscription_id")
    )

    hub_ref_exec = hub.exec.azure
    for resource_path_segment in service_resource_type.split("."):
        hub_ref_exec = hub_ref_exec[resource_path_segment]

    get_resource_only_with_resource_id = hub.OPT.idem.get(
        "get_resource_only_with_resource_id", False
    )

    resource_id = ctx.kwargs.get("resource_id")
    local_params = {**ctx.kwargs}

    if not resource_id and not get_resource_only_with_resource_id:
        resource_id = (state_ctx.get("old_state") or {}).get(
            "resource_id"
        ) or hub.tool.azure.resource_utils.construct_resource_id(
            service_resource_type, local_params
        )

    if not resource_id and not state_ctx.get("rerun_data"):
        result["comment"].append(
            hub.tool.azure.comment_utils.already_absent_comment(
                azure_service_resource_type, name
            )
        )
        return result

    if not state_ctx.get("rerun_data"):
        get_ret = await hub_ref_exec.get(state_ctx, resource_id=resource_id)

        if not get_ret["result"]:
            result["result"] = False
            result["comment"] += get_ret["comment"]
            return result

        if not get_ret["ret"]:
            result["result"] = True
            result["comment"].append(
                hub.tool.azure.comment_utils.already_absent_comment(
                    azure_service_resource_type, name
                )
            )
            return result

        result["old_state"] = get_ret["ret"]
    else:
        result["old_state"] = state_ctx["rerun_data"]["old_state"]

    if state_ctx.get("test"):
        result["comment"].append(
            hub.tool.azure.comment_utils.would_delete_comment(
                azure_service_resource_type, name
            )
        )
        return result

    if not state_ctx.get("rerun_data"):
        resource_url = hub.tool.azure.resource_utils.construct_resource_url(
            state_ctx, service_resource_type, local_params
        )
        # First iteration; invoke resource's delete()
        response_delete = await hub.exec.request.raw.delete(
            state_ctx,
            url=resource_url,
            success_codes=[200, 202, 204],
        )

        if not response_delete["result"]:
            hub.log.debug(
                f"{hub.tool.azure.comment_utils.could_not_delete_comment('azure.sql_database.databases', name)} {response_delete['comment']} {response_delete['ret']}"
            )
            result["result"] = False
            result["comment"] = [response_delete["comment"], response_delete["ret"]]
            return result

        if response_delete["status"] == 202:
            # Deleting the resource is in progress.
            result["rerun_data"] = {
                "operation_id": str(uuid.uuid4()),
                "operation_headers": dict(response_delete.get("headers")),
                "resource_url": resource_url,
                "old_state": result["old_state"],
            }
            return result
    else:
        # delete() has been called on some previous iteration
        handle_operation_ret = await hub.tool.azure.operation_utils.handle_operation(
            state_ctx, state_ctx.get("rerun_data"), service_resource_type
        )
        if not handle_operation_ret["result"]:
            result["comment"].append(handle_operation_ret["comment"])
            if handle_operation_ret.get("rerun_data"):
                result["rerun_data"] = handle_operation_ret["rerun_data"]
                if handle_operation_ret["rerun_data"].get("has_error", False):
                    result["result"] = False
            else:
                result["result"] = False

            return result

        result["comment"].append(
            hub.tool.azure.comment_utils.delete_comment(
                azure_service_resource_type, name
            )
        )

    return result
