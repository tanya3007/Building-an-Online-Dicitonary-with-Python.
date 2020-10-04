#import json module for opening the data file
import simplejson as json
from difflib import get_close_matches
#open data file
data = json.load(open("C:\\Users\\apar\\Desktop\\data.json"))
#creating the function
def getMeaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    # give matching word
    elif len(get_close_matches(w, data.keys())) > 0:
        close_match = get_close_matches(w, data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[close_match]
        elif choice == 'n':
            return "The word doesn't exist."
        else:
            return "Sorry, We didn't understand your entry."
    else:
        return "The word doesn't exist."

ans = "yes"
#create while loop for continue or exit the searching
while (ans == "yes" or ans == "Yes"):

    word = input('Enter word: ')
    #calling the declared function
    meaning = getMeaning(word)
    #printing the meaning of searched word
    if type(meaning) == list:
        for item in meaning:
            print(item)
    else:
        print(meaning)
    #providing yes or no statemnt to continue or exit the loop
    ans = input("yes or Yes for continue to search or if you want to exit press no or No:")


