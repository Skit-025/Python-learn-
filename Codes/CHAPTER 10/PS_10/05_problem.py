import random as rn
class Train:
    def __init__(self):
        print("****-MENU-****\n 1.Book\n 2.Check status\n 3.Collect fair details")
        self.Menu=input("ENTER WHAT DO YOU WANT: ")
        if self.Menu.lower()=="1.book" or "book":
            print(f"Confirmed you want to {self.Menu.capitalize()}")
            self.book(input("Enter from-station: "),input("Enter to-station: "))
            self.get_status()
        elif self.Menu.lower()=="2.check status" or "check status":
            print(f"Confirmed you want to {self.Menu.capitalize()}")
        elif self.Menu.lower()=="3.collect fair details" or "collect fair details":
            print(f"Confirmed you want to{self.Menu.capitalize()}")
        else:
            print(f"Something went wrong bro...,Try again..")
    def book(self,from_station,to_station):
        print(f"You are going from {from_station} to {to_station}")
        print("Train details..")
        if (from_station=="DMNJ" and to_station=="BBSR") or (from_station=="BBSR" and to_station=="DMNJ"):
            Trains=["1.Hirakhand Express","Skit's Train"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
        elif (from_station=="KOAA" and to_station=="PNBE") or (from_station=="PNBE" and to_station=="KOAA"):
            Trains=["1.Akal Takth Express","Ara Garib Rath Express"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
        elif (from_station=="DWK" and to_station=="JAM") or (from_station=="JAM" and to_station=="DWK"):
            Trains=["1.Ahemdabad Vande Bharat Express","Shalimar weekly sf express"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
        elif (from_station=="CSMT" and to_station=="BBSN") or (from_station=="BBSN" and to_station=="CSMT"):
            Trains=["1.Konark Express","Skit's Train"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
    def get_status(self):
        seat=rn.choice(["yes","no"])
        if seat=="yes":
            print("A seat is booked details sent in login mail...")
        else:
            print("No more tickets for this train..")
    def get_fair_info(self,from_station,to_station):
        if (from_station=="DMNJ" and to_station=="BBSR") or (from_station=="BBSR" and to_station=="DMNJ"):
            Trains=["1.Hirakhand Express","Skit's Train"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
        elif (from_station=="KOAA" and to_station=="PNBE") or (from_station=="PNBE" and to_station=="KOAA"):
            Trains=["1.Akal Takth Express","Ara Garib Rath Express"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
        elif (from_station=="DWK" and to_station=="JAM") or (from_station=="JAM" and to_station=="DWK"):
            Trains=["1.Ahemdabad Vande Bharat Express","Shalimar weekly sf express"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
        elif (from_station=="CSMT" and to_station=="BBSN") or (from_station=="BBSN" and to_station=="CSMT"):
            Trains=["1.Konark Express","Skit's Train"]
            print(f"Trains available{Trains}")
            train=input("Choose any one train...")
obj=Train()