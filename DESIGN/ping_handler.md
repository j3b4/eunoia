# Ping Handler
This is a project to try to learn a bit about using "handlers" as per the 
advice of Kovitikus: [Handlers](https://github.com/kovitikus/hecate/blob/master/docs/evennia/Handlers.md)

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
<<<<<<< HEAD

  class PingHandler:
=======
	
>>>>>>> bc110abc0d8cac68c2ac077cb69aadc18db41682
	def __ini__(self, owner):
		self.owner = owner

	and then add all the methods that would act on the body (owner)
	of the handler when handling a ping.

# Things to handle
Well bodies do two things with ping. They ping and they get pinged. When they
get pinged the respond automatically by ponging back. 


# Thoughts
So my thought is that if it were not for handlers all the ping responding 
code would be in my different typeclasses. It could be customized. With the 
handler, do all types that use the handler have to process the ping the
same way?

I'll have to see.

# Stop.
Stop this project until I have a clear reason to use handlers. At this point, with this level of understanding it's really pre-mature optimization.
