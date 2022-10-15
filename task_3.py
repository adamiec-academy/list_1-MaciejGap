def envelope(n):
    # segment 1
    print((n * 2 + 1) * "*")

    # segment 2
    for i in range(n - 1):
        print("*" + i * " " + "*" + (2 * n - 3 - 2 * i) * " " + "*" + i * " " + "*")

    # Segment 3
    print("*" + (n - 1) * " " + "*" + (n - 1) * " " + "*")

    # Segment 4
    for i in range(n - 1):
        print("*" + (n - 2 - i) * " " + "*" + (2 * i + 1) * " " + "*" + (n - 2 -i) * " " + "*")

    # Segment 5
    print((n * 2 + 1) * "*")
