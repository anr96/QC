# set up our variables
person1 = "Alex"
age1 = 23
likes_coding = False

person2 = "Priya"
age2 = 35
likes_coding = True

person3 = "Eden"
age3 = 23
likes_coding = True


#------------------------------------------------------------------------------------
# we can do conditions where we are checking against a fixed value, like a number
if age1 > 18:
    print("You are an adult")

#if likes_coding:
if likes_coding == True:
    print("Yay, you're in the right class")
else:
    print("That's ok! Let me know if you change your mind")

#------------------------------------------------------------------------------------
# we can also check conditions between/compare variables to each other
if age1 > age2:
    #means that person1 is older than person2
    print(f"{person1} is older than {person2}")
elif age1 < age2:
    #means that person1 is older than person2
    print(f"{person1} is younger than {person2}")
else:
    #default value, but we know if you are not younger or older, you are the same age
    print(f"{person1} is the same age as {person2}")
    