import json
import os

import jsonpickle
import requests

from gecore.ps_discord_slash.implementations.reservation.models.token_request_info import TokenRequestInfo
from gecore.ps_discord_slash.models.discord_config import JaegerEventRoles

token_api = os.getenv('token_api_url')


def process_reservation_start(command_body: {}) -> (str, bool):
    token_info = retrieve_required_info(command_body)
    return generate_link(token_info)


def retrieve_ovo_url() -> str:
    # Won't be cached right now as we are testing at the moment
    return os.getenv('ovo_web_url')


def generate_link(token_info: TokenRequestInfo) -> (str, bool):
    pickled_request = jsonpickle.encode(token_info, unpicklable=False)
    r = requests.post(token_api, json=pickled_request)
    if r.status_code == 200:
        token_result = r.json()
        print(token_result)
        redeem_code = token_result['redeem_code']
        return f'{retrieve_ovo_url()}?code={redeem_code}', True
    return None, False


def retrieve_required_info(command_body: {}) -> TokenRequestInfo:
    requester_id, approved_ids, has_extra_reps = retrieve_ids(command_body)
    group_name = retrieve_group_name(command_body)
    if has_extra_reps:
        return TokenRequestInfo(requester_id, group_name, approved_ids)
    else:
        return TokenRequestInfo(requester_id, group_name)


def retrieve_ids(command_body: {}) -> (int, int, bool):
    """filters reps and includes them if they not their own."""
    requester_id = command_body['member']['user']['id']
    if check_extra_reps(command_body):
        approved_ids = retrieve_extra_reps(command_body, requester_id)
        return int(requester_id), approved_ids, True
    else:
        return int(requester_id), None, False


def has_rep_role(roles: []) -> bool:
    for role in roles:
        if int(role) is JaegerEventRoles.OVO_REP or JaegerEventRoles.COMMUNITY_REP:
            return True
    return False


def retrieve_extra_reps(command_body: {}, requester_id) -> []:
    approved_ids = []
    members = command_body['data']['resolved']['members']
    for user_id, user_info in members.items():
        if user_id is not requester_id:
            if has_rep_role(user_info['roles']):
                approved_ids.append(int(user_id))
    return approved_ids


def check_extra_reps(command_body: {}) -> bool:
    for entry in command_body['data']['options']:
        if entry['name'] == 'extrareps':
            return True
    return False


def retrieve_group_name(command_body: {}) -> str:
    for entry in command_body['data']['options']:
        if entry['name'] == 'group':
            return entry['value']
