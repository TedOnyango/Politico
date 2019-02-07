OFFICES = []

class OfficeModel():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        
    @staticmethod
    def view_all_offices():
        return OFFICES

    def save_office(self):
        office = {
            "id": self.id,
            "name": self.name,
            "type": self.type
        }
        OFFICES.append(office)

    @staticmethod
    def get_specific_office(id):
        return [office for office in OFFICES if office["id"] == id]