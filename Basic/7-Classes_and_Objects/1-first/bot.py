class bot:
    def __init__ (self, name, age=0, energy=0, shield_level=100):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield_level = shield_level
    
    def display_name(self):
        print("-"*(len(self.name)+2))
        print("|"+self.name+"|")
        print("-"*(len(self.name)+2))

    def display_age(self):
        print("                   \\\ ,")
        print("                    \ `|")
        print("                    ) (   .-""-.")
        print("                     | |  /_  {  '.")
        print("                     | | (/ `\   } )")
        print("                     | |  ^/ ^`}   {")
        print("                     \  \ \=  ( {   )")
        print("                      \  \ '-, {   {{")
        print("                       \  \_.'  ) }  )")
        print("                        \.-'   (     (")
        print("                        /'-.'_. ) (  }")
        print("                        \_(    {   _/\\")
        print("                         ) '--' `-;\  \\")
        print("                     _.-'       /  / /")
        print("              <\/>_.'         .'  / /")
        print("          <\/></\>/.  '      /<\// /")
        print("          </\>  _ |\`- _ . -/|<// (")
        print("       <\/>    - _- `  _.-'`_/- |  \\")
        print("       </\>        -  - -  -     \\\\")
        print("        }`<\/>                <\/>`{")
        print("        { </\>-<\/>_<\/>_<\/>-</\> }")
        print("        }      </\> </\> </\>      {")
        print("     <\/>.                         <\/>")
        print("     </\>                          </\>")
        print("      {`<\/>                     <\/>`}")
        print("      } </\>-<\/>_<\/>_<\/>_<\/>-</\> {")
        print("      {      </\> </\> </\> </\>      }")
        print("      }                               }")
        print("      {          H A P P Y",self.age,"          {")
        print("   <\/>        B I R T H D A Y        <\/>")
        print("   </\>                               </\>")
        print("     `<\/>                          <\/>'")
        print("      </\>-<\/>_<\/>_<\/>_<\/>_<\/>-</\>")
        print("           </\> </\> </\> </\> </\> ")

    def display_energy(self):
        print("\nEnergy level:")
        print(str("█"*int(self.energy/20))+str("[]"*(5-int((self.energy/20)))))

    def display_shield(self):
        print("\nShield level:")
        if len(str(self.shield_level)) <=2:
            print("____")
        else:
            print("_____")
        print("["+str(self.shield_level)+"]")
        print("\\"+" "*len(str(self.shield_level))+"/")
        if len(str(self.shield_level)) <=2:
            print(" \\/")
        else:
            print(" \\ /")
            print("  V")

    def display_summary(self):
        self.display_name()
        self.display_age()
        self.display_energy()
        self.display_shield()


    

filip = bot("Filip",29, 80, 10)
darren = bot("Darren",30, 100)
noob = bot("noob", 15, 20)
#filip.display_name()
#filip.display_age()
filip.display_summary()
#darren.display_energy()
#noob.display_energy()