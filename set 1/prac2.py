while True:
    l = float(input("Enter the length: "))
    b = float(input("\nEnter the breadth: "))
    print("\n1. Area\n2. Perimeter\n3. Exit")
    cho = int(input("\nEnter the choice: "))
    if cho == 1:
        area = l * b
        print("\nArea of the rectangle with length", end="")
        print(l, "and breadth", b, "is: ", area)
    elif cho == 2:
        perimeter = 2 * (l + b)
        print("\nPerimeter of the rectangle with length", end="")
        print(l, "and breadth", b, "is: ", perimeter)
    elif cho == 3:
        break
    else:
        print("Invalid Input!")
