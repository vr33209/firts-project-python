from flask_restful import Resource, reqparse
from models.hotel import HotelModel


hoteis = [
            {
                "id":1,
                "name":"Copacana Pallace",
                "starts":5.0,
                "city":"Rio de Janeiro"
            },
            {
                "id":2,
                "name":"Copacana",
                "starts":4.0,
                "city":"Rio de Janeiro"
            },
            {
                "id":3,
                "name":"Pallace",
                "starts":4.0,
                "city":"São paulo"
            }
        ]

class Hoteis(Resource):
    def get(self):
        
        return { "hoteis":hoteis}

def verifyExistHotel(hoteis, id):
        for hotel in hoteis:
            if hotel["id"] == id:
                return hotel
        return False 
    
class Hotel(Resource):
    def get(self, id):
        for hotel in hoteis:
            if hotel["id"] == id:
                return hotel
        return {"message":"Hotel não encontrado!"},400

    def post(self,id):
        body = reqparse.RequestParser()
        body.add_argument("name")
        body.add_argument("starts")
        body.add_argument("city")
        dados = body.parse_args()        
        hotel_obj = HotelModel(id,**dados)
        new_hotel = hotel_obj.json()
        hoteis.append(new_hotel)
        return  new_hotel

    def delete(self,id):
        print(self)

    def put(self,id):
        hotel = verifyExistHotel(hoteis,id)
        if hotel:
            body = reqparse.RequestParser()
            body.add_argument("name")
            body.add_argument("starts")
            body.add_argument("city")
            dados = body.parse_args()
            hotel.update(**dados)
            return hotel 
        body = reqparse.RequestParser()
        body.add_argument("name")
        body.add_argument("starts")
        body.add_argument("city")
        dados = body.parse_args()
        new_hotel = {'id':id,**dados}
        hoteis.append(new_hotel)
        return new_hotel 
