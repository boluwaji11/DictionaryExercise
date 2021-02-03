# Open the file to extract
winners = open("WorldSeriesWinners.txt", "r")

# Read the entire file
infile = winners.read()

# Close the file to increase memory space
winners.close()

# Converts string to list using each line space
infile = infile.split("\n")

# Create an empty dictionary to hold the key-value pair
dictionary1 = {}

for each_word1 in infile:
    win_count = infile.count(each_word1)  # count each word
    dictionary1[each_word1] = win_count

print("Dictionary with Team Name as keys and Win Frequency as values:")
print("---------------------------------------------------------------")
print()
# print(dictionary1)
print()

print("Dictionary with Year as keys and Team Name as values:")
print("---------------------------------------------------------------")
search = int(input("Please Enter the Year: "))  # Search option for users
print()

# Create a list of the championship years
year = []
for i in range(1903, 2009):
    if i == 1904 or i == 1994:  # Excluding the years without championship games
        continue
    year.append(i)

# Using a zip iterable to combine the winning year and team lists
year_team = zip(year, infile)

# Convert the iterable to a dictionary
dictionary2 = dict(year_team)

# Print Output
print("The World Series Champion", "in", search, "was the", dictionary2[search])
# print("They have won the Championship", dictionary1[win_count])
