def main():
 players = {"Elizabeth":{"Wins":"41","Losses":"22","Ties":"11"},"Jimmy":{"Wins":"41","Losses":"22","Ties":"11"},"Timmy":{"Wins":"41","Losses":"22","Ties":"11"}}
 command = int(input("Enter a command"))
 if command == 1:
  SearchPlayer(players)
 elif command == 2:
    ListPlayers(players)
 elif command == 3:
   AddPlayer(players)
def SearchPlayer(players):
 for name,values in players.items():
  enter_name = input("Enter a player to Search for")
  if name == enter_name:
   print(f"{name},{values}")
   
def ListPlayers(players):
 for i, name in enumerate(sorted(players.keys()),start=1):
  print(f"{i}.{name}")

def AddPlayer(players):
   name = input("Enter a name for the new player")
   wins = input("Enter the wins")
   losses = input("Enter the losses")
   ties =  input("Enter the ties")
   players[name] = [wins,losses,ties]
   print(f"Added stats for {name}")
   ListPlayers(players)
main()