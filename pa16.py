# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.
class Surfer:
    def __init__(self,name,speed,jump,accuracy,damage):
        self.name = name
        self.speed = speed
        self.jump = jump
        self.accuracy = accuracy
        self.damage = damage
    def my_detail(self):
        print("Name :: "+self.name)
        print("Speed :: "+self.speed)
        print("Jump :: "+self.jump+" m")
        print("Accuracy :: "+self.accuracy+" %")
        print("Damage :: "+self.damage+" %")
        print("\n")

surfer1 = Surfer('Piku','250','5','76','92')
surfer1.my_detail()
surfer2 = Surfer('Hano','300','7','90','81')
surfer2.my_detail()
