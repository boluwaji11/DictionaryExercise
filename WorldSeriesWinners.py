###############Declare the main function
def main():
    # Display the program header
    print("--------------------------------------------------------------")
    print("\tWelcome to the World Series Champions Database")
    print("--------------------------------------------------------------")

    choice = 0  # Placeholder variable for the while loop
    while choice != 3:

        print()
        # Display Home Menu list
        print("===========")
        print("---MENU---")
        print("===========")
        print("1. Search Winner by Year")
        print("2. View all Championship winners (1903-2008)")
        print("3. Quit Program")
        print()
        choice = int(
            input("From the menu list, select your desired request (1 to 3): ")
        )

        # Run the request
        if choice == 1:
            year_search(file_open())
            print()
            input("Press Enter to see the menu list again... ")
        elif choice == 2:
            view_all(file_open())
            print()
            input("Press Enter to see the menu list again... ")
        elif choice == 3:
            print("Program is exiting..... Thanks for using the program.")
        else:
            print("\nError: Invalid selection!")
            print("Enter a number between 1 and 3")
            input("\nPress Enter to make selection again... ")


####################Declare the file_open function
def file_open():
    # Open the file to extract
    winners = open("WorldSeriesWinners.txt", "r")

    # Read the entire file
    infile = winners.read()

    # Close the file to increase memory space
    winners.close()

    # Converts string to list using each line space
    infile = infile.split("\n")

    return infile


####################Declare the year_search function
def year_search(infile):
    # Create an empty dictionary to hold the key-value pair
    dictionary1 = {}

    for each_word in infile:
        win_count = infile.count(each_word)  # count each word
        dictionary1[each_word] = win_count

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

    # Request user search input
    print()
    year_search = int(input("Please Enter the Year to Search: "))

    # Display search result
    team_output = dictionary2.get(year_search)
    frequency_output = dictionary1.get(team_output)

    print(
        "=============================================================================="
    )
    if year_search == 1904 or year_search == 1994 or year_search < 1903:
        print("No World Series played in the year ", year_search, ".", sep="")
    elif year_search > 2008:
        print("No championship information on record.")
    else:
        print(
            "In the year ",
            year_search,
            ", the ",
            team_output,
            " won the World Series.",
            sep="",
        )
        print(
            "So far, they've won the championship series", frequency_output, "time(s)."
        )
    print(
        "=============================================================================="
    )


####################Declare the view_all function
def view_all(infile):

    # Create a list of the championship years
    year_list = []
    for i in range(1903, 2009):
        if i == 1904 or i == 1994:  # Excluding the years without championship games
            continue
        year_list.append(i)

    # Convert the elements to strings
    year = list(map(str, year_list))

    # Using a zip iterable to combine the winning year and team lists
    year_team = zip(year, infile)

    # Display Full list of winners and year won
    print()
    print("\t---------------------------------------")
    print("\t        List of Winners per Year")
    print("\t---------------------------------------")
    for all_team in year_team:
        print(" ".join(all_team))  # Display all winners


################Call the Main Function
main()