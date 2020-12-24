from gecore.ps_discord_slash.models.discord_config import JaegerEventRoles, JaegerEventChannel


def check_if_allowed_role(roles) -> bool:
    for role in roles:
        print(role)
        if int(role) in JaegerEventRoles.__members__.values():
            return True
    return False


def check_if_correct_channel(channel_id) -> bool:
    if int(channel_id) in JaegerEventChannel.__members__.values():
        return True
    else:
        return False
