print("Welcome! This program performs text mining into a dictionary.")
print()

# Open the file to extract
text = open("text.txt", "r")

# Read the entire file
infile = text.read()

# Close the file to increase memory space
text.close()

# List of special characters to be removed from the file
special_characters = [",", "."]

for every_character in special_characters:
    infile = infile.replace(every_character, "")

# Converts all the block of strings to lowercase characters
infile = infile.lower()

# Converts string to list using the space between each word
infile = infile.split()

# Create an empty dictionary to hold the key-value pair
dictionary = {}

for each_word in infile:
    word_count = infile.count(each_word)  # count each word
    dictionary[each_word] = word_count

print("The result of the text mining is:")
print("---------------------------------")
print()
print(dictionary)
