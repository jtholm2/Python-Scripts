import pandas as pd
import time
from selenium import webdriver

browser = webdriver.Firefox()
def scrapeThis(url, num):
    browser.get(url) #opens the website input from the user
    time.sleep(2) #allows time for the elements of the webpage to load
    responsibilities = browser.find_element_by_css_selector('div.jd-info:nth-child(2) > p:nth-child(2)') #finds and stores the element associated with the 'Responsibilities' section
    qualifications = browser.find_element_by_css_selector('div.jd-info:nth-child(3)') #finds and stores the element associated with the 'Qualifications' section
    moreInfo = browser.find_element_by_css_selector('div.jd-info:nth-child(1)') #finds and stores the element associated with the 'More Info' section
    newString = str(moreInfo.text) + " " + str(responsibilities.text) + " " + str(qualifications.text) #creates a new string and concatenates each element stored from the 3 previous lines
    finalString = ""
    for character in newString: #this for loop is iterating through each character in the newString
        if character.isalnum() or character == " ": #this if statement checks if the character is alphanumeric or a space, and if so adds it to the finalString
            finalString += character
    finalString = finalString.lower() #this changes the entire string to lowercase

    words = finalString.split(" ") #this will create a list of each word in the finalString variable
    finalDictionary = {} #establishing a dictionary in order to store word counts

    for word in words: #begins the iteration through the list 'words'
        finalDictionary.setdefault(word, 0) #this command checks if the 'word' is listed in the finalDictionary.keys(). If not, it will create a new key:value pair and set it equal to 0
        finalDictionary[word] = finalDictionary[word] + 1 #this command will take the key and update it's value by 1

    sortedDictionary = {k: v for k, v in sorted(finalDictionary.items(), key=lambda item: item[1], reverse=True)} #this function will sort the values in descending order, so that the words with the highest count are listed first


    df = pd.DataFrame(data=sortedDictionary, index=[0]) #the following three lines allow me to create a new excel file with the new sorted dictionary key:value pairs
    df=(df.T)
    if num == 1:
        with pd.ExcelWriter('job_posting_word_count.xlsx') as writer:
            df.to_excel(writer, sheet_name='Sheet_' + str(num))
    else:
        with pd.ExcelWriter('job_posting_word_count.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name= 'Sheet_' + str(num))

i = 1
while(True):
    print("would you like to scrape, y or n:")
    choice = input()
    if(choice.lower() != 'y'):
        break
    else:
        print("please enter the url you would like to scrape: ")
        url = input()
        scrapeThis(url, i)
        i = i + 1
