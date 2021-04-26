import json

from gecore.ps_discord_slash.models.interactions import InteractionType
from gecore.ps_discord_slash.models.response_models import error_response, pong_response, generic_response
from gecore.ps_discord_slash.verification import verifier


def lambda_handler(event, context):
    headers = event['headers']
    raw_body = event['body']
    verification_result = verifier.verify_key(headers, raw_body)
    if not verification_result.verified:
        return error_response(verification_result.error)
    json_body = json.loads(raw_body)
    interaction_type = json_body['type']
    if interaction_type == InteractionType.PING:
        return pong_response()
    command_result = process_command(json_body)
    result = generic_response(command_result.type, command_result.data)
    print(result)
    return result
