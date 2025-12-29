class Animal:
    type1="omnivores"
    sound="Speak"
    def lion(self):
        self.type1="carnivores"
        self.sound="Raor"
        return print(f"Animal type:{self.type1}, Animal sound: {self.sound}")
    def deer(joy):
        joy.type1="herbivores"
        joy.sound="chew chew"
        return print(f"Animal type:{joy.type1},Animal sound: {joy.sound}")
    # def dog(toffy):
    #     toffy.type1="omnivores"
    #     toffy.sound="bark"
    #     return print(f"Animal type:{toffy.type1}, Animal sound: {toffy.sound}")
obj=Animal()
obj.lion()
Animal.deer(obj)