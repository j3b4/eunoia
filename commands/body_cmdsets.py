# commands/body_cmdsets.py

from evennia import CmdSet
from commands.body import CmdPing
from evennia.commands.default import account, help


class CmdSetBody(CmdSet):
    key = "Body Commands"
    mergetype = "Replace"
    priority = 10

    def at_cmdset_creation(self):
        self.add(CmdPing())
        self.add(account.CmdWho())
        self.add(account.CmdQuit())
        self.add(account.CmdOOC())
        self.add(help.CmdHelp())
