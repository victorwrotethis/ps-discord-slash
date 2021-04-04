from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import os
from collections import namedtuple

from gecore.ps_discord_slash.implementations.bases.models.error_message import ErrorMessage

public_key = os.getenv('discord_public_api_key')

VerificationResult = namedtuple('VerificationResult', 'verified error')


def verify_key(headers, raw_body: str) -> VerificationResult:
    signature = headers['x-signature-ed25519']
    timestamp = headers['x-signature-timestamp']

    try:
        vk = VerifyKey(bytes.fromhex(public_key))
        vk.verify(f'{timestamp}{raw_body}'.encode(), bytes.fromhex(signature))
        return VerificationResult(True, None)
    except BadSignatureError:
        return VerificationResult(False, ErrorMessage.SignatureIssue)
    except TypeError:
        return VerificationResult(False, ErrorMessage.TypeIssue)
    except ValueError:
        return VerificationResult(False, ErrorMessage.ValueIssue)
