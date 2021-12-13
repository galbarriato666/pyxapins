print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

secret_number = 777

num = int(input("Intro num "))

while num != secret_number:
    if num != secret_number:
        print("Ha ha! you're stuck in my loop")
    num = int(input("Intro num "))
else:
    if num == secret_number:
        print("Well done")
print("End of the program")