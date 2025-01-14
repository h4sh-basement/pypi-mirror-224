import json
from typing import Dict

import spyctl.api as api
import spyctl.cli as cli
import spyctl.config.configs as cfg
import spyctl.resources.policies as p
import spyctl.resources.suppression_policies as sp
import spyctl.spyctl_lib as lib
import spyctl.commands.merge as m


def handle_apply(filename):
    resrc_data = lib.load_resource_file(filename)
    kind = resrc_data.get(lib.KIND_FIELD)
    if kind == lib.POL_KIND:
        type = resrc_data[lib.METADATA_FIELD][lib.METADATA_TYPE_FIELD]
        if type in lib.SUPPRESSION_POL_TYPES:
            handle_apply_suppression_policy(resrc_data)
        elif type in lib.GUARDIAN_POL_TYPES:
            handle_apply_policy(resrc_data)
        else:
            cli.err_exit(f"Unrecognized policy type '{type}'.")
    else:
        cli.err_exit(f"The 'apply' command is not supported for {kind}")


def handle_apply_policy(policy: Dict):
    ctx = cfg.get_current_context()
    policy = p.Policy(policy)
    uid, api_data = p.get_data_for_api_call(policy)
    if uid:
        resp = api.put_policy_update(*ctx.get_api_data(), uid, api_data)
        if resp.status_code == 200:
            cli.try_log(f"Successfully updated policy {uid}")
    else:
        resp = api.post_new_policy(*ctx.get_api_data(), api_data)
        if resp and resp.text:
            uid = json.loads(resp.text).get("uid", "")
            cli.try_log(f"Successfully applied new policy with uid: {uid}")


def handle_apply_suppression_policy(policy: Dict):
    ctx = cfg.get_current_context()
    matching_policies = check_suppression_policy_selector_hash(policy)
    if matching_policies:
        policy = handle_matching_policies(policy, matching_policies)
    else:
        policy = sp.TraceSuppressionPolicy(policy)
    uid, api_data = sp.get_data_for_api_call(policy)
    if uid:
        resp = api.put_policy_update(*ctx.get_api_data(), uid, api_data)
        if resp.status_code == 200:
            cli.try_log(f"Successfully updated suppression policy {uid}")
    else:
        resp = api.post_new_policy(*ctx.get_api_data(), api_data)
        if resp and resp.text:
            uid = json.loads(resp.text).get("uid", "")
            cli.try_log(
                f"Successfully applied new suppression policy with uid: {uid}"
            )


def handle_matching_policies(policy: Dict, matching_policies: Dict[str, Dict]):
    uid = policy[lib.METADATA_FIELD].get(lib.METADATA_UID_FIELD)
    if uid:
        return sp.TraceSuppressionPolicy(policy)
    query = (
        "There already exists a policy matching this scope. Would you like"
        " to merge this policy into the existing one?"
    )
    if not cli.query_yes_no(query):
        return sp.TraceSuppressionPolicy(policy)
    ret_pol = policy
    for uid, m_policy in matching_policies.items():
        merged = m.merge_resource(ret_pol, "", m_policy)
        if merged:
            ret_pol = merged
    ret_pol[lib.METADATA_FIELD][lib.METADATA_UID_FIELD] = uid
    return sp.TraceSuppressionPolicy(ret_pol)


def check_suppression_policy_selector_hash(policy: Dict) -> Dict[str, Dict]:
    ctx = cfg.get_current_context()
    selector_hash = policy[lib.METADATA_FIELD].get(
        lib.METADATA_S_CHECKSUM_FIELD
    )
    if not selector_hash:
        return {}
    type = policy[lib.METADATA_FIELD][lib.METADATA_TYPE_FIELD]
    params = {
        lib.METADATA_TYPE_FIELD: type,
        lib.API_HAS_TAGS_FIELD: [f"SELECTOR_HASH:{selector_hash}"],
    }
    resp_policies = api.get_policies(*ctx.get_api_data(), params)
    rv = {}
    for r_pol in resp_policies:
        uid = r_pol[lib.METADATA_FIELD][lib.METADATA_UID_FIELD]
        rv[uid] = r_pol
    return rv
