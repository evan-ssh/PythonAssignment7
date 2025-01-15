import csv
def main():
 contact = OpenEmails()
 command = int(input("Enter a command"))
 if command == 1:
  CreateEmails(contact)
  
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

def CreateEmails(contact):
 for first_name,last_name,email in contact:
  print(f"To:	     {email}")
  print(f"From:	 noreply@deals.com")
  print(f"Subject: Deals!\n")
  print(f"Hi {first_name},\n")
  print(f"We've got some great deals for you. Check our website!")


main()