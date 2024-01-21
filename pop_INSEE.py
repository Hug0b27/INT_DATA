import urllib.request
import json
import pyodbc

def perform_api_request():
    url = "https://geo.api.gouv.fr/communes/"
    params = {"fields": "population"}

    try:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"

        with urllib.request.urlopen(full_url) as response:
            if response.getcode() == 200:
                data = json.load(response)
                return data
            else:
                print(f"Erreur lors de la requête API : {response.getcode()} {response.read().decode('utf-8')}")
                return None

    except urllib.error.URLError as e:
        print(f"Erreur lors de la requête API : {e}")
        return None

api_data = perform_api_request()

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-70TTSDM;DATABASE=INT_DATA;UID=root;PWD=root'
connection = pyodbc.connect(connection_string)

cursor = connection.cursor()

for entry in api_data:
    code_postal = entry.get("codePostal", "")
    population_info = entry.get("population", 0)

    update_query = "UPDATE COMMUNES SET Population = ? WHERE Code_postal = ?"
    cursor.execute(update_query, population_info, code_postal)

connection.commit()

cursor.close()
connection.close()
