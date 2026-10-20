from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced, print_queue_demo


def menu():

    while True:

        print("\n===== DATA STRUCTURES MENU =====")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Array Queue")
        print("4. Linked Queue")
        print("5. Balanced Parentheses")
        print("6. Print Queue Simulation")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":

            stack = ArrayStack(3)

            try:
                stack.push(10)
                stack.push(20)

                print("Stack:", stack)

                print("Pop:", stack.pop())

            except Exception as e:
                print(e)

        elif choice == "2":

            stack = LinkedStack()

            stack.push(10)
            stack.push(20)

            print("Top:", stack.peek())

        elif choice == "3":

            queue = ArrayQueue(5)

            queue.enqueue("A")
            queue.enqueue("B")

            print(queue)

        elif choice == "4":

            queue = LinkedQueue()

            queue.enqueue("A")
            queue.enqueue("B")

            print(queue)

        elif choice == "5":

            expression = input(
                "Enter expression: "
            )

            print(
                "Balanced"
                if is_balanced(expression)
                else "Not Balanced"
            )

        elif choice == "6":
            print_queue_demo()

        elif choice == "0":
            break

        else:
            print("Invalid option")


menu()