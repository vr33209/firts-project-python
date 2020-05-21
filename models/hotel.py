class HotelModel:
    def __init__(self,id,name,starts,city):
        self.id = id
        self.name = name
        self.starts = starts
        self.city = city

    def json(self):
        return {
            "id":self.id,
            "name":self.name,
            "starts":self.starts,
            "city":self.city,
        }