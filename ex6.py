x = "There are 10 types of people"
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x 
print y

print "I said: %r" % x
print "I also said: %s" % y

hilarious = False
joke_eval = "Isn't that funny? %r"

print joke_eval % hilarious

w = "This is left side "
e = "This is right side"

print w + e
