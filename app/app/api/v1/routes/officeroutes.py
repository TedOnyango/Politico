from flask import Flask, jsonify, make_response, request
from app.api.v1.models.officemodels import OfficeModel
from app.api.v1.models.partymodels import PartiesModel
from app.api.v1.routes import endpoint


@endpoint.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    try:
        type = data['type']
        name = data['name']
        id = data['id']
    except:
        return make_response(jsonify({"status": 400,
									  "error": "Must provide id, name and type"
									  }), 400)

    newoffice = OfficeModel(name=name, type=type, id=id)
    newoffice.save_office()

    return make_response(jsonify({ "status": 201,
									"data": [{
										"type": type,
										"name": name,
										"id": id
									}]
								}), 201)
@endpoint.route('/offices', methods=['GET'])
def get_office(id):
    office = OfficeModel.get_specific_office(id)
    if office:
        return make_response(jsonify({"status": 200, "data": office}), 200)
    return make_response(jsonify({"status": 404, "error": "We cant find this office"}), 404)



 