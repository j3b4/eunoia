"""
At_initial_setup module template

Custom at_initial_setup method. This allows you to hook special
modifications to the initial server startup process. Note that this
will only be run once - when the server starts up for the very first
time! It is called last in the startup process and can thus be used to
overload things that happened before it.

The module must contain a global function at_initial_setup().  This
will be called without arguments. Note that tracebacks in this module
will be QUIETLY ignored, so make sure to check it well to make sure it
does what you expect it to.

"""

from evennia.utils import create, logger
from django.conf import settings

'''
LIMBO_DESC = (
        """
        Welcome to Limbo. You can do anything you want in Limbo.
        Welcome to Limbo. Anything is possible in Limbo! Limbo!
        """
        )
'''


def at_initial_setup():
    """ This is the final touches on Setup"""
    logger.log_info("Eunoia initial setup: Euze and other objects ...")

    room_typeclass = settings.BASE_ROOM_TYPECLASS
    euze_obj = create.create_object(room_typeclass, "Euze", nohome=True)
    # limbo_obj.id = 7
    euze_obj.tags.add("Euze")
    euze_obj.save()
    euze_obj.db.desc = "This is the Euze"
    euze_obj.save()
    # pass
