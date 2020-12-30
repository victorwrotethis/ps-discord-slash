from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import os

public_key = os.getenv('discordPublicApiKey')


def verify_key(headers, raw_body: str) -> bool:
    signature = headers['x-signature-ed25519']
    timestamp = headers['x-signature-timestamp']

    try:
        vk = VerifyKey(bytes.fromhex(public_key))
        vk.verify(f'{timestamp}{raw_body}'.encode(), bytes.fromhex(signature))
        return True
    except BadSignatureError as ex:
        print(ex)
        pass
    return False
