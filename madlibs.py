
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
pnoun = input("Enter a plural noun: ")
bodypart = input("Enter a body part: ")
number = int(input("Enter a whole number: "))
place = input("Enter a place: ")
ingverb = input("Enter a verb ending with ing: ")

def madlib1():
    print ("I had a " + noun + " it was very " + adjective + 
    ". The " + pnoun + " always keep chirping on my " 
    + bodypart + ".I ate " + pnoun + " " + str(number) + " times more than cherries." +
    " I always go to " + place + ". At this place all the people there are always " + ingverb + ".")

def madlib2():
    print ("It was a " + adjective + " car. I saw it coming from afar and it had a  "
    + noun + ". The car crosses a lot of  "
    + pnoun + " while driving to " + place + ". It was " + ingverb + " down the road. "
    + " The " + pnoun + " were very annoyed with the sound of the car which was " + str(number) + " horsepower" + "! " +
    "I felt teh chills going down my " + bodypart + ".")

def madlib3():
    print ("My " + noun + " is always kept under the bed. My bed is  " + adjective
    + " . I went to check under my bed adn  "
    + place + ". I found some " + pnoun + " under my bed. I was terrified because they started crawling on my "
    + bodypart + "! This pain hurt " + str(number) + " times more than an ACL tear. I shook off the pain, and started " +
    ingverb + " with some of my friends.")

storynumber = input(" Which story would you like to play? (1, 2, 3, or q): ")

if storynumber == "1":
    madlib1()
elif storynumber == "2":
    madlib2()
elif storynumber == "3":
    madlib3()
elif storynumber == "q":
    print("You have succesfully quit")
else:
    print("Invalid input. Click run and choose again")