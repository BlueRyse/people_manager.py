from people_manager_class import people_manager_class

def main():
    people_manager = people_manager_class()
    print('Available operations: 1 add, 2 remove, 3 quit \n')
    x = input('Input the corrispondent number:')

    while x != '3' and (x == '1' or x == '2'):
        if x == '1':
            name = input('What is the person\'s name?:')
            surname = input('What is the person\'s surname?:')
            age = input('What is the person\'s age?:')
            people_manager.add(name,surname,age)
            print()
        else:
            name = input('What is the person\'s name?:')
            surname = input('What is the person\'s surname?:')
            age = input('What is the person\'s age?:')
            people_manager.remove(name,surname,age)
            print()
        x = input('What\'s next? Input the corrispondent number:')
        print()

    json = people_manager.get_json()
    print(json)
    print('Goodbye!')

if __name__ == '__main__':
    main()
