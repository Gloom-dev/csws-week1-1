guests = ["Anna", "Hannes", "Felix"]
personleft = "Anna"
personadded = "Mick"
guests.remove(personleft)
guests.append(personadded)
for x in guests:
    message = f"Hi {x.title()}. You are invited to my dinenr party!"
    print(message)
print(f"{personleft} can't make it...")