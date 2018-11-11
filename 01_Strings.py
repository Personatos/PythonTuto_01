# Strings manipulation rules


# strings can be writen in double quotes or single quotes
string_double = "This is a string in double quotes "
string_single = 'This is a string in single quotes '

print (string_double)
print (string_single)

# if you wana use the same double and single quotes inside the string, use \ before the type of quote that you're using

strings_same_chars_01 = 'i don\'t like single quote inside this single quoted string. But it works!'
strings_same_chars_02 = "I used \"double quoutes\" inside this double quoted string"

print (strings_same_chars_01)
print (strings_same_chars_02)

# you can usa raw string. Useful for paths
# And you can add strings

string_no_raw = "c:\\home"
string_raw = r"c:\\home"

print("String with no raw:  " + string_no_raw)
print("String with raw:  " + string_raw)

# and you can multiply strings

string_to_repeat= "Piu "
print('String "' + string_to_repeat + '" multiplied by 5:  ' + (string_to_repeat * 5) )

# Getting characters from string

string_to_char = "0123 is the way to count strings but don't forget the -1 in the end"
print() # blank line
print('Look at the string: " ' + string_to_char + ' "')
print("the char in position 0 is: " + string_to_char[0])
print("the char in the last position is: " + string_to_char[-1] + "  or:  " + string_to_char[len(string_to_char)-1])
print("I can take the char '3' by doing: " + string_to_char[3] + "  or:  " + string_to_char[-64])
      
# Getting strings form strings

print("If you want just the numbers: " + string_to_char[0:4] + "  or:  " + string_to_char[:4])

# length of a string

print("the length of the string is: " + str(len(string_to_char)) + " chars")
