from gecore.ps_discord_slash.models.discord_config import JaegerEventRoles


def retrieve_ids_if_rep(command_body: {}):
    """filters reps and includes them if they not their own."""
    members = command_body['data']['resolved']['members']
    requester_id = command_body['member']['user']['id']
    approved_ids = []
    for user_id, user_info in members.items():
        if user_id is not requester_id:
            if has_rep_role(user_info['roles']):
                approved_ids.append(int(user_id))
    return approved_ids


def has_rep_role(roles: []) -> bool:
    for role in roles:
        if int(role) is JaegerEventRoles.OVO_REP or JaegerEventRoles.COMMUNITY_REP:
            return True
    return False
