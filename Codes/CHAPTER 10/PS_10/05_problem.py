import random as rn
class Train:
    def book(self,from_station,to_station):
        print(f"You are going from {from_station} to {to_station}")
        print("Train details..")
        if (from_station=="DMNJ" and to_station=="BBSR") or (from_station=="BBSR" and to_station=="DMNJ"):
            Trains=["1.hirakhand express","2.Skit's Train"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
        elif (from_station=="KOAA" and to_station=="PNBE") or (from_station=="PNBE" and to_station=="KOAA"):
            Trains=["1.akal takth express","ara garib rath express"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
        elif (from_station=="DWK" and to_station=="JAM") or (from_station=="JAM" and to_station=="DWK"):
            Trains=["1.ahemdabad vande bharat express","shalimar weekly sf express"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
        elif (from_station=="CSMT" and to_station=="BBSN") or (from_station=="BBSN" and to_station=="CSMT"):
            Trains=["1.konark express","Skit's Train"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
        else:
            print("No trains are currently on service in this route.")
        return train
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
        return seat
    def get_fare_info(self,from_station,to_station):
        print(f"You are going from {from_station} to {to_station}")
        print("Train details..")
        if (from_station=="DMNJ" and to_station=="BBSR") or (from_station=="BBSR" and to_station=="DMNJ"):
            Trains=["1.hirakhand express","2.Skit's Train"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fare for the train is: 205 rupees")
            else:
                print("No fare as you are on Skit's Train!!!")
        elif (from_station=="KOAA" and to_station=="PNBE") or (from_station=="PNBE" and to_station=="KOAA"):
            Trains=["1.akal takth express","ara garib rath express"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fare for the train is: 350 rupees")
            else:
                print("fare for the train is: 450 rupees")
        elif (from_station=="DWK" and to_station=="JAM") or (from_station=="JAM" and to_station=="DWK"):
            Trains=["1.ahemdabad vande bharat express","shalimar weekly sf express"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fare for the train is: 700 rupees")
            else:
                print("fare for the train is: 757 rupees")
        elif (from_station=="CSMT" and to_station=="BBSN") or (from_station=="BBSN" and to_station=="CSMT"):
            Trains=["1.konark express","Skit's Train"]
            print(Trains)
            train=input("Choose any one train...").lower()
            print(f"You choosed {train} to travel")
            if train==Trains[0]:
                print("fare for the train is:478 rupees")
            else:
                print("No fare as you are on Skit's Train!!!")
        else:
            print("No trains are currently on service in this route.")
    def __init__(self):
        print("****-MENU-****\n 1.Book\n 2.Check status\n 3.Collect fare details")
        self.Menu=input("ENTER WHAT DO YOU WANT: ")
        if self.Menu.lower() in ("1.book","book",'1'):
            print(f"Confirmed you want to {self.Menu.capitalize()}")
            self.book(from_station=input("Enter from-station: ").upper(),to_station=input("Enter to-station: ").upper())
            a=self.get_status()
            if a=="no":
                print("No more tickets for this train..")
                return
            else:
                print("In order to get the fare details please enter again\n")
                self.get_fare_info(from_station=input("Enter from-station: ").upper(),to_station=input("Enter to-station: ").upper())
        elif self.Menu.lower() in ("2.check status","check status",'2'):
            print(f"Confirmed you want to {self.Menu.capitalize()}")
            print("Checking status:")
            self.get_status()
        elif self.Menu.lower() in ("3.collect fare details","collect fare details",'3'):
            print(f"Confirmed you want to {self.Menu.capitalize()}")
            print("Collecting the fare deails..")
            self.get_fare_info(input("Enter from-station: ").upper(),input("Enter to-station: ").upper())
        else:
            print(f"Something went wrong bro...,Try again..")
obj=Train()