
def ripOjos(input, output):
    with open(output, "wt") as out:
        with open(input, "rt") as int:
            for char in int:
                out.write(char.replace("0", "-"))

ripOjos("Dragon.in", "DragonEyesClosed.out")
ripOjos("Knight.in", "knightEyesClosed.out")
