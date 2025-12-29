import random as rn
class Train:
    def __init__(self):
        print("****-MENU-****\n 1.Book\n 2.Check status\n 3.Collect fair details")
        self.Menu=input("ENTER WHAT DO YOU WANT: ")
        if self.Menu.lower() in ("1.book","book",'1'):
            print(f"Confirmed you want to {self.Menu.capitalize()}")
            self.book(input("Enter from-station: ").upper(),input("Enter to-station: ").upper())
            self.get_status()
            self.get_fair_info
        elif self.Menu.lower() in ("2.check status","check status",'2'):
            print(f"Confirmed you want to {self.Menu.capitalize()}")
            print("Checking status:")
            self.get_status()
        elif self.Menu.lower() in ("3.collect fair details","collect fair details",'3'):
            print(f"Confirmed you want to{self.Menu.capitalize()}")
            print("Collecting the fair deails..")
            self.get_fair_info(input("Enter from-station: ").upper(),input("Enter to-station: ").upper())
        else:
            print(f"Something went wrong bro...,Try again..")
    def book(self,from_station,to_station):
        print(f"You are going from {from_station} to {to_station}")
        print("Train details..")
        if (from_station=="DMNJ" and to_station=="BBSR") or (from_station=="BBSR" and to_station=="DMNJ"):
            Trains=["1.hirakhand express","2.Skit's Train"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is: 205 rupees")
            else:
                print("No fair as you are on Skit's Train!!!")
        elif (from_station=="KOAA" and to_station=="PNBE") or (from_station=="PNBE" and to_station=="KOAA"):
            Trains=["1.akal takth express","ara garib rath express"]
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is: 350 rupees")
            else:
                print("fair for the train is: 450 rupees")
        elif (from_station=="DWK" and to_station=="JAM") or (from_station=="JAM" and to_station=="DWK"):
            Trains=["1.ahemdabad vande bharat express","shalimar weekly sf express"]
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is: 700 rupees")
            else:
                print("fair for the train is: 757 rupees")
        elif (from_station=="CSMT" and to_station=="BBSN") or (from_station=="BBSN" and to_station=="CSMT"):
            Trains=["1.konark express","Skit's Train"]
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is:478 rupees")
            else:
                print("No fair as you are on Skit's Train!!!")
        else:
            print("No trains are currently on service in this route.")
    def get_status(self):
        seat=rn.choice(["yes","no"])
        if seat=="yes":
            print("Seats are available")
            choice=input("Confirm by yes or no if you want a ticket: ").lower()
            if choice=="yes":
                print("A seat is booked details sent in login mail...")
            else:
                print("Status was shown..")
        else:
            print("No more tickets for this train..")
    def get_fair_info(self,from_station,to_station):
        print(f"You are going from {from_station} to {to_station}")
        print("Train details..")
        if (from_station=="DMNJ" and to_station=="BBSR") or (from_station=="BBSR" and to_station=="DMNJ"):
            Trains=["1.hirakhand express","2.Skit's Train"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is: 205 rupees")
            else:
                print("No fair as you are on Skit's Train!!!")
        elif (from_station=="KOAA" and to_station=="PNBE") or (from_station=="PNBE" and to_station=="KOAA"):
            Trains=["1.akal takth express","ara garib rath express"]
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is: 350 rupees")
            else:
                print("fair for the train is: 450 rupees")
        elif (from_station=="DWK" and to_station=="JAM") or (from_station=="JAM" and to_station=="DWK"):
            Trains=["1.ahemdabad vande bharat express","shalimar weekly sf express"]
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is: 700 rupees")
            else:
                print("fair for the train is: 757 rupees")
        elif (from_station=="CSMT" and to_station=="BBSN") or (from_station=="BBSN" and to_station=="CSMT"):
            Trains=["1.konark express","Skit's Train"]
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fair for the train is:478 rupees")
            else:
                print("No fair as you are on Skit's Train!!!")
        else:
            print("No trains are currently on service in this route.")
obj=Train()