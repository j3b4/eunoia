# eunoia/commands/tests.py

# import unittest
from evennia.commands.default.tests import CommandTest
# from evennia.utils.test_resources import EvenniaTest
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
        # extralook = general.CmdLook()


class TestCmdIB(CommandTest):
    """Unittest of IB. Should create a body and go into it."""
    def setUp(self):
        self.character_typeclass = Character
        self.body_typeclass = Body
        super(TestCmdIB, self).setUp()

    def test_simple(self):
        Results = self.call(CmdIB(), "")
        Expectation = ("Created new body: Nebody for \d+|"
                       "You have a body: #\d+")
        self.assertRegex(Results, Expectation)
        # self.assertEqual(self.body.id, "8")


class TestCmdOOB(CommandTest):
    """Testing OOB which should return a player to their character"""
    # character_typeclass = Character

    def test_simple(self):
        CmdOOB_results = self.call(CmdOOB(), "")
        Expectation = ('You have a character: #\d+')
        self.assertRegex(CmdOOB_results, Expectation)
