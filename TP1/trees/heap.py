import heapq

data = [5, 1, 9, 3]

while True:
    print("\nChoose heap type:")
    print("1. Min Heap")
    print("2. Max Heap")
    print("3. Exit")

    choice1 = input("Enter your choice: ")

    if choice1 == "3":
        print("Exiting program.")
        break

    elif choice1 == "1":
        print("\nMIN HEAP")
        data = [5, 1, 9, 3]
        heapq.heapify(data)
        print("Initial heap:", data)

        while True:
            print("\nChoose an operation:")
            print("3. Insert a value")
            print("4. Remove root (min value)")
            print("5. Back to main menu")

            choice2 = input("Enter your choice: ")

            if choice2 == "3":
                val = int(input("Enter a value to insert: "))
                heapq.heappush(data, val)
                print("Heap after insertion:", data)

            elif choice2 == "4":
                if data:
                    print("Removed smallest value:", heapq.heappop(data))
                    print("Heap after removing min:", data)
                else:
                    print("Heap is empty, nothing to remove.")

            elif choice2 == "5":
                break
            else:
                print("Invalid choice, please enter 3..5.")
    elif choice1 == "2":
        print("\nMAX HEAP")
        data = [5, 1, 9, 3]
        max_heap = [-x for x in data]
        heapq.heapify(max_heap)
        print("Initial heap:", [-x for x in max_heap])

        while True:
            print("\nChoose an operation:")
            print("3. Insert a value")
            print("4. Remove root (max value)")
            print("5. Back to main menu")

            choice2 = input("Enter your choice: ")

            if choice2 == "3":
                val = int(input("Enter a value to insert: "))
                heapq.heappush(max_heap, -val)
                print("Heap after insertion:", [-x for x in max_heap])

            elif choice2 == "4":
                if max_heap:
                    print("Removed largest value:", -heapq.heappop(max_heap))
                    print("Heap after removing max:", [-x for x in max_heap])
                else:
                    print("Heap is empty, nothing to remove.")

            elif choice2 == "5":
                break
            else:
                print("Invalid choice, please enter 3..5.")

    else:
        print("Invalid choice, please enter 1..3.")
