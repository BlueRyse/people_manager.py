from people_manager_class import people_manager_class

def main():
    people_manager = people_manager_class()
    print('Available operations: 1 add, 2 remove, 3 quit \n')
    operation = input('Input the corrispondent number: ')

    while operation != '3' and (operation == '1' or operation == '2'):
        if operation == '1':
            print('Add operation:')
            name = input('What is the person\'s name?: ')
            surname = input('What is the person\'s surname?: ')
            age = input('What is the person\'s age?: ')
            people_manager.add(name,surname,age)
            print()
        else:
            print('Remove operation:')
            name = input('What is the person\'s name?: ')
            surname = input('What is the person\'s surname?: ')
            age = input('What is the person\'s age?: ')
            people_manager.remove(name,surname,age)
            print()
        operation = input('What\'s next? Input the corrispondent number: ')
        print()

    if(len(people_manager.people_list) == 0):
        print('Wrong input')
        quit()

    json = people_manager.get_json()
    print(json)

if __name__ == '__main__':
    main()
