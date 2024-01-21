import urllib.request
import json
import pyodbc

# Fonction pour effectuer la requête API
def perform_api_request():
    url = "https://geo.api.gouv.fr/communes/"
    params = {"fields": "population"}

    try:
        # Créer l'URL complet avec les paramètres
        full_url = f"{url}?{urllib.parse.urlencode(params)}"

        # Effectuer la requête GET
        with urllib.request.urlopen(full_url) as response:
            # Vérifier si la requête a réussi (code d'état 200)
            if response.getcode() == 200:
                data = json.load(response)
                return data
            else:
                print(f"Erreur lors de la requête API : {response.getcode()} {response.read().decode('utf-8')}")
                return None

    except urllib.error.URLError as e:
        print(f"Erreur lors de la requête API : {e}")
        return None

# Données de l'API
api_data = perform_api_request()

# Connexion à la base de données SQL Server
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-70TTSDM;DATABASE=INT_DATA;UID=root;PWD=root'
connection = pyodbc.connect(connection_string)

# Créer un curseur
cursor = connection.cursor()

# Itérer sur les données de l'API et mettre à jour la base de données
for entry in api_data:
    code_postal = entry.get("codePostal", "")
    population_info = entry.get("population", 0)

    # Requête de mise à jour
    update_query = "UPDATE COMMUNES SET Population = ? WHERE Code_postal = ?"
    cursor.execute(update_query, population_info, code_postal)

# Valider la transaction
connection.commit()

# Fermer le curseur et la connexion
cursor.close()
connection.close()
