RED = "red"
BLUE = "blue"
YELLOW = "yellow"


A = input("Enter the first color(Please insert it in a lowwercase): ")
B = input("Enter the second color(Please insert it in a lowercase): ")


if A not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color1")

elif B not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color2")

elif A == B:
    print("Error: The two colors you entered are same")

else:
    if A == RED:
        if B == BLUE:
            print("The new color is PURPLE")
        else:
            print("The new color is ORANGE")
    elif A == BLUE:
        if B == RED:
            print("The new color is PURPLE")
        else:
            print("The new color is GREEN")
    elif A == YELLOW:
        if B == RED:
            print("The new color is ORANGE")
        else:
            print("The new color is GREEN")