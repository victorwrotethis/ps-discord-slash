from gecore.ps_discord_slash.commands.command_name_interface import SlashCommandName


class OvOSlashCommand(SlashCommandName):
    SEARCH_BASE_ID = 'searchbaseid'
    REQUEST_ACCOUNT = 'request_account'
    REQUEST_ACCOUNTS = 'request_accounts'
    RESERVATION = 'reservation'
    MANAGE_COMMAND = 'manage'

    @staticmethod
    def provide_members():
        return OvOSlashCommand.__members__.values()
