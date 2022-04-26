from tokenize import String
from config.DB import DB
from config.AlexAPI import AlexAPI
from API.Author import Author
from API.Publication import Publication

class openAlex():


    ## En attendant d'avoir le lien entre le site web et le programme python

    research = "SORANA Cimpan"

    ## Connexion avec la base de donnée, récupération du curseur pour avoir l'accès à l'ensemble des informations 
    
    dataBase = DB()

    ## Récupération des id AlexAPI en fonction du nom de l'utilisateur

    API = AlexAPI()

    # On prend les informations de l'auteurs en fonction du profil avec le plus d'interaction

    author = Author(research, API, dataBase, filter_by = "display_name")

    ## Récupération des articles en fonction des id AlexAPI

    publications = Publication(author.getArrayAuthorIDs(), API, dataBase)

    publications.insertPublications()

    ## Création des liens avec les autres autheurs + création des auteurs dans notre database
