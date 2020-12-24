import json

from gecore.ps_discord_slash.models.interactions import InteractionType
from gecore.ps_discord_slash.models.response_models import error_response, pong_response, generic_response
from gecore.ps_discord_slash.processing.processor import process_command
from gecore.ps_discord_slash.verification import verifier


def lambda_handler(event, context):
    headers = event['headers']
    raw_body = event['body']
    verified = verifier.verify_key(headers, raw_body)
    if not verified:
        return error_response()
    json_body = json.loads(raw_body)
    interaction_type = json_body['type']
    if interaction_type == InteractionType.PING:
        return pong_response()
    command_result = process_command(json_body)
    return generic_response(command_result.type, command_result.data)
