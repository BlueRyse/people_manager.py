import json

class people_manager_class:
    def __init__(self):
        self.people_list = []
        self.people_dict = {'people':self.people_list}

    def add(self, name, surname, age):
        if (not isinstance(name, str) or not isinstance(surname, str) or
        not isinstance(age, str)):
            print("Incorrect type/s")
            return
        dict = {}
        dict.update({'name':name, 'surname':surname, 'age':age})
        self.people_list.append(dict)

    def remove(self,name,surname,age):
        try:
            dict={}
            dict.update({'name':name, 'surname':surname, 'age':age})
            self.people_list.remove(dict)
        except ValueError:
            print('The element you are trying to remove doesn\'t exist')
            raise

    def get_json(self):
        json_data = json.dumps(self.people_dict, indent=2)
        return json_data
