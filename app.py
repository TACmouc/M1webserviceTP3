import requests

url = 'http://localhost:5000/films'

new_film = {
    'nom': 'Nouveau Film',
    'description': 'Description du nouveau film',
    'date_parution': '2023-10-30',
    'acteurs': [1, 2],  # Remplacez par les ID d'acteurs existants
    'realisateurs': [1],  # Remplacez par les ID de réalisateurs existants
}

response = requests.post(url, json=new_film)

if response.status_code == 201:
    print('Film créé avec succès.')
    print(response.json())
else:
    print('Échec de la création du film.')
    print(response.text)
