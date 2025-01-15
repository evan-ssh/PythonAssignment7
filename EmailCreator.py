import csv
def main():
 while True:
  contact = OpenEmails()
  try:
   command = int(input("Enter a command"))
   if command == 1:
    CreateEmails(contact)
   elif command == 2:
    ListContacts(contact)
   elif command == 3:
    AddEmails(contact)
  except ValueError:
   print("Enter a command")

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

def SaveEmails(contact):
 try:
  with open("contacts_emails.csv","w",newline='') as file:
   writer = csv.writer(file)
   writer = writer.writerows(contact)
 except PermissionError:
  print("User does not have permissions to save emails")
 except Exception as e:
  print(f"An error occured while saving to file{e}")
  
def CreateEmails(contact):
 while True:
  print(f"{'Email Creator':>25}")
  reps_name = input("Enter name of Representative")
  if not reps_name:
   print("Cannot Continue Without Reps Name")
   continue
  for first_name,last_name,email in contact:
   print("===================================")
   print(f"To: {email}")
   print(f"From: noreply@deals.com")
   print(f"Subject: Deals!\n")
   print(f"Hi {first_name},\n")
   print(f"We've got some great deals for you.\n Check our website!")
   print(f"~{reps_name}")
   print("===================================")
  print(f"{'<===Emails Sent===>':25}")
  break
 
def ListContacts(contact):
 for i, (name,last_name,email) in enumerate(contact):
  print(f"{i}. Name:{name} LastName:{last_name} Email:{email}")

def AddEmails(contact):
 first_name = input("Enter First Name:")
 last_name = input("Enter a last name")
 email = input("Enter an Email")
 contact.append([first_name,last_name,email])
 SaveEmails(contact)
main()