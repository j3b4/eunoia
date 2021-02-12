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


class TestCmdIB(CommandTest):
    """Unittest of IB. Should create a body and go into it."""
    def test_simple(self):
        Expectation = ("Created new body: Nebody for 6|"
                       "You have a body: #8")
        self.call(CmdIB(), "", Expectation, caller=self.account,
                  )


class TestCmdOOB(CommandTest):
    """Testing OOB which should return a player to their character"""
    # character_typeclass = Character

    def test_simple(self):
        CmdOOB_results = self.call(CmdOOB(), "")
        Expectation = ('You have a character: #6')
        self.assertRegex(CmdOOB_results, Expectation)
