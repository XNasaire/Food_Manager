from flask import Blueprint, request, jsonify
from backend.modeles.Nourriture import Nourriture
from backend.database import db

nourriture_bp = Blueprint('nourriture', __name__)

@nourriture_bp.route('/nourritures', methods=['GET'])
def get_nourritures():
    return "Liste des nourritures (exemple)"

@nourriture_bp.route('/nourriture', methods=['POST'])
def ajouter_nourriture():
    data = request.json
    nom = data.get('nom')
    user_id = data.get('user_id')
    if not nom or not user_id:
        return jsonify({'error': 'Champs manquants'}), 400
    n = Nourriture(nom=nom, user_id=user_id)
    db.session.add(n)
    db.session.commit()
    return jsonify({'message': 'Nourriture ajoutée'}), 201

@nourriture_bp.route('/nourriture/<int:id>', methods=['DELETE'])
def supprimer_nourriture(id):
    n = Nourriture.query.get(id)
    if not n:
        return jsonify({'error': 'Nourriture non trouvée'}), 404
    db.session.delete(n)
    db.session.commit()
    return jsonify({'message': 'Nourriture supprimée'}), 200
