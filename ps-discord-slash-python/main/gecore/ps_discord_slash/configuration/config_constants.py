import os

class ConfigConstants:
    discord_public_key = os.getenv('discord_public_api_key')
    discord_app_id = os.getenv('discord_app_id')
    discord_agent_name = os.getenv('discord_agent_name')
