import json
import jsonpickle

from gecore.ps_discord_slash.models.error_message import ErrorMessage
from gecore.ps_discord_slash.models.interactions import InteractionResponseType


content_json = {"content-type": "application/json"}


def error_response(error_message: ErrorMessage):
    print(error_message)
    return {
        "statusCode": 401,
        "headers": content_json,
        "body": json.dumps({
            "message": "invalid request signature"
        }),
    }


def pong_response():
    return {
        "statusCode": 200,
        "headers": content_json,
        "body": json.dumps({
            "type": InteractionResponseType.PONG
        })
    }


def generic_response(ir_type: InteractionResponseType, content):
    return {
        "statusCode": 200,
        "headers": content_json,
        "body": json.dumps({
            "type": ir_type,
            "data": json.loads(jsonpickle.encode(content, unpicklable=False))
        })
    }
