

def chess_board(n , k):
    w = k * " "
    b = k * "#"

    for _ in range(n):
        for _ in range(k):
            for _ in range(n):
                print(w + b, end="")
            print()

        for _ in range(k):
            for _ in range(n):
                print(b + w, end="")
            print()
