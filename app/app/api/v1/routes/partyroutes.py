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