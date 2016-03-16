#
# Jeff Kropelnicki
# 
# Homework
 
import random

def random_grid(object):
    '''This is a function that can be used to create a grid of rumdom numbers. The function asks for the 
    number of rows and columns the user would like. It then asks for the range of minimum and maximum numbers
    for the ranbom numbers in the grid.
    This fuctions uses the random from the python stardard library: this generators pseudo-random number 
    based on a range.'''
    
    grid = [] #Define grid as a list
    
    #Asks the user to define the parameters of the grid
    num_rows = raw_input("How many raws would you like in your grid? ")
    num_columns = raw_input("How many columns would you like in you grid? ")
    min_range = raw_input("What is the minimum number you would like in your grid? ")
    max_range = raw_input("what is the maximum number you would like in your grid? ")
    
    #Set the rows and columns to the user specified choose
    for row in range(int(num_rows)):
        grid.append([])
        for column in range(int(num_columns)):
            #random.randint returns a random integer
            grid[row].append(random.randint((int(min_range)),(int(max_range))))         
        
    
    ajax = "" # set ajax to a string 
    
    #Converts the above grid from a list to a string.
    for row in grid:
        ajax += (' '.join([str(x) for x in row])) + "\n" 
    print ajax
    
    #Writes the ajax top a user given .txt file
    with open(r"/Users/jeffkropelnicki/Desktop/text.txt", 'w') as text_file:
        text_file.write(ajax)      
        