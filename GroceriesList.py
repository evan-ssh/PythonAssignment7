def main():
 groceries = OpenGroceries()
 print(groceries)

def OpenGroceries():
 try:
  groceries = []
  with open("groceries.txt",newline='') as file:
   for row in file:
    print(row)
 except FileNotFoundError as e:
  print(f"File wasn't found check directory{e}")
 return groceries