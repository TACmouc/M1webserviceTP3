from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Exemple de données (utilisez une base de données réelle dans un environnement de production)
films = [
    {
        'id': 1,
        'nom': 'Film 1',
        'description': 'Description du film 1',
        'date_parution': '2023-01-01',
        'acteurs': [1, 2],
        'realisateurs': [1],
    },
    {
        'id': 2,
        'nom': 'Film 2',
        'description': 'Description du film 2',
        'date_parution': '2023-02-01',
        'acteurs': [2, 3],
        'realisateurs': [2],
    },
]

acteurs = [
    {
        'id': 1,
        'nom': 'Smith',
        'prenom': 'John',
        'date_naissance': '1970-01-01',
    },
    {
        'id': 2,
        'nom': 'Doe',
        'prenom': 'Jane',
        'date_naissance': '1980-02-02',
    },
]

realisateurs = [
    {
        'id': 1,
        'nom': 'Smith',
        'prenom': 'John',
        'date_naissance': '1970-01-01',
    },
    {
        'id': 2,
        'nom': 'Brown',
        'prenom': 'David',
        'date_naissance': '1985-03-03',
    },
]

# Route pour la page d'index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route pour récupérer un film par ID
@app.route('/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    film = next((f for f in films if f['id'] == film_id), None)
    if film is not None:
        return jsonify(film)
    else:
        return 'Film non trouvé', 404

# Route pour récupérer une collection de films
@app.route('/films', methods=['GET'])
def get_films():
    max_results = min(int(request.args.get('max_results', 20)), 20)
    filtered_films = films
    # Ajoutez ici la logique de filtrage par acteurs ou réalisateurs si nécessaire
    return jsonify(filtered_films[:max_results])

# Route pour créer un film
@app.route('/films', methods=['POST'])
def create_film():
    data = request.json
    # Ajoutez ici une logique pour valider les données d'entrée
    new_film = {
        'id': len(films) + 1,
        'nom': data['nom'],
        'description': data['description'],
        'date_parution': data['date_parution'],
        'acteurs': data.get('acteurs', []),
        'realisateurs': data.get('realisateurs', []),
    }
    films.append(new_film)
    return jsonify(new_film), 201

# Route pour mettre à jour un film par ID
@app.route('/films/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    data = request.json
    film = next((f for f in films if f['id'] == film_id), None)
    if film is not None:
        # Ajoutez ici la logique de mise à jour des champs du film
        film['nom'] = data['nom']
        film['description'] = data['description']
        film['date_parution'] = data['date_parution']
        film['acteurs'] = data.get('acteurs', [])
        film['realisateurs'] = data.get('realisateurs', [])
        return jsonify(film)
    else:
        return 'Film non trouvé', 404

# Route pour supprimer un film par ID
@app.route('/films/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    film = next((f for f in films if f['id'] == film_id), None)
    if film is not None:
        films.remove(film)
        return '', 204
    else:
        return 'Film non trouvé', 404

# Ajoutez des routes similaires pour les acteurs et les réalisateurs

if __name__ == '__main__':
    app.run(debug=True)
