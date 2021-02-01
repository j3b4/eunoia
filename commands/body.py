# commands/body.py
"""
Commands for Eunoia bodies.
"""

from evennia import Command
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


