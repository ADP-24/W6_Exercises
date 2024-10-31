name = input("Please enter a name: ")

def trunc_name(name):
    name = name.lower()

    if name[0] in 'aeiou':
        return name  # No truncation needed if it starts with a vowel
    
    elif len(name) > 1 and name[1] in 'aeiou':
        return name[1:]  # Return name without the first consonant
    
    elif len(name) > 2 and name[1] not in 'aeiou':
        return name[2:]  # Return name without the first two consonants

    return name  # Just return the name as is if no other case matched

truncated_name = trunc_name(name)
print(f"Truncated name for the song: {truncated_name}")

def name_game(name):
    truncated = trunc_name(name)
    yield f"{name.capitalize()}, {name.capitalize()}, bo-b{truncated}"
    yield f"Banana-fana fo-f{truncated}"
    yield f"Me my mo-m{truncated}"
    yield f"{name.capitalize()}!"

name = input("Enter a name to play the name game: ")
for line in name_game(name):
    print(line)

names = ["Anthony", "Paul", "CHARLIE", "George", "Ringo", "John Lennon"]

for name in names:
    print(f"Name Game for {name}:")
    for line in name_game(name):
        print(line)
    print('\n')