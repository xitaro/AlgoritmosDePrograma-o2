from Queue import Queue

queue = Queue()
option = -1

while(option != 0):
    print('''
    1 - Add
    2 - Delete
    3 - Print
    4 - Inverted Print
    0 - Quit
    ''')

    option = input("Choose a option: ")

    if option == '1':
        value = input("Enter a value: ")
        queue.append(value)
    
    if option == '2':
        queue.dequeue()
        pass

    if option == '3':
        queue.print()
    
    if option == '4':
        queue.invertedPrint()
    