import random
def jeu_de_devinettes():
   the_number = random.randint(1, 100)
   guess = 0
   essaie = 0
   jouer_encore = ""

   while guess != the_number:
       guess = int(input("Entrez un nombre svp : "))
       if guess > the_number:
           print("Plus petit")
           essaie += 1

       elif guess < the_number:
           print("Plus grand")
           essaie += 1
       else:
           print('Bravo! Le nombre etait', the_number, ". Vous avez reussit en ",essaie,"essaies")
           jouer_encore = input("Voulez-vous rejouer? O ou N : ").lower()

       if jouer_encore == "n":
           break
       elif jouer_encore == "o":
           jeu_de_devinettes()


jeu_de_devinettes()
