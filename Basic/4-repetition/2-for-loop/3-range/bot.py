brightness = "**"
level = int(input("What level of brightness is required? ")) + 1
print("Adjusting brightness...")
for x in range(2,level,2):
    print("Beep's brightness level: ", brightness)
    print("Bop's brightness level: ", brightness, "\n")
    brightness = brightness + "**"
print("Adjustments complete!")