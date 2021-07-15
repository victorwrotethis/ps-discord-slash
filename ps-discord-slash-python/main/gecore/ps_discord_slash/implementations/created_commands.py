from gecore.ps_discord_slash.commands.command_name_interface import InteractionCommandName


class OvOInteractionCommand(InteractionCommandName):
    SEARCH_BASE_ID = 'searchbaseid'
    REQUEST_ACCOUNT = 'request_account'
    REQUEST_ACCOUNTS = 'request_accounts'
    RESERVATION = 'reservation'
    TEST_GLOBAL = 'globaltest'

    @staticmethod
    def provide_members():
        return OvOInteractionCommand.__members__.values()
