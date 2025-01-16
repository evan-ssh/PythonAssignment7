def main():
 players = {"Elizabeth":{"Wins":"41","Losses":"22","Ties":"11"},"Jimmy":{"Wins":"41","Losses":"22","Ties":"11"},"Timmy":{"Wins":"41","Losses":"22","Ties":"11"}}
 while True:
  try:
   command = int(input("Enter a command"))
   if command < 1 or command > 4:
    print("Enter a valid command")
   if command == 1:
    SearchPlayer(players)
   elif command == 2:
    ListPlayers(players)
   elif command == 3:
    AddPlayer(players)
   elif command == 4:
    return False
  except ValueError:
   print("Enter a valid command")
def DisplayMenu():
   print("COMMAND MENU")
   print("1 - Search a Player")
   print("2 - List Players")
   print("3 - Add a player")
   print("4 - Exit Program")
def SearchPlayer(players):
 enter_name = input("Enter a player to Search for")
 for name,values in players.items():
  if enter_name == name:
   print(f"{enter_name},{values['Wins']}\nLosses:{values['Losses']}\n{values['Ties']}")
   break
 else:
  print("Player not in stats list")
def ListPlayers(players):
 for i, name in enumerate(sorted(players.keys()),start=1):
  print(f"{i}.{name}")

def AddPlayer(players):
   name = input("Enter a name for the new player")
   wins = input("Enter the wins")
   losses = input("Enter the losses")
   ties =  input("Enter the ties")
   players[name] = {"Wins":wins,"Losses":losses,"Ties":ties}
   print(f"Added stats for {name}")

main()