# commands/body.py
"""
Commands for Eunoia bodies.
"""

from evennia import Command
from evennia.utils import logger


class CmdPing(Command):
    """
    Seek information about surrounding objects that are nearby*

    Usage:
      ping
      ping <other body>

    Without arguments it returns a list of all other nearby objects.

    With argument it returns basic information about the target other body.
    Pinging also gives up information about the body pinging, it reveals
    location, the fact that the body is pinging, and potentially other details
    to all bodies within range.
    """
    key = "ping"
    # locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location

        if not self.args:
            # general ping of surrounding
            message = "you..."
            # lmessage = f"\"ping!\" ... coming from {caller}"
            caller.msg(message)
            location.msg_contents(text=("ping!", {'type': 'ping'}),
                                  from_obj=caller)
            return

        target = caller.search(self.args.strip())

        if target == caller:
            message = "You don't ping yourself"
            caller.msg(message)
            return

        if target:
            message = f"You ping {target}."
            lmessage = f"\"ping!\" ... {caller} pings at {target}"
            tmessage = f"{caller} pings you"
            location.msg_contents(text=(lmessage, {'type': 'ping'}),
                                  from_obj=caller)
            caller.msg(message)
            location.msg_contents(text=(tmessage, {'type': 'ping'}),
                                  from_obj=caller)


class CmdOOB(Command):
    """
    Go 'out of body' and return to your 'character' in Limbo and the lobby
    where you can chat and stuff.

    Usage:
      OOB

      oob

    Takes no arguments. Just leaves the Euze part of the game immediately.
    Your body goes into safe storage while you're away.
    """
    key = "oob"

    def func(self):
        caller = self.caller
        account = self.account
        # character = self.account.character
        char = caller.db.char

        if char:
            # self.msg(f"You have a character: #{char.id}:{char.key}")
            # try to puppet it
            try:
                account.puppet_object(self.session, char)
                logger.log_sec(
                        f"Out of body success: (Caller: {caller}\n"
                        f"Character:{char.key}(#{char.id})\n"
                        f"IP: {self.session.address}"
                        )
            except RuntimeError as exc:
                self.msg("|rThat failed|n {msg}")
                self.msg(exc)
                logger.log_sec(
                        f"Puppet failed: (Caller: {caller}, "
                        f"Character:{char}, "
                        f"IP: {self.session.address}"
                        )
        else:
            self.msg("no character perhaps")
        return
