# Learning Journal
Record facts as I learn them through trial, error, discovery, or advice.

# Current questions

## How do I build Limbo or other permanent rooms? 

Answer maybe to see : server/initial_setup.py
No, griatch says to use tags to help locate permanent rooms. 
I'm doing that and it is working but I'm feeling doubtful. I feel there should still be another way
of designating globally unique objects.

## How can I modify Limbo 
14:55 < j3b> Anyone have any idea how to change the default description of
             Limbo. I see that it is set as a global in server/initial_setup.py
14:56 < j3b> By the time my module server/conf/at_initial_setup.py runs the
             limbo object has already been created so changing the global
             doesn't do anything does it.
15:40 < evenniacode> [forum] j3b posted 'Is this the right way to use tags to
                     identify perma/ or hard coded objects in the db?'
<https://groups.google.com/d/msg/evennia/iE4elT4XdRE/YR1RLEmSAgAJ>
16:26 < Griatch> j3b: No, the at_initial_setup hook is indeed called after the
                 creation of the #1 user and Limbo. Since Limbo _is_ always #2,
                 you easily modify it from your initial_creation hook though.


### How would I do the same thing for the purpose of a unit test?
in the setup function ... 
Griatch says to override and mock. I'll have to figure out what that means.

# Latest Facts and answers
* in the test command the keyword argument "receiver" refers to which object will receive the input that we want the unit test to capture in order to assert as equal.

