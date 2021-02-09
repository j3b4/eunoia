# eunoia/commands/tests.py

# import unittest
from evennia.commands.default.tests import CommandTest
from evennia.utils.test_resources import EvenniaTest
from commands.command import CmdIB
from commands.body import CmdOOB
from typeclasses.euzebody import Body
from typeclasses.characters import Character
from evennia.commands.default import general


class TestLookChar(CommandTest):
    """just look first as a character"""

    def test_look(self):
        """looks in ther room as the acharacter"""
        lookscene = "Char(#6)"
        self.call(general.CmdLook(), "me", lookscene)
        extralook = general.CmdLook()


class TestCmdIB(CommandTest):
    """Unittest of IB. Should create a body and go into it."""
    # body_typeclass = Body

    def test_simple(self):
        CmdIB_results = self.call(CmdIB(), "")
        self.assertRegex(CmdIB_results, "Created new body: Nebody for \d+\n"
                                        "You have a body: #\d+")
        # looks in ther room as the body
        lookscene = "Char(#6)"
        self.call(general.CmdLook(), "me", lookscene)
        print("Looked at me as a body.")


class TestCmdOOB(CommandTest):
    """Testing OOB which should return a player to their character"""
    # character_typeclass = Character

    def test_simple(self):
        CmdOOB_results = self.call(CmdOOB(), "")
        Expectation = ('You have a character: #\d+')
        self.assertRegex(CmdOOB_results, Expectation)
