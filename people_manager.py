from people_manager_class import people_manager_class

def main():
    people_manager = people_manager_class()
    print("Available operations: 1 add, 2 remove, 3 quit \n")
    operation = input("Input the corrispondent number: ")

    while operation != '3' and (operation == '1' or operation == '2'):
        if operation == '1':
            print("Add operation:")
            name = input("What is the person\'s name?: ")
            surname = input("What is the person\'s surname?: ")
            age = input("What is the person\'s age?: ")

            if people_manager.same_person_check(name,surname,age):
                same = input("You are trying to add a person that's already in the list, are you sure? y/n: ")
                if(same == 'y'):
                    people_manager.add(name,surname,age)
                else:
                    print("No changes have been made.")

            if people_manager.same_name_surname(name,surname):
                same = input("A person with the same name has been detected in the list. Do you want to update? y/n: ")
                if(same == 'y'):
                    people_manager.update_age(name,surname,age)
                elif(same == 'n'):
                    same = input("Do you want to add it? y/n: ")
                    if(same == 'y'):
                        people_manager.add(name,surname,age)
                    else:
                        print("No changes have been made. ")
                else:
                    print("Wrong input. No changes have been made.")

            if(not people_manager.same_person_check(name,surname,age)
            and not people_manager.same_name_surname(name,surname)):
                people_manager.add(name,surname,age)

            print()
        else:
            print("Remove operation:")
            name = input("What is the person's name?: ")
            surname = input("What is the person's surname?: ")
            age = input("What is the person's age?: ")
            people_manager.remove(name,surname,age)
            print()
        operation = input("What's next? Input the corrispondent number: ")
        print()

    if(len(people_manager.people_list) == 0 and operation != '3' and not operation.isnumeric()
    and len(people_manager.people_list) != 0):
        print("Wrong input")
        quit()

    if(len(people_manager.people_list) != 0):
        json = people_manager.get_json()
        print(json)
    else:
        print("No people added. Nothing to print.")

if __name__ == "__main__":
    main()
