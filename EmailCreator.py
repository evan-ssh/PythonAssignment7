import csv
def main():
 contact = OpenEmails()
 print(f"{contact[0]}")

def OpenEmails():
 try:
  contact = []
  with open("contact_emails.csv") as file:
   reader = csv.reader(file)
   for row in reader:
    first_name = row[0].title()
    last_name = row[1].title()
    email = row[2].lower()
    contact.append([first_name,last_name,email])
 except FileNotFoundError as e:
  print(f"Could not find file check directory{e}")
 return contact

main()