# Design strategy Basically start with an Evennia "talker" style mud. Implement
the minimum functions necessary to allow players to interact with each other and
try to achieve intimacy or eunoia.

# Control Communication

## Disable default commands that allow free form communication.

* all channels
* say
* whisper
* pose

## Implement Communication commands
* Attitudes
* Posture
* Signals
* Intimate conversation

# Give the game some objectives 

The objective should be to achieve intimacy
with other players.

# Determine the obstacles 

What if anything prevents the players from instantly achieving intimacy

## Create trade-offs

* Tough choices 
* What does a player have to sacrifice to achieve the objective?
* Why is that a challenge?

# Idea: Intimacy is a limited resource.
Time is limited too. All bodies die at a certain time. 
So you want to be as picky as possible about who you choose to be intimate
with.

# Matchmaking, fitness and Eunoia.
Final score is based on achieving the best possible match. Finding the right
partner.  Matchmaking score is subjective/objective

# Attributes
Playerbodies (player bots; bods; playerbod? hmmm) have attributes. Lets say
three attributes (two randomly assigned, one chosen from a list... or three
chosen from a draft... I don't know). Player bods have attributes. Bods also
have preferences or orientation or... a list of attributes they are attracted
to. 

## Proposed definitions of orientation and preference
* Orientation is the traits your body is naturally attracted to.
* Preferences are traits that the player chooses to favour.

## List of example traits or attributes
buff, soft, dainty, robust, virile, warm, angular, hot, cool, vibrant, scintilating, strong, weak, frail, hearty, sharp, smooth, rough, chiselled, mighty, demure, coy, steadfast, sincere, complex, shy, gregarious, belligerent, effervescent, silky, mean, confident, kind, sly, generous, stern, aloof, ...

I would like at least one hundred personal adjectives that describe body, character, personalilty...

## Attraction mechanic
Each player knows some of the traits they find specifically attractive. In fact
they have a natural response to every possible trait (natural meaning hidden in their body's code but not necessarily known to the player). 

## Aversion
Aversions are traits that repell the player body. A player does not immediately
know what traits they are averse to until they have encountered them. Spending
time in proximity to otherbodies with averse traits may carry a penalty. Some other bodies might have traits a player is attracted to, and others they are averse to, what a dilemna!

## Familiarity
Familiarity is a measure of how well a body knows another body. Familiarity can be mutual or imbalanced. Familiarity is a factor in intimacy. I'm not sure yet what the other factor(s) might be. But in practicaly terms familiarity means knowing what the other body's traits are. It can also include knowing what their preferences are.

# Itch bots 
So at the lowest levels of intimacy bots could easily masquerade as
players. They will try to attract players and waste their time.  Players can
compete with each other and with the bots for attention, trying to get the best
mates. Bots also 'poison the well' so to speak by reducing trust over all.
Players have to act out sometimes to distinguish themselves from bots.

# Compatibility 
Compatibility traits include objective fitness scores as well as subjective
complimentariness and also meta-game attributes like play styles, geo-region,
timezone, language etc.

# Distribution and testing 
This game will certainly need some critical mass of
players to actually find out if it works

But it is a design goal to make it playable and fun with low participation
rates. I think there are ways. For example build for asynchronous intimacy.
Find ways for players to interact by leaving signals and messages for each other

