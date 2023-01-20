solution = "ACCOMPLI"
tentatives = 2
affichage = ""
lettres_trouvees = ""

 

for l in solution:
  affichage = affichage + "_ "

 

print(">> Bienvenue dans le jeu du pendu <<")

 

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].upper()

 

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien !")
  else:
    tentatives = tentatives - 1
    print("-> Nope\n")
    if tentatives==1:
        print("fausse Tentative , il vous reste une autre ")
    if tentatives==0:
        print("fausse Tentative , jeu perdu \n")

 

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

 

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break

print("\n    * Fin de la partie *    ")
