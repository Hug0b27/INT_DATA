# INTEGRATION DE DONNEES

Le projet est d'integrer des données à partir d'un fichier csv fourni au préalable dans une base de données. Ce fichier contient une liste de communes de france avec des informations telles que leur code INSEE, leur code postal et le nom de la commune.
Nous devrons faciliter la lecture de ces données avec la creation d'un TRIGGER  pour suivre les actions effectuées sur les tables, et une VIEW pour extraire la aprtie des données qui nous intéresse particulièrement dans une ou plusieurs tables.

Nous verrons dans ce projet comment faire cette intégrationa partir d'un csv, creer le TRIGGER et la VIEW et en dernier lieu récupérer des données supplémentaires à partir d'une API et les intégrer à notre base.

# TECHNOLOGIES

- Python version 3.x : script d'intégration par API
- Serveur SQL Server
- DBeaver : Gestionnaire de base de données SQL Server

# CREATION DE LA BASE DE DONNEES 

- Se connecter à son serveur SQL Server
- Clic droit sur le serveur -> "Créer une base de données"  -> Nommer la base de données ("INT_DATA" pour moi) -> Clic OK

# IMPORTATION DES DONNEES VIA FICHIER CSV AVEC DBEAVER

- Déployer le menu déroulant de la base de données jusqu'à "Tables" -> Clic droit sur "Tables" -> Importer des données
- Choisir CSV comme source
- Choisir le fichier à importer (019HexaSmal.csv dans mon cas) -> modifier le ColumnDelimiter en fonction du fichier (";" pour ma part)
- Parametrer la table en fonction des besoins
- Terminer l'intégration en cliquant sur "Commencer"
- Renommer la table si besoin ("COMMUNES" pour ma part)

# CREATION DU TRIGGER

voir fichier CREATE_TRIGGER.sql

Le trigger permet de voir qui a fait une intégration sur la table COMMUNES et quand.

# CREATION DE LA VIEW

voir fichier CREATE_VIEW.sql

Dans mon cas la vue permet de lister à partir de notre table COMMUNES, toutes les communes du Nord Pas de Calais en se basant sur les codes postaux commencant par 59 et 62.

# RECUPERATION DE DONNEES DE POPULATION VIA API

voir fichier pop_INSEE

Dans cette étape, nous devons récuperer les information de popiulation des commmunes à partir du code INSEE. Pour cela nous intérgerons l'API Geo via un script Python.
Notre script doit pouvoir se connceter à notre de base de données SQL Server, il faut donc lui donner les paramètres personnalisés de votre serveur de base de données pour qu'il s'y connecte.
Il faut aussi avoir installé au préalable les bibliothèque python suivantes sur votre machine: 
- requests -> pip install requests
- pyodbc -> pip install pyodbc

Une fois les données récupérées, nous les intégrons dans la même table COMMUNES que nous utilisions.

Nous avons donc terminé ce projet, notre base de données a été enrichie grâce à des données externes, nous avons une vue des communes du Nord Pas de Calais et un trigger d'intégration




