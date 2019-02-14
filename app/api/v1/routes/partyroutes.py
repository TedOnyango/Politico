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
    except:
        return make_response(jsonify({"status": 404, "error":
                                      "Provide required fields"}), 404)

    newparty = PartiesModel(id=id, name=name,
                            hqAddress=hqAddress, logoUrl=logoUrl)
    newparty.save_party()

    return make_response(jsonify({"status": 201,
                                  "data": [{
                                      "id": id,
                                      "name": name,
                                      "hqAddress": hqAddress,
                                      "logoUrl": logoUrl
                                  }]
                                  }), 201)


@endpoint.route('/parties', methods=['GET'])
def view_parties():
    PARTIES = PartiesModel.view_parties()
    for party in PARTIES:
        return make_response(jsonify({"status": 200,
                                      "data": PARTIES
                                      }), 200)
    else:
        return make_response(jsonify({"status": 404, "error":
                                      "No parties found"}), 400)


@endpoint.route('/parties/<int:id>', methods=['GET'])
def get_specific_party(id):
    party = PartiesModel.get_specific_party(id)
    if party:
        id == "id"
        return make_response(jsonify({"status": 200, "data":
                                      PartiesModel.get_specific_party(id)
                                      }), 200)
    else:
        return make_response(jsonify({"status": 404, "error":
                                      "No party with such id"}), 404)


@endpoint.route('/parties/<int:id>', methods=['DELETE'])
def delete_party(id):
    PARTIES = PartiesModel.view_parties
    if id == "id":
        PartiesModel.delete_party(id)
        return make_response(jsonify({"status": 200,
                                      "data": "Deleted Sucessfully"
                                      }), 200)
    return make_response(jsonify({"status": 404, "error":
                                  "No party with such id"}), 404)


@endpoint.route('/parties/<int:id>/name', methods=['PATCH'])
def edit_parties(id):
    data = request.get_json()
    name = data["name"]

    party = PartiesModel.edit_party(id, name)
    if party:
        id == "id"
        return make_response(jsonify({"status": 200,
                                      "data": [{"id": id, "name": name}]
                                      }), 200)
    return make_response(jsonify({"status": 404,
                                  "error": "Party not found"
                                  }), 404)
