count = 99
while count > 0:
    if count == 1:
        print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.\n")
    else:
        print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
        print(f"Take one down, pass it around, {count - 1} {'bottle' if count - 1 == 1 else 'bottles'} of beer on the wall.\n")
    count -= 1

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")
