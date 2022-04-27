# Importation des classes pour la configuration
from config.DB import DB
from config.AlexAPI import AlexAPI
from config.ResearchInitializer import ResearchInitializer
from config.Source import Source

# Importation des classes pour la gestion des sous-ensemble API
from API.AuthorAPI import AuthorAPI
from API.PublicationAPI import PublicationAPI

class openAlex():
    
    ## En attendant d'avoir le lien entre le site web et le programme python
    research = "Cave Jonathan"
    
    initialize = ResearchInitializer(research)
    
    ## Connexion avec laclea base de donnée, récupération du curseur pour avoir l'accès à l'ensemble des informations 
    dataBase = DB()
    
    ## Permet de récupérer les informations relative à la source 
    sourceID = Source("openAlex", dataBase).getMySQLID()

    ## Récupération des id AlexAPI en fonction du nom de l'utilisateur
    API = AlexAPI()

    ## On prend les informations de l'auteurs en fonction du profil avec le plus d'interaction
    authors = AuthorAPI(initialize.getSortResearch(), initialize.getPrepareResearch(), API, dataBase, sourceID, filter_by = "display_name")

    ## Récupération des articles en fonction des id AlexAPI
    ## Création des liens avec les autres autheurs + création des auteurs dans notre database

    publications = PublicationAPI(authors.getArrayAuthorIDs(), API, dataBase, sourceID, authors.getIdAuthor())

    # Fermeture de la connexion avec la base de donnée
    dataBase.close()