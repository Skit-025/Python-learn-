class athleats:
    type="Runner"
    sports="400m"
    name="Jessy"
    """A constructer is a special method that is automatically called when an object of a class is created.
    It is used to initialize the attributes of the object."""
    def __init__(self, type, sports, name):#This is a constructer and a dunder method
        self.type=type
        self.sports=sports
        self.name=name
    def details_collector(self):
        return print(f"Athleat type: {self.type} ,Athleat\'s sports: {self.sports} ,Athleat\'s name:{self.name}")
Stessy=athleats("Sprinter","900m","Stessy")
Stessy.details_collector()
Jessy=athleats("Sprinter","200m","Jessy")
Jessy.details_collector()