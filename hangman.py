from graphics import *
import crossword
from main import *
from leaderboard import *
import time

 ###DRAWS HANDMNAD STAND####
class Structure:
  def __init__(self, win, position):
    self.base = None
    self.vertical = None
    self.top = None
    self.down = None
    self.make_structure(position)
  
  def make_structure(self, position):
    self.base = Rectangle(Point(-100,-100), Point(100,-90))
    self.base.setFill("black")

    self.vertical = Rectangle(Point(100,-90), Point(90,120))
    self.vertical.setFill("black")

    self.top = Rectangle(Point(90,120), Point(0,110))
    self.top.setFill("black")

    self.down = Rectangle(Point(-10,120), Point(0,100))
    self.down.setFill("black")
  
  def draw_structure(self, win):
    self.base.draw(win)
    self.vertical.draw(win)
    self.top.draw(win)
    self.down.draw(win)
  
  def undraw_structure(self):
    self.base.undraw()
    self.vertical.undraw()
    self.top.undraw()
    self.down.undraw() 


 ###DRAWS HANGMAN BODY####
class Hangman_Body:
  def __init__(self, win, position):
    self.head = None
    self.body = None
    self.leftArm = None
    self.rightArm = None
    self.leftLeg = None
    self.rightLeg = None
    self.make_head(position)
    self.make_body(position)
    self.make_left_arm(position)
    self.make_right_arm(position)
    self.make_left_leg(position)
    self.make_right_leg(position)
    
  def make_head(self,position):
    self.head = Circle(Point(-5,80), 20)
    self.head.setOutline("black")
    
  def make_body(self,position):
    self.body = Line(Point(-6,0), Point(-6,60))
    self.body.setFill("black")
    
  def make_left_arm(self,position):
    self.left_arm = Line(Point(-6,30), Point(-40, 50))
    self.left_arm.setFill("black")
    
  def make_right_arm(self,position):
    self.right_arm = Line(Point(-6,30), Point(40, 50))
    self.right_arm.setFill("black")
    
  def make_left_leg(self,position):
    self.left_leg = Line(Point(-30, -45), Point(-6,0))
    self.left_leg.setFill("black")

  def make_right_leg(self,position):
    self.right_leg = Line(Point(30, -45), Point(-6,0))
    self.right_leg.setFill("black")
  
  def draw_head(self, win):
    self.head.draw(win)
    
  def draw_body(self, win):
    self.body.draw(win)
    
  def draw_left_arm(self, win):
    self.left_arm.draw(win)

  def draw_right_arm(self, win):
    self.right_arm.draw(win)
    
  def draw_left_leg(self, win):
    self.left_leg.draw(win)
    
  def draw_right_leg(self, win):
    self.right_leg.draw(win)
    
  def undraw_body(self):
    self.head.undraw()
    self.body.undraw()
    self.left_leg.undraw()
    self.right_leg.undraw()
    self.right_arm.undraw()
    self.left_arm.undraw()


 ###REpLACES LETTER GUESSED IN LIST####
def replace_letter(win,word,guess,space_list,old_line):
  old_line.undraw()
  x = word.find(guess)
  space_list[x] = guess
  letterline = Text((Point(0,-160)), space_list)
  letterline.setSize(24)
  letterline.draw(win)
  return letterline

 ###RESTARTS HANDMAN GAME####
def restart_hangman(win,letterline, spaceline, old_line):
  letterline.undraw()
  spaceline.undraw()
  old_line.undraw()
  hb.undraw_body()
  st.undraw_structure()
  space_list = [] 
  crossword.crossword_game(win)
  

 ###GUESS LETTER LOGIC####
def hangman_guess(win, word):
  global st
  st = Structure(win, Point(0,0))
  global hb
  hb = Hangman_Body(win, Point(0,0))
  lost_guess = 0
  win_guess = 0
  num_letters = len(word)
  space_list = []
  guess_list = []
  st.draw_structure(win)
  for num in range(num_letters):
    space_list.append("_")
  spaceline = Text((Point(0, -160)), space_list)
  spaceline.setSize(24)
  spaceline.draw(win)
  old_line = spaceline
  
   ###IF WORD IS NOT GUESSED, IT CONTIUES TO ASK FOR A LETTER####
  while lost_guess < 6 or win_guess < num_letters:
    guess = input("guess a letter:").lower().strip()[0]
  
    if guess in word and guess not in guess_list: 
      num_letters = len(word)
      win_guess +=1
      letterline = Text((Point(0,-160)), space_list)
      guess_list.append(guess)
      old_line = replace_letter(win,word,guess,space_list,old_line)
      print("Great, Now guess another letter")
      if win_guess == num_letters:
        print("*yay! you guessed the word!*")
        restart_hangman(win,letterline, spaceline, old_line)
        break
    else:
      guess_list.append(guess)
      lost_guess +=1
      if lost_guess == 1:
        print('Sorry try again!')
        hb.draw_head(win) 
      elif lost_guess ==2:
        print('Sorry try again!')
        hb.draw_body(win) 
      elif lost_guess== 3:
        print('Sorry try again!')
        hb.draw_left_leg(win) 
      elif lost_guess ==4:
        print('Sorry try again!')
        hb.draw_right_leg(win) 
      elif lost_guess ==5:
        print('Sorry try again!')
        hb.draw_right_arm(win) 
      elif lost_guess == 6:
        hb.draw_left_arm(win)
        print("You are all out of guesses :(")
        print("*taking you back to the crossword*")
        time.sleep(.5)
        print("*you'll see what the word was on the crossword*")
        time.sleep(2)
        restart_hangman(win,letterline,spaceline,old_line)
        crossword.crossword_game(win)

        break
