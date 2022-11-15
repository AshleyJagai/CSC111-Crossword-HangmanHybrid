
#        Name: <Paloma Huntingto, Ashlely Jagai>
# Course Info: CSC111 - Fall 2021
# Description: Submission for Final Progect
#        Date: <11/04/2021>
#--------------------------------------------------------------
from graphics import * 
from crossword import *
from hangman import *

class Buttons:
  def __init__(self, x=0, y=0, x2=0, y2=0):
    self.x = x
    self.y = y
    self.x2 = x2
    self.y2 = y2
 
    self.rec = Rectangle(Point(x, y),Point(x2,y2))
    self.rec.setFill("white")
    self.rec.setOutline("white")

    
  def draw_button(self, win):
    self.rec.draw(win)

  def undraw_button(self, win):
    self.rec.undraw()
    



def title_page(width, height, win):

###CROSSWORD###
  txtCrossword = Text(Point(-(width/4),(height/4)),'Crossword')
  txtCrossword.setFill('black')
  txtCrossword.setSize(24)
  
###HANGMAN###
  txtHangman = Text(Point((width/4),(height/4)),'Hangman')
  txtHangman.setFill('black')
  txtHangman.setSize(24)

###HYBRID###
  txtHybrid = Text(Point(-(0),(height/7)),'Hybrid')
  txtHybrid.setFill('black')
  txtHybrid.setSize(24)

  txtAdvance = Text(Point(-(0), (height/180)), 'press h for how to play or s for start')
  txtAdvance.setFill('black')
  txtAdvance.setSize(15)
  
 ###DRAWS###
  txtCrossword.draw(win)
  txtHangman.draw(win)
  txtHybrid.draw(win)
  txtAdvance.draw(win)
  
  ###HANGMAN IMAGE####
  hangmanImage = Image(Point(5,-180), "Hangman.png")
  hangmanImage.draw(win)


  ###INSTRUCTIONS####
  buttoninstruction = Buttons(-210,-180, 210,200)
  instructionstext = 'HOW TO PLAY: Solve the CrossWord puzzle by choosing a secret word to guess. After chosing one of the secret words; the player has to guess what it is one letter at a time by pressing on the letter on their keyboard. If the letter occurs in the word, the computer fills in the blanks with that letter in the right places. Whenever the players guess a letter that is not in the secret word they get a strike that brings them closer to losing. To show this, body parts are drawn in adding a new part to the drawing with every wrong answer. HOW TO WIN: The player wins when they complete the crossword puzzle.'
  instructionsCharacter = instructionstext
  instructionsCharacter = instructionsCharacter.split()
  line0 = (" ").join(instructionsCharacter[:3])
  line1 = (" ").join(instructionsCharacter[3:10])
  line2 = (" ").join(instructionsCharacter[10:18])
  line3 = (" ").join(instructionsCharacter[18:26])
  line4 = (" ").join(instructionsCharacter[26:37])
  line5 = (" ").join(instructionsCharacter[37:45])
  line6 = (" ").join(instructionsCharacter[45:54])
  line7 = (" ").join(instructionsCharacter[54:62])
  line8 = (" ").join(instructionsCharacter[62:70])
  line9 = (" ").join(instructionsCharacter[70:80])
  line10 = (" ").join(instructionsCharacter[80:88])
  line11 = (" ").join(instructionsCharacter[88:98])
  line12 = (" ").join(instructionsCharacter[98:104])
  line13 = (" ").join(instructionsCharacter[104:107])
  line14 = (" ").join(instructionsCharacter[107:114])
  line15 = (" ").join(instructionsCharacter[114:116])
  instructions13 = Text((Point(-5, 160)), line0)
  instructions1 = Text((Point(0, 135)), line1)
  instructions2 = Text((Point(0, 115)), line2)
  instructions3 = Text((Point(0, 95)), line3)
  instructions4 = Text((Point(0, 75)), line4)
  instructions5 = Text((Point(0, 55)), line5)
  instructions6 = Text((Point(0, 35)), line6)
  instructions7 = Text((Point(0, 15)), line7)
  instructions8 = Text((Point(0, -5)), line8)
  instructions9 = Text((Point(0, -25)), line9)
  instructions10 = Text((Point(0, -45)), line10)
  instructions11 = Text((Point(0, -65)), line11)
  instructions12 = Text((Point(0, -85)), line12)
  instructions14 = Text((Point(0, -120)), line13)
  instructions15 = Text((Point(-5, -145)), line14)
  instructions16 = Text((Point(0, -165)), line15)


  ###START####
  inputBox = input("Button? (h for How To Play, s for Start) ").lower()

  if inputBox == "h":
    buttoninstruction.draw_button(win)
    instructions13.draw(win)
    instructions1.draw(win)
    instructions2.draw(win)
    instructions3.draw(win)
    instructions4.draw(win)
    instructions5.draw(win)
    instructions6.draw(win)
    instructions7.draw(win)
    instructions8.draw(win)
    instructions9.draw(win)
    instructions10.draw(win)
    instructions11.draw(win)
    instructions12.draw(win)
    instructions14.draw(win)
    instructions15.draw(win)
    instructions16.draw(win)
    instructions1.setTextColor("black")
    instructions2.setTextColor("black")
    instructions3.setTextColor("black")
    instructions4.setTextColor("black")
    instructions5.setTextColor("black")
    instructions6.setTextColor("black")
    instructions7.setTextColor("black")
    instructions8.setTextColor("black")
    instructions9.setTextColor("black")
    instructions10.setTextColor("black")
    instructions11.setTextColor("black")
    instructions12.setTextColor("black")
    instructions13.setTextColor("black")
    instructions14.setTextColor("black")
    instructions15.setTextColor("black")
    instructions16.setTextColor("black")
    inputBox = input("If ready to play press s for start ").lower()

    if inputBox == "s":
      txtCrossword.undraw()
      txtHangman.undraw()
      txtHybrid.undraw()
      txtAdvance.undraw()
      hangmanImage.undraw()
      instructions1.undraw()
      instructions2.undraw()
      instructions3.undraw()
      instructions4.undraw()
      instructions5.undraw()
      instructions6.undraw()
      instructions7.undraw()
      instructions8.undraw()
      instructions9.undraw()
      instructions10.undraw()
      instructions11.undraw()
      instructions12.undraw()
      instructions13.undraw()
      instructions14.undraw()
      instructions15.undraw()
      instructions16.undraw()
      buttoninstruction.undraw_button(win)
      crossword_game(win)

  elif inputBox == "s": 
    txtCrossword.undraw()
    txtHangman.undraw()
    txtHybrid.undraw()
    txtAdvance.undraw()
    hangmanImage.undraw()
    instructions1.undraw()
    instructions2.undraw()
    instructions3.undraw()
    instructions3.undraw()
    instructions4.undraw()
    instructions5.undraw()
    instructions6.undraw()
    instructions7.undraw()
    instructions8.undraw()
    instructions9.undraw()
    instructions10.undraw()
    instructions11.undraw()
    instructions12.undraw()
    instructions13.undraw()  
    instructions14.undraw()
    instructions15.undraw()
    instructions16.undraw()
    buttoninstruction.undraw_button(win)
    crossword_game(win)

  else:
    print("Please run again and type a given option (s or h)")

  
def main():

  ###################START PAGE WIN###################
  width = 500
  height = 500
  win = GraphWin('Crossword-Hangman Hybrid', width, height)
  bg = Image(Point(width/150, height/550), "BBG.gif")
  bg.draw(win)


  win.setCoords(-(width/2), -(height/2), (width/2), (height/2))
  title_page(width, height, win)




if __name__ =="__main__":
  main()
