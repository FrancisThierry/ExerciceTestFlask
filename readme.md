# Exercice : API Flask pour le tableau périodique

## Objectif

Créer une API qui retourne un élément du tableau périodique à partir de son numéro atomique.

## Étapes

### 1. Mock et TDD

1. **Définir l'API**  
    - Endpoint : `/element/<int:numero>`
    - Méthode : `GET`
    - Réponse attendue : JSON avec le nom et le symbole de l'élément.

2. **Écrire les tests unitaires**  
    - Utiliser `pytest` et `Flask` en mode test.
    - Mock des données du tableau périodique (ex : dictionnaire Python).

3. **Développer l'API**  
    - Implémenter l'endpoint en utilisant les données mockées.
    - Vérifier que les tests passent.

### 2. Utilisation de la bibliothèque `mendeleev`

1. Remplacer le mock par la récupération réelle des éléments via `mendeleev`.
2. Adapter les tests si nécessaire.

## Exemple de test unitaire (pytest)

```python
def test_get_element(client):
     response = client.get('/element/1')
     assert response.status_code == 200
     assert response.json == {"nom": "Hydrogène", "symbole": "H"}
```

## Ressources

- [Flask](https://flask.palletsprojects.com/)
- [pytest](https://docs.pytest.org/)
- [mendeleev](https://mendeleev.readthedocs.io/)

---

**Bonus** : Gérer les cas d'erreur (numéro invalide, hors bornes, etc).