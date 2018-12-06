'''
Write a program that will read the file, 'red-headed-league.txt', count the frequency of the words and store it as a csv file.
Create a class called WordCounter with the following methods.def __init__(self,filename) where filename is the name of the text file, 'red-headed-league.txt'. This function should
read the text file
def removepunctuation(self) must remove all the punctuations and leave only alphabets and numbers in each word
def findcount(self) must count the frequency of each word and store it in a instance variable called countdict
def writecountfile(self,csvfilename) writes the content of the countdict variable to a csv file with two columns.
The first column is the word and second column is the count.
Create an instance of the class and call appropriate method and store the result in a csv file. Printout the five most popular words.
NOTE: DO NOT USE THE COUNTER DATA STRUCTURE IN COLLECTIONS MODULE.
'''

import string


class WordCounter(object):
    def __init__(self, filename):
        file = open(filename, 'r')
        self.text = file.read()
        file.close()

    def removepunctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)

    wordDictionary = {}

    def findcount(self):
        self.wordList = self.text.split(" ")
        self.wordDictionary = {x: self.wordList.count(x) for x in set(self.wordList)}

    def writecountfile(self, csvfilename):
        with open(csvfilename, 'w') as csv_file:
            columntitlerow = "word,count\n"
            csv_file.write(columntitlerow)
            for key, value in self.wordDictionary.items():
                row = key + "," + str(value) + "\n"
                csv_file.write(row)


w = WordCounter("C:/Users/omer/Downloads/red-headed-league.txt")
w.removepunctuation()
w.findcount()
w.writecountfile("C:/Users/omer/Downloads/red-headed-league.csv")
sorted_wordCount = sorted(w.wordDictionary.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_wordCount[0:5])
