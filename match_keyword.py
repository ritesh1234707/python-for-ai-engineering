name = input("What's your name? ")

match name: 
    case "Harry" | "Tonny" | "Luffy" | "Zoro":
        print ("One Piece")
    case "Eren":
        print("siganshina")
    case _:
        print("Who? ")