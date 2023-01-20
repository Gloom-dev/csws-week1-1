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
    message += f"Damn, I just found out the table won't arrive in time. I have to shrink the list..."
    print(message)

for x in range(len(guests)):
    if len(guests) > 2:
        shrinkedperson = guests.pop()
        print(f"Sorry, {shrinkedperson}. Because i dont't have any space I have to remove you from the list...")
