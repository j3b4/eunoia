# eunoia/commands/tests.py

# import unittest
from evennia.commands.default.tests import CommandTest
# from evennia.utils.test_resources import EvenniaTest
from commands.command import CmdIB
from commands.body import CmdOOB
# from typeclasses.euzebody import Body
# from typeclasses.characters import Character
from evennia.commands.default import (
        general,
        account,
        # help,
        # admin,
)


class TestLookChar(CommandTest):
    """just look first as a character"""

    def test_look(self):
        """looks in ther room as the acharacter"""
        lookscene = "Char(#6)"
        self.call(general.CmdLook(), "me", lookscene)


class TestAccount(CommandTest):
    """Emulate the built-in test"""
    def test_ooc(self):
        self.call(account.CmdOOC(), "", "You go OOC.", caller=self.account)

    def test_ic(self):
        self.account.db._playable_characters = [self.char1]
        self.account.unpuppet_object(self.session)
        self.call(
                 account.CmdIC(), "Char", "You become Char.",
                 caller=self.account,
                 receiver=self.char1)


class TestCmdBody(CommandTest):
    """
    Unittest of IB. Should create a body and go into it.
    Then come leave the body and come back out.
    """
    def test_IB(self):
        self.call(
                CmdIB(), "", "You become Nebody.",
                caller=self.char1,
                receiver=self.char1,
                )

    def test_OOB(self):
        self.call(CmdOOB(), "", "You become Char.")
