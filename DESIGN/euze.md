# Enter the Euze
This describes the concept of entering the proper Eunoia game from a standard 
vanilla Evennia mud in multisession=0. So upon entering the game you are in a
lobby with standard Evennia rooms, and commands. "Look" reveals other objects,
player characters, and exits. One of the exits (or commands) available in the 
lobby allows you to enter the Euze.

# The Euze
When you enter the Euze you are assigned a new 'body' which has almost none of
the standard Evennia commands. No "look", no "say" or "get" for example. Also
your body has an arbitrary name or key which might not even...

Anyway the Euze is the real game. 

## Design notes
So I think that entering the Euze is achieved by removing all the default
cmd_sets and offering some new ones. Should it involve creating a new
character object? Yes maybe. That makes the most sense. 

So the Euze command puppets a new character/body... euzebody is a typeclass.

# Euzebody
limited commandsets
arbitrary name or key
traits
look returns something arbitrary  - like only select traits and attitudes
