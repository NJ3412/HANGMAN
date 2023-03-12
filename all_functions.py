# amount of letters each word
# everyone give a letter
# everyone has an amount of changes
# Give output from answers to


import random

class Hangman:

    def __init__(self):
        self.name_players = []
        self.status_players ={}
        self.word_dots = []
        self.hidden = None
        self.chances_players = []


    def pick_word(self):
        words = ['baba']
        self.hidden = random.choice(words)
        #weghalen 1
        print(self.hidden)
        return self.hidden

    def players(self):

        list_123 = ['first', 'second', 'third', 'forth', 'fifth', 'sixt']
        print("welcome to the big Hangmanshow!")
        self.name_players = []
        self.status_players = {}

        while True:
            amount_players = input("amount players playing: ")

            try:
                amount_players = int(amount_players)
                break

            except ValueError:
                print("sorry you didn't fill in a number, please try again")


        for a, b in zip(range(amount_players), list_123):
            self.chances_players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            lala = input(f"What is the {b} name of the player?\n")
            self.name_players.append(lala)

        print(self.name_players)

        status_players = {item: self.chances_players for item in self.name_players}

        for key, value in status_players.items():
            print(key, value)


        return status_players



    def game(self, hidden, status_players):
        positions = []

        print(f"Let's play the game "+", ".join(status_players.keys()) + ".")
        # add 'and' for 2 or more players


        word_dots = ['.' for i in self.hidden];
        print(word_dots)


        modified_dots = " ".join(" ." for i in word_dots);
        print(modified_dots)


        for name, chances in status_players.items():

            letter = input(f"{name} guess a letter or the word:\n")

            if len(letter) >1:
                print("let me see if you guess the word right..")

                if letter == hidden:
                    print(f"YEAH the word is {hidden}")

                else:
                    status_players[name] = status_players[name][:-3]
                    display_chance = len(status_players[name])
                    print(f"wrong guess, you've lost 3 chances [{display_chance}/10]")

                    for key, value in status_players.items():
                        print(key, value)


                    continue
            else:

                    if letter in self.hidden:
                        print(f"Yes! letter {letter} is in the hidden word ")

                        positions = (i for i in range(len(hidden)) if hidden[i] == letter)
                        print(positions)

                        [word_dots.__setitem__(i, letter) for i in positions];
                        print(word_dots)

                        modified_dots = " ".join(i for i in word_dots);
                        print(modified_dots
                        continue


                    else:
                        print("n")











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
