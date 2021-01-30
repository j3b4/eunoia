r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/j3/evdev/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "eunoia"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")


######################################################################
# Default Channels for players
######################################################################
# These are additional channels to offer. Usually, at least 'public'
# should exist. The superuser will automatically be subscribed to all channels
# in this list. New entries will be created on the next reload. But
# removing or updating a same-key channel from this list will NOT automatically
# change/remove it in the game, that needs to be done manually.
# DEFAULT_CHANNELS = [
    # helpme 
#    {
#        "key": "HelpMe",
#        "aliases": ("hm"),
#        "desc": "To ask for help from Helpers or Admins",
#        "locks": "control:perm(Admin);listen:perm(Helper);send:all()",
#    }
#]

######################################################################
# Default Account setup and access
######################################################################

# Different Multisession modes allow a player (=account) to connect to the
# game simultaneously with multiple clients (=sessions). In modes 0,1 there is
# only one character created to the same name as the account at first login.
# In modes 2,3 no default character will be created and the MAX_NR_CHARACTERS
# value (below) defines how many characters the default char_create command
# allow per account.
#  0 - single session, one account, one character, when a new session is
#      connected, the old one is disconnected
#  1 - multiple sessions, one account, one character, each session getting
#      the same data
#  2 - multiple sessions, one account, many characters, one session per
#      character (disconnects multiplets)
#  3 - like mode 2, except multiple sessions can puppet one character, each
#      session getting the same data.
MULTISESSION_MODE = 0
# The maximum number of characters allowed by the default ooc char-creation command
MAX_NR_CHARACTERS = 1

