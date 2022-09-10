name = "CJ"
favorite_color = 'purple'
age = 10


# TODO: create an activity

# We've printed out strings before, but how can we print out multiple variables at once?
# Similar to concatenation in activity one
print("Hi, I'm " + name + " and my favorite color is " + favorite_color)
# Similar to concatenation in activity two
# notice that when using the comma format, I don't need the spaces before/after the variable
print("Hi, I'm", name, "and my favorite color is", favorite_color)

# What if we try to do the above line, but with age?
print("Hi, I'm " + age)

# We need to update the type of age so that it's compatible with the string before it
# TYPE CASTING
print("Hi there, I'm " + str(age))

# and now we can print out all of our variables in one line!
print("Hello, I'm " + name + ". I'm " + str(age) + " years old and my favorite color is " + favorite_color)

# ALTERNATE METHOD (my preferred method) - STRING FORMATTING
# instead of having to type cast our non-string variables, we can use string formatting to automatically do that for us
print(f"Hello, I'm {name}. I'm {age} years old and my favorite color is {favorite_color}")

