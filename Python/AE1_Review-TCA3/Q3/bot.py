print("How many heroes must we gather?")
hero_no = int(input())

print("Gathering heroes...")
for gathered_hero in range(1,hero_no+1,1):
    print("...found hero",gathered_hero)
    gathered_hero += 1
print("...all the heroes have been gathered")