from typing import Any
from typing import Dict


RESOURCE_ID_TEMPLATES = {
    "sql_database.databases": "/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}",
}

RESOURCE_URL_TEMPLATES = {
    "sql_database.databases": "{ctx.acct.endpoint_url}{resource_id}?api-version=2021-11-01",
}


def construct_resource_id(hub, resource_type: str, input_props: Dict[str, Any]) -> str:
    id_template = RESOURCE_ID_TEMPLATES.get(resource_type)
    if not id_template:
        raise ValueError(f"Could not construct resource_id for {resource_type}")

    return id_template.format(**input_props)


def construct_resource_url(
    hub, ctx, resource_type: str, input_props: Dict[str, Any]
) -> str:
    url_template = RESOURCE_URL_TEMPLATES.get(resource_type)
    if not url_template:
        raise ValueError(f"Could not construct resource_url for {resource_type}")

    resource_id = input_props.get(
        "resource_id"
    ) or hub.tool.azure.resource_utils.construct_resource_id(resource_type, input_props)
    subscription_id = input_props.get("subscription_id") or ctx.acct.subscription_id

    return url_template.format(
        **{
            "ctx": ctx,
            **input_props,
            "resource_id": resource_id,
            "subscription_id": subscription_id,
        }
    )


def get_subscription_id_from_account(
    hub, ctx: Dict, subscription_id: str = None
) -> str:
    """If subscription_id is explicitly passed by the user, this subscription_id will be returned.
    If subscription_id is empty, this method will return default subscription_id from Azure account
    :param hub: Hub
    :param ctx: Context for the execution of the Idem run located in `hub.idem.RUNS[ctx['run_name']]`.
    :param subscription_id: A string explicitly passed by the user.
    :return: The correct subscription_id
    """
    if not subscription_id:
        subscription_id = ctx.get("acct", {}).get("subscription_id")
    if not subscription_id:
        hub.log.warning("Could not find subscription_id in account")
    return subscription_id


def is_pending(hub, ret: dict, state: str = None, **pending_kwargs) -> bool:
    """
    This method enables state specific implementation of is_pending logic,
    based on resource specific attribute(s).
    Usage 'idem state <sls-file> --reconciler=basic', where the reconciler attribute
    can be missed.

    :param hub: The Hub into which the resolved callable will get placed.
    :param ret: The returned dictionary of the last run.
    :param state: The name of the state.
    :param pending_kwargs: (dict, Optional) May include 'ctx' and 'reruns_wo_change_count'.

    :return: True | False
    """
    if not ret:
        return False

    if ret.get("rerun_data") and ret["rerun_data"].get("has_error", False):
        return False

    if ret.get("rerun_data"):
        return True

    if ret["result"]:
        return False

    return (
        pending_kwargs
        and pending_kwargs.get("reruns_wo_change_count", 0)
        <= hub.reconcile.pending.default.MAX_RERUNS_WO_CHANGE
    )
