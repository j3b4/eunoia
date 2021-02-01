# permutaions.md
In testing we want simplicity.
5 traits. Each body has 3 expressed, 3 preferred and 2 disliked.

This results in 10 body types (BTs):
abc abd abe acd ace ade bcd bce bde cde

Also 10 'likes' (LTs):
abc abd abe acd ace ade bcd bce bde cde

Which means 100 Body-Like types (BLs):
abcabc abcabd abcabe abcacd abcace abcade abcbcd abcbce abcbde abccde abdabc
abdabd abdabe abdacd abdace abdade abdbcd abdbce abdbde abdcde abeabc abeabd
abeabe abeacd abeace abeade abebcd abebce abebde abecde acdabc acdabd acdabe
acdacd acdace acdade acdbcd acdbce acdbde acdcde aceabc aceabd aceabe aceacd
aceace aceade acebcd acebce acebde acecde adeabc adeabd adeabe adeacd adeace
adeade adebcd adebce adebde adecde bcdabc bcdabd bcdabe bcdacd bcdace bcdade
bcdbcd bcdbce bcdbde bcdcde bceabc bceabd bceabe bceacd bceace bceade bcebcd
bcebce bcebde bcecde bdeabc bdeabd bdeabe bdeacd bdeace bdeade bdebcd bdebce
bdebde bdecde cdeabc cdeabd cdeabe cdeacd cdeace cdeade cdebcd cdebce cdebde
cdecde

And every BL dislikes the two traits it doesn't like.
To be clear, what you are doesn't affect what you like or dislike. But you 
cannot like and dislike a trait. So any BL's dislikes can be deduced from
whatever is not in the last 3 trait list.

In this case, there is no distinction between dislike and indifference.

variation:

Consider if each trait is onepart of a binary. Any trait not expressed IS it's
opposite. This lets me have 10 traits for the price of 5.
Example traits:

```
bold, mean, tough, hot, honest
shy, nice, soft, cool, sly
```
* does this change the indifference mechanic? Sort of. It is not clear if you
dislike the opposites of things you like. 

If so, then you really have 5 likes and 5 dislikes. But still only 100 BL types
exist in the world. That's probably fine.

It also means that each body has 5 apparent traits even though only 3 need to 
be selected. So I've invented a 5-bit set of personalities. "Brilliant."
