def run(name):
    print(f"{name} was running through the playground!")

def swing(name):
    print(f"{name} loves playing on the swing!")

def slide(name):
        print(f"{name} always uses the tallest slide!")

def hide_and_seek(name):
        print(f"{name} likes to play hide and seek!")


running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kids in running_kids:
    run(kids)

for kids in swinging_kids:
    swing(kids)

for kids in sliding_kids:
    slide(kids)

for kids in hiding_kids:
    hide_and_seek(kids)
