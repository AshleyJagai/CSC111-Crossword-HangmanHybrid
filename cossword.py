from graphics import *
import random  
from hangman import *
from leaderboard import *
import time

player = input("What is your name? ").lower()
choices= []
choicesleft= ['1','2','3','4','5']
start = time.time()
r = open('Leaderboard.txt', 'r')
l = open('Leaderboard.txt', 'a')
   ###FIRST WORD####
first_word_let_1 = Text((Point(68, 210)), "s")
first_word_let_1.setFill("black")
first_word_let_1.setSize(24)
first_word_let_2 = Text((Point(68, 170)), "n")
first_word_let_2.setFill("black")
first_word_let_2.setSize(24)
first_word_let_3 = Text((Point(68, 125)), "o")
first_word_let_3.setFill("black")
first_word_let_3.setSize(24)
first_word_let_4 = Text((Point(68, 80)), "w")
first_word_let_4.setFill("black")
first_word_let_4.setSize(24)
first_word_let_5 = Text((Point(68, 40)), "f")
first_word_let_5.setFill("black")
first_word_let_5.setSize(24)
first_word_let_6 = Text((Point(68, 0)), "l")
first_word_let_6.setFill("black")
first_word_let_6.setSize(24)
first_word_let_7 = Text((Point(68, -40)), "a")
first_word_let_7.setTextColor("black")
first_word_let_7.setSize(24)
first_word_let_8 = Text((Point(68, -80)), "k")
first_word_let_8.setFill("black")
first_word_let_8.setSize(24)
first_word_let_9 = Text((Point(68, -120)), "e")
first_word_let_9.setFill("black")
first_word_let_9.setSize(24)  
 ###SECOND WORD####
second_word_let_1 = Text((Point(32, 125)), "c")
second_word_let_1.setFill("black")
second_word_let_1.setSize(24)
second_word_let_2 = Text((Point(68, 125)), "o")
second_word_let_2.setFill("black")
second_word_let_2.setSize(24)
second_word_let_3 = Text((Point(115, 125)), "l")
second_word_let_3.setFill("black")
second_word_let_3.setSize(24)
second_word_let_4 = Text((Point(155, 125)), "d")
second_word_let_4.setFill("black")
second_word_let_4.setSize(24)
 ###THIRD WORD####
third_word_let_1 = Text((Point(-98, 45)), "g")
third_word_let_1.setFill("black")
third_word_let_1.setSize(24)
third_word_let_2 = Text((Point(-98, 0)), "l")
third_word_let_2.setFill("black")
third_word_let_2.setSize(24)
third_word_let_3 = Text((Point(-98, -40)), "o")
third_word_let_3.setFill("black")
third_word_let_3.setSize(24)
third_word_let_4 = Text((Point(-98, -80)), "v")
third_word_let_4.setFill("black")
third_word_let_4.setSize(24)
third_word_let_5 = Text((Point(-98, -125)), "e")
third_word_let_5.setFill("black")
third_word_let_5.setSize(24)
third_word_let_6 = Text((Point(-98, -160)), "s")
third_word_let_6.setFill("black")
third_word_let_6.setSize(24)
 ###FOURTH WORD####
fourth_word_let_1 = Text((Point(-135, -40)), "h")
fourth_word_let_1.setFill("black")
fourth_word_let_1.setSize(24)
fourth_word_let_2 = Text((Point(-98, -40)), "o")
fourth_word_let_2.setFill("black")
fourth_word_let_2.setSize(24)
fourth_word_let_3 = Text((Point(-52,-40)), "l")
fourth_word_let_3.setFill("black")
fourth_word_let_3.setSize(24)
fourth_word_let_4 = Text((Point(-15, -40)), "i")
fourth_word_let_4.setFill("black")
fourth_word_let_4.setSize(24)
fourth_word_let_5 = Text((Point(30, -40)), "d")
fourth_word_let_5.setFill("black")
fourth_word_let_5.setSize(24)
fourth_word_let_6 = Text((Point(68, -40)), "a")
fourth_word_let_6.setFill("black")
fourth_word_let_6.setSize(24)
fourth_word_let_7 = Text((Point(115, -40)), "y")
fourth_word_let_7.setFill("black")
fourth_word_let_7.setSize(24)
 ###FIFTH WORD####
fifth_word_let_1 = Text((Point(-175, -125)), "s")
fifth_word_let_1.setFill("black")
fifth_word_let_1.setSize(24)
fifth_word_let_2 = Text((Point(-135, -125)), "l")
fifth_word_let_2.setFill("black")
fifth_word_let_2.setSize(24)
fifth_word_let_3 = Text((Point(-98, -125)), "e")
fifth_word_let_3.setFill("black")
fifth_word_let_3.setSize(24)
fifth_word_let_4 = Text((Point(-52, -125)), "d")
fifth_word_let_4.setFill("black")
fifth_word_let_4.setSize(24)

