# amount of letters each word
# everyone give a letter
# everyone has an amount of changes
# Give output from answers to


import random
import sys


class Hangman:

    def __init__(self):
        self.name_players = []
        self.status_players ={}
        self.display ={}
        self.word_dots = []
        self.hidden = ""
        self.chances_players = []
        self.ladila = []


    def pick_word(self):

        words = ['baby', 'cat', 'dog', 'egg', 'fish', 'goat', 'hat', 'ice', 'jelly', 'kite',
                     'lion', 'monkey', 'nest', 'owl', 'pig', 'queen', 'rabbit', 'sun', 'tree', 'umbrella',
                     'van', 'whale', 'zebra']

        self.hidden = random.choice(words)

        return self.hidden


    def hangman_display(self):
        self.display = {
        'first': """
                 |             
                 |            
                 |            
                 |            
                 |            
                 |            
                _|_
                """,
        'second' : """
                 _________
                 |       |             
                 |           
                 |            
                 |            
                 |            
                 |            
                _|_
                """,
        'third' : """
                 _________
                 |       |             
                 |       O   
                 |            
                 |            
                 |            
                 |            
                _|_
                """,
        'fourth' :  """
                 _________
                 |       |             
                 |       O   
                 |      \|/      
                 |            
                 |            
                 |            
                _|_
                """,

        'fifth' : """
                 _________
                 |       |             
                 |       O   
                 |      \|/      
                 |       |     
                 |            
                 |            
                _|_
                """,
        'sixth' : """
                 _________
                 |       |             
                 |       O
                 |     =====   
                 |      \|/      
                 |       |    
                 |      / \     
                 |            
                _|_
                """
        }


    def players(self):

        list_123 = ['FIRST', 'SECOND', 'THIRD', 'FORTH', 'FIFTH', 'SIXTH']
        print("\n\nWELCOME TO THE HANGMANSHOW!\n")
        self.name_players = []
        self.status_players = {}

        while True:
            amount_players = input("AMOUNT PLAYERS:\n")

            try:
                amount_players = int(amount_players)
                break

            except ValueError:
                print("NUMBER NO LETTER!")


        for a, b in zip(range(amount_players), list_123):
            self.chances_players = [1, 2, 3, 4, 5, 6]
            lala = input(f"\n{b} PLAYER NAME:\n")
            self.name_players.append(lala)

        status_players = {item: self.chances_players for item in self.name_players}

        return status_players



    def game(self, hidden, status_players):
        positions = []
        self.ladila = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
        self.chances_doll = [1, 2, 3, 4, 5, 6]



        word_dots = ['.' for i in self.hidden];



        while True:
            for name, chances in status_players.items():

                modified_dots = " ".join(" ." for i in word_dots);
                print(f"\n\n{modified_dots}")

                letter = input(f"\n{name} GUESS A LETTER/WORD: ")
                modified_dots = " ".join(" ." for i in word_dots);

                if len(letter) >1:

                    if letter == hidden:
                        print(f"YOU WON!")
                        break

                    else:
                        status_players[name] = status_players[name][:-1]
                        display_chance = len(status_players[name])
                        print(f"WRONG! [{display_chance}/6]")

                        for key, value in status_players.items():
                            print(key, value)


                        continue
                else:

                        if letter in self.hidden:
                            print(f"\n\n      GOOD!")

                            positions = (i for i in range(len(hidden)) if hidden[i] == letter)

                            [word_dots.__setitem__(i, letter) for i in positions];

                            modified_dots = " ".join(i for i in word_dots);
                            print(modified_dots)
                            continue


                        else:

                            status_players[name] = status_players[name][:-1]
                            self.chances_doll.pop()
                            display_chance = len(status_players[name])



                            if self.ladila[0] in self.display:
                                print(f"\n{self.display[self.ladila[0]]}")
                                self.ladila.pop(0)

                            print("WRONG!\n")
                            print(f"{name.capitalize()} TOTAL CHANCES: {display_chance}/6")
                            print(f"HANGMAN TOTAL CHANCES: {len(self.chances_doll)}/6\n")

                            if len(self.ladila) <= 0:
                                 print(f"YOU BOTH LOST, LOSERS!")
                                 print(f"WORD WAS: {hidden.capitalize()}")
                                 sys.exit()




                            continue











    # enter how many persons play > do in the call
    # maybe also words > funny

    #if given letter is in word:
     #   print("this letter is in it:")
     #   print(#the letter on the word, rest with dots)
        #remove chances of the person
        #input > create player > name
        #create changes for each player.
        #explain game rules

    #1."""" "hello who is play"
     #   2. enter names
      #  3. explain
       # 4. system picks word and prints dots
        #5 first player can input letter pick
        #6. system checks if letter is in the word
       # 7. yes > print ("yeey!"), show the letter displayed
      #  8. no > print('merp'), lower the chances print(amount of chances))
     #   9. display which numbers were given already
     #   10. next person.
    #    11 display hangman"""
