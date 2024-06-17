def custom_song(name1, name2, adjective1, adjective2, noun1, noun2, place1, place2):
    song = (
        f"The wheels on the bus go round and round,\n"
        f"Round and round, round and round,\n"
        f"The wheels on the bus go round and round,\n"
        f"All through {place1}.\n\n"
        f"The {adjective1} {noun1} on the bus goes up and down,\n"
        f"Up and down, up and down,\n"
        f"The {adjective1} {noun1} on the bus goes up and down,\n"
        f"All through {place1}.\n\n"
        f"The {noun2} on the bus goes {adjective2} and {adjective2},\n"
        f"{adjective2} and {adjective2}, {adjective2} and {adjective2},\n"
        f"The {noun2} on the bus goes {adjective2} and {adjective2},\n"
        f"All through {place2}.\n\n"
        f"{name1} and {name2} on the bus say, \"Move on back,\"\n"
        f"\"Move on back, move on back,\"\n"
        f"{name1} and {name2} on the bus say, \"Move on back,\"\n"
        f"All through {place2}.\n"
    )
    print(song)

name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
place1 = input("Enter a place: ")
place2 = input("Enter another place: ")

custom_song(name1, name2, adjective1, adjective2, noun1, noun2, place1, place2)
