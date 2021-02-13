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

TRAITS = [("warm", "cool"), ("nice", "mean"), ("soft", "hard")]
# TRAITS as a list of tuples should allow me to access values a
# eg: TRAITS[2][1] is "hard", TRAITS[1][0] is "nice".


class Body(Character):
    """ The body is the type of object that populates the Euze.
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

    def at_object_creation(self):
        """
        Create the traits and preferences.j
        """
        import random
        b = []  # body type
        a = []  # attraction type
        for x in TRAITS:
            a.append(random.choice(x))
            b.append(random.choice(x))
        self.db.bodytype = b
        self.db.attraction = a

    def at_after_move(self, source_location, **kwargs):
        """
        No looking around after move.
        Just overloading this for now.
        """
        pass


class Itchbot(Body):
    """
    Itch bots are inspired by fake multi players in itch.io games. They do
    their best to impersonate other real player bodies.
    """

    def at_death(self):
        pass

    def at_pbody_present(self, pbody):
        """
        Try to interact with other bodies when players are online and
        in the Euze.
        """
        # When a player is present then start a ticker to randomly ping
        # other bodies and sometimes the world.
        pass

    def at_ping_receive(self, message):
        """
        If a direct ping received try to intereact with that body with
        higher priority.
        """
        response = None
        if message is not None:
            response = 1
        return response

    def msg(self, text=None, from_obj=None, **kwargs):
        """
        Custom msg() listenning for pings.
        TODO: Pings seems to lave a "from_obj" and so they are
        giving us trouble.
        """

        if from_obj != self:
            print(f"MSG:{text[0]} TYPE:{text[1]}  FROM: {from_obj}")
            # we must ignore our own pings
            # words = text[0]
            # print(f"{self} heard {text[0]} < out of {from_obj}")
            if 'ping' in text[0]:
                # ping back
                if from_obj is not None:
                    print(f"I heard a from {from_obj}")
                    self.execute_cmd(f"ping {from_obj}")
        super().msg(text=text, from_obj=from_obj, **kwargs)
