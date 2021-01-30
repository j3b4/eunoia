# The Silence Module overloads built in Evennia communication commands
# and ups their permissions so that only staff can use them. 

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

#
# Hmm
#

#        self.remove(default_cmds.CmdAddCom)
#        self.remove(default_cmds.CmdAllCom)
#        self.remove(default_cmds.CmdCBoot)
#        self.remove(default_cmds.CmdDelCom)
#        self.remove(default_cmds.CmdChannels)
#        self.remove(default_cmds.CmdCdestroy)
class CmdChannelCreate(default_cmds.CmdChannelCreate):
    locks = 'cmd:perm(Helper)'


class CmdChannelCdestroy(default_cmds.CmdCDestroy):
    locks = 'cmd:perm(Helper)'


class CmdChannels(default_cmds.CmdChannels):
    locks = 'cmd:perm(Helper)'
        
#        self.remove(default_cmds.CmdClock)
#        self.remove(default_cmds.CmdCBoot)
#        self.remove(default_cmds.CmdCemit)
#        self.remove(default_cmds.CmdCWho)
#        self.remove(default_cmds.CmdCdesc)
#        self.remove(default_cmds.CmdChannels)
#        self.remove(default_cmds.CmdPage)
