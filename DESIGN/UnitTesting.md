# Unit Testing

# Test Body creation.

# Learn unit testing
Review
https://github.com/evennia/ainneve/blob/master/commands/tests.py
and other examples until I know what I'm doing or at the very least until 
I have some decent questions to ask.

## Learning plan
Start a document with a list of tests described in a format roughly like this:

"When a player does X, the game should do Y (and display or message Z)."

For example:

### Test CmdIB "ib"

When a player enters "ib" while in character and they do not already have a i
body the game should create a new body for them and message the player: 
"you created a new body", and then cause the  player's account to begin 
puppeting the new body in the room called Euze.

When a player already has a body, then the "ib" command should simply cause
them to start puppeting the body in whatever location it was last. 

The test for this should be able to puppet a body.

### Test CmdOOB "oob"

When a player is puppetting a body the 'oob' command should be available.
When called, it should unpuppet the players body, and put them back into 
their "character" in Limbo or related rooms. Cause them to puppet their
character.

