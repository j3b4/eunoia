# commands/body.py 
"""
Commands for Eunoia bodies.
"""

from evennia import Command
from evennia.commands.default import  help, building, account, general
from typeclasses.euzebody import Body
from evennia.utils import utils, create, logger, search


class CmdIB(Command):
    """
    Go into your body, in the Euze and play Eunoia. 

    Usage:
      ib

    This command is available to your character in Limbo and adjacent rooms. If you
    already have a 'body' in the Euze then your puppet it immediately. If you do not
    presently have a live body then you will be taken to a body creation room or menu
    or something.
    """

    key = "ib"

    def func(self):
        from evennia.objects.models import ObjectDB
        caller = self.caller
        account = self.account

        # if you have a body, puppet it.
        # begs the question what is it to 'have' a body?

        # if you do not have a body, go to newbody routine.
        typeclass = Body
        start_location = ObjectDB.objects.get_id("Euze") # TODO: make this more dynamic
        default_home = start_location
        permissions = "body"
        key = "Nebody"

        # create the body
        new_body = create.create_object(typeclass, key=key, location=start_location,
                home=default_home, permissions=permissions
        )

        # only creator can puppet
        new_body.locks.add(f"puppet:id({new_body.id}) or pid({account.id})")

        # return some sort of message
        self.msg(f"Created new body: {key}. So that's a start.")
        logger.log_sec(
                f"Body created: {key} (Caller: {account}, IP:{self.session.address}"
                )



class CmdPing(Command):
    """
    seek information about surrounding objects that are nearby*

    Usage:
      ping
      ping <other body>

    Without arguments it returns a list of all other nearby objects.

    With argument it returns basic information about the target other body. Pinging
    also gives up information about the body pinging, it reveals location, the fact
    that the body is pinging, and potentially other details to all bodies within
    range.
    """
    key = "ping"
    # locks = "cmd:all()" 
    def func(self):
        caller = self.caller
        location = caller.location

        if not self.args:
            # general ping of surrounding
            message = "You try to ping but it doesn't tell you much yet."
            lmessage = f"\"ping!\" ... coming from {caller}"
            caller.msg(message)
            location.msg_contents(lmessage)
            return

        target = caller.search(self.args.strip())

        if target == caller:
            message = "You don't ping yourself"
            caller.msg(message)
            return

        if target:
            message = f"You ping {target}."
            tmessage = f"{caller} pings you."
            lmessage = f"\"ping!\" ... {caller} pings at {target}"
            location.msg_contents(lmessage)
            caller.msg(message)
            target.msg(tmessage)


