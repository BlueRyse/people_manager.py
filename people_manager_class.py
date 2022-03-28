import json

class people_manager_class:
    def __init__(self):
        self.people_list = []
        self.people_dict = {"people":self.people_list}

    def add(self, name, surname, age):
        if (not isinstance(name, str) or not isinstance(surname, str) or
        not age.isnumeric()):
            print("Incorrect type/s. No changes have been made.")
            return
        dict = {}
        dict.update({"name":name, "surname":surname, "age":age})
        self.people_list.append(dict)

    def update_age(self,name,surname,age):
        for dict in self.people_list:
            if(dict['name'] == name and dict['surname'] == surname):
                dict['age'] = age
                return

        print("Nothing to update.")

    def remove(self,name,surname,age):
        try:
            dict={}
            dict.update({"name":name, "surname":surname, "age":age})
            self.people_list.remove(dict)
        except ValueError:
            print("The element you are trying to remove doesn't exist")
            return

    def same_person_check(self,name,surname,age):
        dict={}
        dict.update({"name":name, "surname":surname, "age":age})
        return dict in self.people_list

    def same_name_surname(self,name,surname):
        for dict in self.people_list:
            return (dict['name'] == name and dict['surname'] == surname)

    def get_json(self):
        json_data = json.dumps(self.people_dict, indent=2)
        return json_data
