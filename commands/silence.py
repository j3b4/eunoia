# The Silence Module overloads built in Evennia communication commands
# and ups their permissions so that only admins can use them. 

from evennia import default_cmds
from evennia import CmdSet, Command

# TODO: 
# Overload Say, Whisper, Pose, SetDesc

class CmdSay(default_cmds.CmdSay):
    key = 'say'
    locks = 'cmd:perm(Helper)'

class CmdWhisper(default_cmds.CmdWhisper):
    key = 'whisper'
    locks = 'cmd:perm(Helper)'

class CmdPose(default_cmds.CmdPose):
    key = 'pose'
    locks = 'cmd:perm(Builder)'

class CmdSetDesc(default_cmds.CmdSetDesc):
    key = 'setdesc'
    locks = 'cmd:perm(Builder)'

