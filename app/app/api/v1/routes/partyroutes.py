from flask import request, make_response, jsonify

from app.api.v1.models.partymodels import PartiesModel
from app.api.v1.routes import endpoint

@endpoint.route('/parties', methods=['POST'])
def create_party():
    try: 
         data = request.get_json()
         id = data["id"]
         name = data["name"]
         hqAddress = data["hqAddress"]
         logoUrl = data["logoUrl"]
         newparty = PartiesModel(id=id, name=name, hqAddress=hqAddress, logoUrl=logoUrl)
         newparty.save_party()
         return make_response(jsonify({"status": 201,
                                  "data": [{
                                      "id": id,
                                      "name": name,
                                      "hqAddress": hqAddress,
                                      "logoUrl": logoUrl,
                                  }]
                                  }), 201)
@endpoint.route('/parties', methods=['GET'])
def view_parties():
    if party:
        return (jsonify({"status": 200,
                                  "data": PartiesModel.view_parties()
                                  }), 200)
@endpoint.route('/parties', methods=['GET'])
def get_specific_party(id):
    if party:
        return make_response(jsonify({"status": 200,
                                  "data": PartiesModel.get_specific_party(id)
                                  }), 200)
    return make_response(jsonify({"status": 404, 
                                    "error": "Party cannot be found"
                                    }), 404)
                                    @endpoint.route('/parties/<int:id>/name', methods=['PATCH'])
def edit_parties(id):
    try:
        data = request.get_json()
        name = data["name"]
        return make_response(jsonify({"status": 200,
                                  "data": [
                                      {
                                          "id": id,
                                          "name": name
                                      }
                                  ]
                                  }), 200)
    return make_response(jsonify({"status": 404,
                                  "error": "Party not found"
                                  }), 404)
     