import json

from gecore.ps_discord_slash.implementations.load_available_commands import check_if_commands_loaded
from gecore.ps_discord_slash.models.default_interaction_responses import not_configured_response
from gecore.ps_discord_slash.models.interactions import InteractionType, InteractionResponse, InteractionResponseType
from gecore.ps_discord_slash.models.response_models import error_response, pong_response, generic_response
from gecore.ps_discord_slash.processing.command_processor import CommandProcessor
from gecore.ps_discord_slash.verification import verifier

command_processor = CommandProcessor()


def lambda_handler(event, context):
    headers = event['headers']
    raw_body = event['body']
    print(raw_body)
    verification_result = verifier.verify_key(headers, raw_body)
    if not verification_result.verified:
        return error_response(verification_result.error)
    check_if_commands_loaded(command_processor)
    json_body = json.loads(raw_body)
    interaction_type = json_body['type']
    if interaction_type == InteractionType.PING:
        return pong_response()
    command_result = command_processor.process_command_request(json_body)
    if not command_result:
        response = InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, not_configured_response()
            )
        return generic_response(response.type, response.data)
    result = generic_response(command_result.type, command_result.data)
    print(result)
    return result