def crossword_game(win):

   ###DRAWS CROSSWORD####
  cross_bkg = Image(Point(0,0), "img/Winter_crossword.png")
  word_list = ["snowflake", "cold", "gloves", "holiday","sled"]
  cross_bkg.draw(win)
  word_fill_ins(win)
  if not choicesleft:
    end = time.time()      
    newtime = round(end-start,2)
    print("Your total time was: " + str(newtime) + "secs")    
    print (player + ", you got all the words! :)")
    filenew = str(newtime)
    l.write(player)
    l.write("\t")
    l.write(filenew)
    l.write("\n")
    print ("The leaderboard:\n" + r.read())
    l.close()
    return 0
    
      
      #purr
   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
   ###CHOOSE WHICH WORD TO GUESS####
  new = ', '.join(choicesleft)
  inputBox1 = input("Which word would you like to guess?" + " " + new + " or 0 to quit?")  
  if "0" in inputBox1:
    end = time.time()
    newtime = round(end-start,2)
    print("Your total time was: " + str(newtime) + "secs")    
    print (player + ", you got all the words! :)")
    filenew = str(newtime)
    l.write(player)
    l.write("\t")
    l.write(filenew)
    l.write("\n")
    print ("The leaderboard:\n" + r.read())
    l.close()
    return 0
  if validate(inputBox1):
    index = choicesleft.index(inputBox1)
    undrawwords()
    if "1" in inputBox1:
      # undraw_word_fill_ins
      cross_bkg.undraw()
      word = word_list[0]
      choices.append("1")
      choicesleft.pop(index)
      hangman_guess(win, word)
      wordsguessed = []

    elif "2" in inputBox1:
      cross_bkg.undraw()
      word = word_list[1]
      choices.append("2")
      choicesleft.pop(index)
      hangman_guess(win, word)

    elif "3" in inputBox1:
      cross_bkg.undraw()
      word = word_list[2]
      choices.append("3")
      choicesleft.pop(index)
      hangman_guess(win, word)

    elif "4" in inputBox1:
      cross_bkg.undraw()
      word = word_list[3]
      choices.append("4")
      choicesleft.pop(index)
      hangman_guess(win, word)

    elif "5" in inputBox1:
      cross_bkg.undraw()
      word = word_list[4]
      choices.append("5")
      choicesleft.pop(index)
      hangman_guess(win, word)
    elif not choicesleft:
      print ("You got all the choices")
      end = time.time()
      newtime = round(end-start,2)
      print("Your total time was: " + newtime + "secs")    
      print (player + ", you got all the words! :)")
      filenew = str(newtime)
      l.write(player)
      l.write("\t")
      l.write(filenew)
      l.write("\n")
      print ("The leaderboard:\n" + r.read())
      l.close()
      
    else:
      print('Pick one of the words to guess. Restart')
  else:
    cross_bkg.undraw()
    crossword_game(win)

    # if inputBox1 == choices:
  #   print("Try again.")
  #   inputBox1

def validate(inputbx):
  if inputbx in choices:
    print ("Element Exists")
    return False
  if inputbx not in choicesleft:
    print ("sorry Buddy")
    return False  
  return True
  
 ###DRAWS LETTER ON CROSSWORD AFTER ITS GUESSED####

def word_fill_ins(win):
### DRAWS WORD ON SCREEN###
  if "1" in choices: 
    first_word_let_1.draw(win)
    first_word_let_2.draw(win)
    first_word_let_3.draw(win)
    first_word_let_4.draw(win)
    first_word_let_5.draw(win)
    first_word_let_6.draw(win)
    first_word_let_7.draw(win)
    first_word_let_8.draw(win)
    first_word_let_9.draw(win)
  if "2" in choices: 
    second_word_let_1.draw(win)
    second_word_let_2.draw(win)
    second_word_let_3.draw(win)
    second_word_let_4.draw(win)

  if "3" in choices: 
    third_word_let_1.draw(win)
    third_word_let_2.draw(win)
    third_word_let_3.draw(win)
    third_word_let_4.draw(win)
    third_word_let_5.draw(win)
    third_word_let_6.draw(win)

  if "4" in choices: 
    fourth_word_let_1.draw(win)
    fourth_word_let_2.draw(win)
    fourth_word_let_3.draw(win)
    fourth_word_let_4.draw(win)
    fourth_word_let_5.draw(win)
    fourth_word_let_6.draw(win)
    fourth_word_let_7.draw(win)

  if "5" in choices: 
    fifth_word_let_1.draw(win)
    fifth_word_let_2.draw(win)
    fifth_word_let_3.draw(win)
    fifth_word_let_4.draw(win)
  
def undrawwords(): 
  if "1" in choices : 
    first_word_let_1.undraw()
    first_word_let_2.undraw()
    first_word_let_3.undraw()
    first_word_let_4.undraw()
    first_word_let_5.undraw()
    first_word_let_6.undraw()
    first_word_let_7.undraw()
    first_word_let_8.undraw()
    first_word_let_9.undraw()
  if "2" in choices : 
    second_word_let_1.undraw()
    second_word_let_2.undraw()
    second_word_let_3.undraw()
    second_word_let_4.undraw()
  if "3" in choices : 
    third_word_let_1.undraw()
    third_word_let_2.undraw()
    third_word_let_3.undraw()
    third_word_let_4.undraw()
    third_word_let_5.undraw()
    third_word_let_6.undraw()
  if "4" in choices: 
    fourth_word_let_1.undraw()
    fourth_word_let_2.undraw()
    fourth_word_let_3.undraw()
    fourth_word_let_4.undraw()
    fourth_word_let_5.undraw()
    fourth_word_let_6.undraw()
    fourth_word_let_7.undraw()
  if "5" in choices : 
    fifth_word_let_1.undraw()
    fifth_word_let_2.undraw()
    fifth_word_let_3.undraw()
    fifth_word_let_4.undraw()
