#String Manipulation:

single_qoute = 'Hello' #String
double_qoute = "World" #String
triple_qoute = """Multi-line string""" #String

text = "Python Programming" #01234567890123
#       0123456789

print(text[0])      #first character #P
print(text[-1])     #last character #g
print(text[0:6])    #slice 0 to 5 #Python
print(text[:6])     #from start to 5 #Python
print(text[7:18])   #7 to 17 #Programming   
print(text[7:])     #7 to end #Programming

# String Method:

name = " bob the builder "

print(len(name))                        #length
print(name.strip())                     #Remove Whitespace
print(name.upper())                     #Uppercase
print(name.lower())                     #Lowercase
print(name.title())                     #title case
print(name.replace("bob", "jane"))      #Replace

#String Formatting:

name = "John Doe"
age = 30

message_1 = f"My name is {name} and I am {age} years old."           #f-strings
message_2 = "My name is {} and I am {} years old.".format(name, age) #str.format()
message_3 = "My name is %s and I am %d years old." % (name, age)     #%-formatting

print(message_1)
print(message_2)
print(message_3)

#Exercise:
#Build a simple text analyzer that counts words, characters, and
#sentences in a given text.
 
text = """Python is a powerful programming language. It's easy to learn
 and versatile!
 You can use Python for web development, data science, and
 automation. The syntax is clean and readable.
 This makes Python perfect for beginners and experts alike."""

# Count characters (includingpython  spaces and punctuation)
char_count = len(text)

# Count words (split by whitespace)
word_count = len(text.split())

# Count sentences (split by '.', '!', '?')
sentence_count = text.count(".") + text.count("!") + text.count("?")


print("Character count:", char_count)
print("Word count:", word_count)
print("Sentence count:", sentence_count)


#Solution from Zarul
#char_count = len(text)
#char_count_no_spaces = len(text.replace(' ', ''))
#word_count = len(text.split())
#sentence_count = text.count('.') + text.count('!') + text.count('?')

#rint(f"Character count (including spaces): {char_count}")            # 239
#print(f"Character count (excluding spaces): {char_count_no_spaces}")  # 204
#print(f"Word count: {word_count}")                                    # 38
#print(f"Sentence count: {sentence_count}")                            # 5