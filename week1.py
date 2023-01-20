guests = ["Anna", "Hannes", "Felix"]
personleft = "Anna"
personadded = "Mick"
guests.remove(personleft)
guests.append(personadded)
for x in guests:
    message = f"Hi {x.title()}.{personleft} sadly can't make it... However, I found a bigger table and I will invite more people"
    print(message)

guests.insert(0,"Lennox")
guests.insert(int(len(guests)/2),"Lennart")
guests.append("Omar")

for x in guests:
    message = f"Hi {x.title()}. You are invited to my dinenr party!"
    print(message)
