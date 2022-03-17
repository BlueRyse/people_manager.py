import json

class people_manager_class:
    def __init__(self):
        self.people_dict = {}
        self.name_list = []
        self.surname_list= []
        self.age_list = []

    def add(self, name, surname, age):
        if (not isinstance(name, str) or
        not isinstance(surname, str) or
        not isinstance(age, str)):
            print("Incorrect type/s")
            return
        self.name_list.append(name)
        self.surname_list.append(surname)
        self.age_list.append(age)
        self.update()

    def update(self):
        self.people_dict['name'] = self.name_list
        self.people_dict['surname'] = self.surname_list
        self.people_dict['age'] = self.age_list

    def remove(self,name,surname,age):
        try:
            self.name_list.remove(name)
            self.surname_list.remove(surname)
            self.age_list.remove(age)
        except ValueError:
            print('The element you are trying to remove is not the dictionary')
            raise
        self.update()

    def print(self):
        print(self.people_dict)
