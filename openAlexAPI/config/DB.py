import mysql.connector
import configparser
import inspect

class DB():

    # Initialisation des informations de la base de données
    def __init__(self):
        self.config = self.getConfig()
        self.connector = self.getConnector()
        self.cursor = self.getCursor()
        self.logConnect()


    # Permet la récupération du connector depuis l'ensemble du projet
    def getConnector(self):
        return self.connector


    # Permet la récupération du curseur depuis l'ensemble du projet
    def getCursor(self):
        return self.connector.cursor(buffered=True)
    

    # Permet de connecter depuis les informations du fichier de configuration
    def getConnector(self):
        return  mysql.connector.connect(
            host = self.config['DATABASE']['host'],
            user = self.config['DATABASE']['user'],
            password = self.config['DATABASE']['password'],
            database = self.config['DATABASE']['dbname']
        )


    # Permet de récupérer la configuration du fichier config.ini
    def getConfig(self):
        config = configparser.ConfigParser()
        config.read('././config.ini')
        return config


    # Permet de verifier si la ligne existe déjà, et de l'insérer sinon
    def checkIfExistsOrInsert(self, object, fieldsComparable):

        fields = self.sortByFieldName(self.getObjectFields(object, type = "all"), fieldsComparable)

        sql = 'SELECT * FROM ' + self.getClassName(object) + ' WHERE '

        for field in fields:
            sql += field[0] + ' = "' + field[1] + '" AND '

        self.cursor.execute(sql[:-4])

        if (self.cursor.fetchone()) == None: 
            self.autoInsert(object)


    # Permet de filtrer en fonction des champs de recherche 
    def sortByFieldName(self, fields, fieldsComparable):
        results = []

        for field in fields:
            if field[0] in fieldsComparable:
                results.append(field)
        
        return results


    # Automatisation de l'insertion dans la base de données
    def autoInsert(self, object):

        className = self.getClassName(object)
        fieldsNames = self.getObjectFields(object, type = "names")
        fieldsValues = self.getObjectFields(object, type = "values")

        sql = 'INSERT INTO ' + str(className) + '(' + ", ".join(fieldsNames) + ') VALUES ("' + '", "'.join(fieldsValues) + '")'

        self.cursor.execute(sql)

        print("INFO | Un(e) nouveau/elle " + str(className) + " a été ajouté sur votre base de données")


    # Permet de récupérer les champs d'un objet, que ce soit des noms ou des values
    def getObjectFields(self, object, type):
        fields = []

        for field in inspect.getmembers(object):
            if not field[0].startswith('_') and not inspect.ismethod(field[1]) and not field[0] == "database":
                if(type == "names"):
                    fields.append(field[0])
                elif(type == "values"):
                    fields.append(str(field[1]))
                elif(type == "all"):
                    fields.append(field)
        return fields


    # Permet de récupérer le nom de la classe actuelle
    def getClassName(self,object):
        return type(object).__name__


    # Permet de vérifier la bonne connexion a la base de données
    def logConnect(self):

        self.cursor.execute("SELECT VERSION()")

        results = self.cursor.fetchone()

        if results:
            print("INFO | Connexion effectuée avec votre base de donnée")
        else:
            print("ERROR | Problème avec la connexion de votre base de donnée")


    # Permet de fermer la connexion a la base de données
    def close(self):
        self.cursor.close()
        self.connector.close()