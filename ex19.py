def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that is for a party"
    print "Get a blanker.\n"

print "Give numbers directly"
cheese_and_crackers(20, 30)

print "Variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math: "
cheese_and_crackers(10 + 20, 5 + 6)

print "Two variables and a math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1003)
