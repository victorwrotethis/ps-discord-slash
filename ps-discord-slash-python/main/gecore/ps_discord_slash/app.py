import json

from gecore.ps_discord_slash.implementations.load_available_commands import check_if_commands_loaded
from gecore.ps_discord_slash.models.default_interaction_responses import not_properly_executed_response
from gecore.ps_discord_slash.models.interactions import InteractionType, InteractionResponse, InteractionResponseType
from gecore.ps_discord_slash.models.response_models import error_response, pong_response, generic_response
from gecore.ps_discord_slash.processing.interaction_processor import InteractionProcessor
from gecore.ps_discord_slash.verification import verifier

interaction_processor = InteractionProcessor()


def lambda_handler(event, _context):
    #AWS
    headers = event['headers'] # AWS, although you do need the headers
    raw_body = event['body'] # AWS, although you do need a body
    print(raw_body) # AWS debugging since the start lol.

    ##Verification
    verification_result = verifier.verify_key(headers, raw_body)
    if not verification_result.verified:
        return error_response(verification_result.error)
    ## Manual implementation to load the commands
    check_if_commands_loaded(interaction_processor)
    json_body = json.loads(raw_body)
    interaction_type = json_body['type']
    ## ping, also semi verification
    if interaction_type == InteractionType.PING:
        return pong_response()
    ## any actual event processing
    interaction_result = interaction_processor.process_command_request(json_body)
    if not interaction_result:
        response = InteractionResponse(
                InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE, not_properly_executed_response()
            )
        return generic_response(response.type, response.data)
    result = generic_response(interaction_result.type, interaction_result.data)
    print(result) # AWS check what the hell we are even returning
    return result
