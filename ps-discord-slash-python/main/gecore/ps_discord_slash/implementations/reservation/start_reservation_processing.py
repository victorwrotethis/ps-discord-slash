from gecore.ps_discord_slash.implementations.reservation.models.token_request_info import TokenRequestInfo
from gecore.ps_discord_slash.models.discord_config import JaegerEventRoles


def retrieve_required_info(command_body: {}) -> TokenRequestInfo:
    requester_id, approved_ids = retrieve_ids_if_rep(command_body)
    group_name = retrieve_group_name(command_body)
    return TokenRequestInfo(requester_id, approved_ids, group_name)


def retrieve_ids_if_rep(command_body: {}) -> (int, int):
    """filters reps and includes them if they not their own."""
    members = command_body['data']['resolved']['members']
    requester_id = command_body['member']['user']['id']
    approved_ids = []
    for user_id, user_info in members.items():
        if user_id is not requester_id:
            if has_rep_role(user_info['roles']):
                approved_ids.append(int(user_id))
    return int(requester_id), approved_ids


def has_rep_role(roles: []) -> bool:
    for role in roles:
        if int(role) is JaegerEventRoles.OVO_REP or JaegerEventRoles.COMMUNITY_REP:
            return True
    return False


def retrieve_group_name(command_body: {}) -> str:
    for entry in command_body['data']['options']:
        if entry['name'] == 'group':
            return entry['value']
