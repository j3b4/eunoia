# Ping 
A ping is a sonic pulse a body may emit into the euze, it sounds like "ping".
Emitting a ping reveals your body's existence, position, and possibly other 
information. However it generates information for you as well, a ping echoes
off of other bodies and returns to you as a slightly muted "pong". Pong is the
sound of a reflected ping. Your body is able to deduce the size and distance of
another body (and perhaps whether it is hard or soft?) from the sound of a
pong. Pong has less range than ping (either half range, or one rank less of
range depending on how range is measured) this means of course that some bodies
will hear your ping without you hearing their pong. (Hearing a faint ping, at 
the lowest volume is an indication that you are outside of the pong range.)

Possibly, one can hear second hand pongs, that is, if another body emits a ping
within a certain range of you, you will hear pongs as well coming off of bodies
as long as they are in range for you. Pongs however do not echo any further and
will not generate any other type of sound.

Potentially there could be a skill called 'pong-shaping' that allows a body to
alter the information contained its pong. Similarly an ability called 
pong-muting might allow a body to completely absorb a ping without reflecting
any pong back. These two abilities would assist in stealth and skulduggery. 

Hearing a ping tells your body that another body is around. The ping
can reveal the direction of the emitting body but not necessarily the distance
because the emmittor might have reduced their output volume intentionally. 
If there is a max volume then at least an outside limit of range is suggested
by the volume of a ping.

If pings convey a particular trait, perhaps it is 'nice' or 'mean'. I don't 
know. If a body has ping-shaping abilities they might broadcast false traits.

## Ping memory short term
Your body has an ability to distinguish, remember and organize pings for a 
short term. That is, if after a silent period a body named x hears some pings
from bodies a, b, and c, x will be able to tell them apart as long as they do
not fall silent for too long. 

e.g. After a period of silence x's short term memory is clear. Then they head a
single ping that comes from a. X hears "ping-1". If bodies b or c then also
ping within 30 seconds they will be labelled "ping-2" and "ping-3" respectively.
This can build and all pings will be remembered distinctly until and unless 30
seconds of silence go by. If at any time that happens then the short term 
memory is reset.

## Ping long term memory.
Once a body has reached a certain level of intimacy, perhaps after touch, or a
kiss, and they have given a body a name, then they may recognize and remember a
body's distinctive ping whenever they hear it. It will come in as ping-name.

Of course if ping-shaping skills exist in the game, then it might be possible to
spoof another body's ping. What level of intimacy this requires is unknown.

## Ping notation (in the console)
In the game command line, pings (and pongs) are displayed as the word "ping" 
or "pong". Prefixes, suffixes, punctuation, and capitalization can be used to
add information to a ping. 

Volume perhaps: ping... Ping ... PING ... PING!  indicating soft to loud
pings.  

As in the example of short term ping memory ping-1 and ping-6 indicate that a
given ping is distinct within the group of pings heard lately. And ping-name 
might indicate a ping from a known body. 

# Specification for programming
* ping command with volume control
    * ping/soft to ping/loud  or perhaps use ping notation as the command
      itself - case sensitive commands.
* need to have implemented movement and relative positioning
* ping listening features:
    * decreasing volume
    * short term ping memory
    * long term ping memory
* pong features
    * decreasing volume.
    * short term memory for pongs as well??
    * long term pong memory??? can you recog a body by pong? Hmmm.
