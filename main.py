#Author:  Juan Roldan
#Title: Interactive Story

import csv
import time

#Function to get user input
def getUserInput():
    formatter1 = "%23s%13s"
    formatter2 = "%23s%12s"
    print('****** Text Adventure Game v1.0******')
    print('*                                   *')
    print(('*' + formatter1)%("1 - New Game","*"))
    print(('* ' + formatter2)%("2 - Load Game","*"))
    print(('* ' + formatter2)%("3 - Quit Game","*"))
    print('*                                   *')
    print('*************************************')

    validated = False
    
    while(validated == False):
        userInput = input(">")
        #if digit between 1 and 3
        if(userInput.isdigit() and (int(userInput) <= 3) and (int(userInput)>=1)):
            validated=True
            return userInput
        else:
            print("Plese enter a number between 1 and 3")
            validated = False

#Function to get story option
def getStoryOption():
    validated = False
    while(validated == False):
        userInput = input(">")
        #if digit between 1 and 3
        if(userInput.isdigit() and (int(userInput) <= 3) and (int(userInput)>=1)):
            validated=True
            return userInput
        else:
            print("Plese enter a number between 1 and 3")
            validated = False


            
#function to output story line according to option chosen by user
def outputStoryLine(currentStoryLine,storyData):
    currentStoryLine = int(currentStoryLine)
    print("\n" + storyData[currentStoryLine][0])
    print("What do you want to do")
    print("1 - " + storyData[currentStoryLine][1])
    print("2 - " + storyData[currentStoryLine][2])
    print("3 - Save Game" + "\n")

# In case user wants to play new game or load game
# currentStoryLine argument: is the story line that will be outputed, either for the first time the program runs or because of a load
def newGame(currentStoryLine):
    #read story file
    infile = open("story.csv","r")
    csvReader = csv.reader(infile)

    #store as 2d list
    storyData = []
    for row in csvReader:
        storyData.append(row)
    
    #call story line for the first time or loaded one
    outputStoryLine(currentStoryLine,storyData)

    stopStory = False

    #stop if story ends
    while(stopStory == False):
        #get story option from user
        stroryOption = getStoryOption()
        #if first option is chosen
        if(int(stroryOption) == 1):
            currentStoryLine = int(storyData[currentStoryLine][3]) - 1
            if(storyData[currentStoryLine][3] == ''):
                stopStory = True
                print(storyData[currentStoryLine][0] + '\n')
                time.sleep(2)
            else:
                outputStoryLine(currentStoryLine,storyData)
        #if second option is chosen
        elif(int(stroryOption) == 2):
            currentStoryLine = int(storyData[currentStoryLine][4]) - 1
            if(storyData[currentStoryLine][4] == ''):
                stopStory = True
                print(storyData[currentStoryLine][0] + '\n')
                time.sleep(2)
            else:
                outputStoryLine(currentStoryLine,storyData)
        #if save option
        else:
            saveGame(currentStoryLine)
            outputStoryLine(currentStoryLine,storyData)
            

#function that loads current story line from txt file
#returns string with the number of the storyLine
def getSavedStoryLine():
    infile = open("storyLine.txt","r")
    line = infile.readline()
    infile.close()
    return line

#Function to determine if file exits
#Return True if exists, false if it does not exist
def fileExits():
    try:
        infile = open("storyLine.txt","r")
        infile.close()
        return True
    except:
        return False

#save story line game on a txt file
def saveGame(currentStoryLine):
    outfile = open("storyLine.txt","w")
    outfile.write(str(currentStoryLine))
    outfile.close()

    print(">>>Game Saved")

#Main function
def main():
    
    flag = True
    while(flag==True):
        option=getUserInput()
        #newGame
        if(option=='1'):
            #call new game function with current story line at 0
            newGame(0)
        #Load Game
        elif(option == '2'):
            if(fileExits()):
                #lookup saved story line
                currentStoryLine = getSavedStoryLine()
                #load game starting at saved story line
                newGame(int(currentStoryLine))
            else:
                print("File does not exist, new game will begin..."+ "\n")
                time.sleep(1)
                newGame(0)
        else:
            print("Quitting Game...")
            return
main()