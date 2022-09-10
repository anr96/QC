my_integer = 567
print(type(my_integer))


# TODO: Change the value of my_float to a float 
# TIP: Change "_" so that when line 8 is ran, you see "I'm a  <class 'float'>" printed out)
my_float = 4.4
print("I'm a", type(my_float))


# TODO: There are 2 possible values for Booleans! Do you remember what they? Print them out and their types
boolean_value_true = True
boolean_value_false = False
print(boolean_value_true, "is a", type(boolean_value_true))
print(boolean_value_false, "is also a", type(boolean_value_true))

# TODO: Create any string and print it out and its type
my_string = "Wow, coding is so fun!"
print(my_string, type(my_string))

# TODO: What kind of data type(s) are the variables below? 
# Type in a comment below some of the differences in the creation/syntax of these
unknown_data_type1 = [1, "hello", "bye", False]
unknown_data_type2 = {"key1": "value1",
                      "key2": False  
                     }

print(type(unknown_data_type1))
print(type(unknown_data_type2))
# Amanda's observation: 
    # 1. lists are created using square brackets, they can be of any data type we have in lines 1-21
    # 2. dictionaries are createud using curly braces, they have key and value pairings
    #    the key and value are separated by the ':' character
    # 3. the values in a dictionary can be of any data type, just like lists