Voici des exemples de requêtes HTTP pour créer, mettre à jour et supprimer un film à l'aide de l'API que nous avons créée dans l'exemple précédent en utilisant l'outil `curl`. Vous pouvez également utiliser des outils comme Postman ou des bibliothèques comme requests en Python pour effectuer ces requêtes.

1. **Créer un film (POST)**

   Pour créer un film, vous devez envoyer une requête POST avec les données du film que vous souhaitez ajouter au point d'extrémité `/films`. Voici un exemple de requête :

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{
       "nom": "Nouveau Film",
       "description": "Description du nouveau film",
       "date_parution": "2023-10-30",
       "acteurs": [1, 2],
       "realisateurs": [1]
   }' http://localhost:5000/films
   ```

   Assurez-vous d'ajuster les données du film en conséquence.

2. **Mettre à jour un film (PUT)**

   Pour mettre à jour un film existant, envoyez une requête PUT avec les données mises à jour au point d'extrémité `/films/<film_id>`, où `<film_id>` est l'identifiant du film que vous souhaitez mettre à jour. Voici un exemple de requête pour mettre à jour un film avec l'ID 1 :

   ```bash
   curl -X PUT -H "Content-Type: application/json" -d '{
       "nom": "Film mis à jour",
       "description": "Nouvelle description du film",
       "date_parution": "2023-11-01",
       "acteurs": [1, 3],
       "realisateurs": [2]
   }' http://localhost:5000/films/1
   ```

   Assurez-vous de spécifier l'ID du film que vous souhaitez mettre à jour et d'ajuster les données en conséquence.

3. **Supprimer un film (DELETE)**

   Pour supprimer un film, envoyez une requête DELETE au point d'extrémité `/films/<film_id>`, où `<film_id>` est l'identifiant du film que vous souhaitez supprimer. Voici un exemple de requête pour supprimer un film avec l'ID 2 :

   ```bash
   curl -X DELETE http://localhost:5000/films/2
   ```

   Assurez-vous de spécifier l'ID du film que vous souhaitez supprimer.

Veuillez noter que ces exemples supposent que votre serveur est en cours d'exécution localement à l'adresse `http://localhost:5000`. Assurez-vous d'ajuster l'URL en fonction de votre configuration de serveur.