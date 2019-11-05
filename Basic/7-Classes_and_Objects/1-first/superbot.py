from bot import bot

class superbot(bot):
    def __init__(self,name,age,energy,shield_level,super_power_level = 1):
        super().__init__(name,age,energy,shield_level)
        self.super_power_level = super_power_level

    def get_super_power(self):
        self.super_power_level = int(input("What is Super Bot a super power level? 1 to 5 \n"))
        if self.super_power_level >= 1 and self.super_power_level <= 5:
            print("Super Bot is charged")
        else:
            print("Invalid input")

    def display_super_power_level(self):
        print("\nSuper Power Energy level:")
        print(str("█"*int(self.super_power_level)+str("[]"*(5-int((self.super_power_level))))))

    def display_superbot_summary(self):
        return super().__str__()

filip = superbot("Filip",29, 90, 60)
darren = bot("Darren",30, 100, 30)
noob = bot("noob", 15, 20, 50)

filip.get_super_power()
filip.display_super_power_level()