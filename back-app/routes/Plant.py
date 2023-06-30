from flask import Blueprint, jsonify, request
from models.PlantModel import PlantModel

main=Blueprint('Plant_blueprint', __name__)

@main.route('/')
def get_Plant():
    try:
        Analysis = PlantModel.get_Plant()
        if(len(Analysis) > 0):
            return jsonify(Analysis)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500