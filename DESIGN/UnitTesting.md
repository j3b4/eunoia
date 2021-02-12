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


# Help

<j3b> The next mystery I'm setting out to learn is how to build a permanent
room like Limbo into my code for two different purposes. (1) in the actual game
I want another room to always exist with a particular dbref (or other way to be
able to write code around it). and (2) I need the same room available for unit
testing.D:BOTToday at 8:36 AM
<j3b> server/initial_setup.py ?D:BOTToday at 9:18
AM
<Griatch> You don't use a hardcoded room for unittesting. Mock it or override
it for the test.[9:19 AM]
<Griatch> The @override_settings decorator from Django
can be used to override Django settings per-test. And you can use mocking to
direct to a test-room you generate for that test.[9:19 AM]
<Griatch> You should
never depend on a specific dbref for a unittest.1[9:23 AM]
<Griatch> The only
reason we have #2 for Limbo is because it's needed as a minimum starting point
when building the database (like #1 will be user #1). I'd suggest using tagging
to find and identify your 'permanent' room instead.

