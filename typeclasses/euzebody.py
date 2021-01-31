# typeclasses/euzebody.py
"""
Object

The Object is the "naked" base class for things in the game world.

Note that the default Character, Room and Exit does not inherit from
this Object, but from their respective default implementations in the
evennia library. If you want to use this class as a parent to change
the other types, you can do so by adding this as a multiple
inheritance.

"""
# from evennia import CmdSet
from typeclasses.characters import Character
from commands.body_cmdsets import CmdSetBody

class Body(Character):
    """
    The body is the type of object that populates the Euze.

    """
    def basetype_setup(self):
        """
        break away from default character cmdset
        """
        super().basetype_setup()
        self.locks.add(
                ";".join(["get:false()", "call:false()"]) 
        )
        self.cmdset.add_default(CmdSetBody, permanent=True)

    def at_after_move(self, source_location, **kwargs):
        """
        No looking around after move. 
        Just overloading this for now.
        """
        pass


