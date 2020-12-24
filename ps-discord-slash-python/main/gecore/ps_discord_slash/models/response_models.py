import json
import jsonpickle
from gecore.ps_discord_slash.models.interactions import InteractionResponseType


def error_response():
    return {
        "statusCode": 401,
        "body": json.dumps({
            "message": "invalid request signature"
        }),
    }


def pong_response():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "type": InteractionResponseType.PONG
        })
    }


def generic_response(ir_type: InteractionResponseType, content):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "type": ir_type,
            "data": json.loads(jsonpickle.encode(content, unpicklable=False))
        })
    }