from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from collections import namedtuple

from gecore.ps_discord_slash.configuration.config_constants import ConfigConstants
from gecore.ps_discord_slash.models.error_message import ErrorMessage

VerificationResult = namedtuple('VerificationResult', 'verified error')


def verify_key(headers, raw_body: str) -> VerificationResult:
    signature = headers['x-signature-ed25519']
    timestamp = headers['x-signature-timestamp']

    try:
        vk = VerifyKey(bytes.fromhex(ConfigConstants.discord_public_key))
        vk.verify(f'{timestamp}{raw_body}'.encode(), bytes.fromhex(signature))
        return VerificationResult(True, None)
    except BadSignatureError:
        return VerificationResult(False, ErrorMessage.SignatureIssue)
    except TypeError:
        return VerificationResult(False, ErrorMessage.TypeIssue)
    except ValueError:
        return VerificationResult(False, ErrorMessage.ValueIssue)
