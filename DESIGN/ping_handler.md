# Ping Handler
This is a project to try to learn a bit about using "handlers" as per the 
advice of Kovitikus (see outline.otl for a link).


# Purpose
Honestly I'm not entirely sure but I feel intuitively that the handler system
will be useful for dealing with the various forms of communication between
bodies and bots.

# General idea
In the body typeclass definition import and use @lazy_property 
above a method for dealing with pings.
The method simply returns PingHandler(self)  - PingHandler needs to have been
imported.

Write a handler module, somewhere, and in it define a PingHandler class.
	
	def __ini__(self, owner):
		self.owner = owner

	and then add all the methods that would act on the body (owner)
	of the handler when handling a ping.


# Thoughts
So my thought is that if it were not for handlers all the ping responding 
code would be in my different typeclasses. It could be customized. With the 
handler, do all types that use the handler have to process the ping the
same way?

I'll have to see.
