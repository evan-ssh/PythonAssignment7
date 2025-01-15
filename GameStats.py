def main():
 players = {"Elizabeth":{"Wins":"41","Losses":"22","Ties":"11"},"Jimmy":{"Wins":"41","Losses":"22","Ties":"11"},"Timmy":{"Wins":"41","Losses":"22","Ties":"11"}}
 command = int(input("Enter a command"))
 if command == 1:
  SearchPlayer(players)
 elif command == 2:
    ListPlayers()
def SearchPlayer(players):
 for name,values in players.items():
  enter_name = input("Enter a player to Search for")
  if name == enter_name:
   print(f"{name},{values}")
   
def ListPlayers():
 for i, name in enumerate(sorted(players.keys()))
  print(f"{i}.{name}")
main()