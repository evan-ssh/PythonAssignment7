def main():
 groceries = OpenGroceries()
 print(groceries)

def OpenGroceries():
 try:
  groceries = []
  with open("groceries.txt",newline='') as file:
   for row in file:
    row = row.strip().replace("<h1>","").replace("<h1>","").replace("<h1>","").replace("</h1>","").replace("<ul>","").replace("<li>","").replace("</li>","").replace("</ul>","")
    if row:
     groceries.append(row)
 except FileNotFoundError as e:
  print(f"File wasn't found check directory{e}")
 return groceries

main()