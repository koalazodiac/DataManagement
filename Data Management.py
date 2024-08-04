import matplotlib.pyplot as plt

#Pre-set empty dictionaries
Types = {}
Years = {}

#reads file
file = open("NaturalDisasters.txt", 'r')
for line in file.readlines():
    #splitting the line into a list 
    line = line.strip('\n')
    line = line.split(",")
    #inputting into the dictionaries
    Types[line[0]] = line[1]
    Years[line[0]] = line[2]
file.close()

#dictionary for option 3, 4 and 8
dict_1 = {}

#formula to make dict_1 display the {Type: count}
for w in Types.values():
    if w in dict_1:
        dict_1[w] += 1
    else:
        dict_1[w] = 1

#dictionary for option 7
dict_2 = {}
#loop to make dict_2 display the {Year: count}
for i in Years.values():
    if i in dict_2:
        dict_2[i] += 1
    else: 
        dict_2[i] = 1


#pre-set format
x_1 = "{:5s} {:3d} disasters reported"
x_2 = "{:11s} {:20d} disasters reported"

#Loops for option 9 and 10
sorted_values = sorted(dict_1.values(), reverse = True)

#pre-set empty keys with the same length as the total number (so that indexing would work)
keys = [""]*len(dict_1)
values = [""]*len(dict_1)

#loop to put sorted values and corresponding keys at the same index
for a in dict_1.keys():
    index = sorted_values.index(dict_1[a])
    #In case of repeated counts: resets the spot to zero so the other same values' index would not be affected
    sorted_values[index] = 0
    keys[index] = a
    values[index] = dict_1[a]
                
Menu = """
Program Menu:
1-How many records are there in the data file? Diusplay all complete records in tabular format.
2-How many different types of natural disasters are reported? Print a numbered list of all types.
3-What type of Natural Disaster has been reported the most and how many times?
4-What type of Natural Disaster has been reported the least and how many times?
5-Display all the titles of the natural disasters of a requested type.
6-Display all the titles of the natural disasters of a requested year.
7-List all the years where 2 or more natural disasters were reported.
8-List all types of natural disasters that have occurred more than 3 times.
9-List the top 5 types of natural disasters that were reported.
10-Display a pie chart plot to show the distribution of titles among the top 8 types of natural disasaters.
11-Exit
Enter your option: 
"""
#Pre-set variable to begin the while loop and is not processed
option = 1
while option != 11:
    #User inputs new option and is processed
    option = int(input(Menu))
    #Option 1 code
    if option == 1:
        #Count the total number of records with the dictionary Types' length
        n = len(Types)
        print("There are", n," records in the data file.")
        #format for the strings
        x = "{:38s} {:10s} {:4s}"
        #some labels on top of the list
        print(x.format('Name', 'Type', 'Date'))
        print(x.format('=================', '==========', '===='))
        #printing of the list
        for i in Types.keys():
            print(x.format(i,Types[i],Years[i]))
        
    # option 2 code
    elif option == 2:
        #set valuable for counting
        count_type = 0
        #set empty list to be added the different types, each only once
        list_type = []
        #program for counting the number of different types
        for i in Types.values():
            if i not in list_type:
                list_type.append(i)
                count_type += 1
        print("There are", count_type, "different types of natural disasters reported")
        for a in range(len(list_type)):
            #No need to format because it only involves one string
            print(str(a+1)+".", list_type[a])
    # option 3 code
    elif option == 3:
        #pre-set value
        max = 0
        #loop to determine the largest value in dict_1 and what key it belongs to
        for v in dict_1.keys():
            if dict_1[v] > max:
                max = dict_1[v]
                max_type = v
        print("The most reported natural disaster type is", max_type)
        print("It is repeated", max, "many times")
    
    # option 4 code
    elif option == 4:
        #pre-set value
        min = len(Types)
        #loop to determine the smallest value in dict_1 and what key it belongs to
        for v in dict_1.keys():
            if dict_1[v] < min:
                min = dict_1[v]
                min_type = v
        print("The least reported natural disaster type is", min_type)
        print("It is repeated", min, "many times")
        
    # option 5 code
    elif option == 5:
        #pre-set format
        x = "{:38s} {:4s}"
        #user input
        o5_input = input("Enter a type to display:")
        #Input error checking
        if not(o5_input.lower() in Types.values()):
            print("Error, enter a valid type!")
        else:
            #loop for displaying according to what the input is
            for i in Types.keys():
                if o5_input.lower() == Types[i].lower():
                    print(x.format(i, Years[i]))
    
    # option 6 code
    elif option == 6:
        #user input
        o6_input = input("Enter a year to display:")
        #if there is none reported
        if not(o6_input in Years.values()):
            print("No Natural Disaster reported during this year!")
        else:
            #loop for finding the disaster titles of the inputted year
            for i in Years.keys():
                if o6_input == Years[i]:
                    #Only one string so no need to format
                    print(i)
    # option 7 code
    elif option == 7:
        #to display the years where disaster occured 2 or more times
        for i in dict_2.keys():
            if dict_2[i] >= 2:
                print(x_1.format(i+':',dict_2[i]))
    # option 8 code
    elif option == 8:
        #displaying the types with 3 or more times reported
        for i in dict_1.keys():
            if dict_1[i] >= 3:
                print(x_2.format(i+':',dict_1[i]))
    # option 9 code
    elif option == 9:  
        #pre-set format
        x_o9 = "{:12s} {:3d}"
        #pre-set value for counting to 5
        count = 1
        #loop for printing from index 0 to 4
        for i in range(len(keys)):
            #stopping after 5
            if count > 5:
                break 
            print(x_o9.format(keys[i], values[i]))
            count += 1
    # option 10 code
    elif option == 10:
        #making a pie chart with matplotlib
        fig, ax = plt.subplots()
        #Title
        ax.set_title("Distribution of Top 8 Types of Natural Disasters")
        #Pie
        ax.pie(values[0:8], labels=keys[0:8], autopct='%1.1f%%')
        plt.show()
        
    # option 11 code  
    elif option == 11:
        print("Exiting...")
    
    #Error code for any inputted option thats other than 1-11
    else:
        print("Invalid option. Please choose a valid option.")

