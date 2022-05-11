from fastapi import FastAPI

# Partie visualisation
from visualization.PowerCloud import PowerCloud
from visualization.PowerGraph import PowerGraph

# Partie scraper
from specific.openAlex.openAlex import openAlex
from specific.openCitation.openCitation import openCitation
from specific.googleScholar.googleScholar import googleScholar
from specific.hal.hal import hal
from specific.hal.API.FileGenerateAPI import FileGenerateAPI
from config.DB import DB

from io import BytesIO
from starlette.responses import StreamingResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/openAlex/{id_connected_user}")
def open_alex(id_connected_user: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "alternative_name" : getAuthorProfil[5],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0]
    }

    openAlex(research)

@app.get("/openCitation/{id_connected_user}")
def open_alex(id_connected_user: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0]
    }

    openCitation(research)

@app.get("/googleScholar/{id_connected_user}")
def open_alex(id_connected_user: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0]
    }

    googleScholar(research)
    
@app.get("/halCompare/{id_connected_user}")
def hal_compare(id_connected_user: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0]
    }

    hal(research)

@app.get("/generateFile/{id_connected_user}/{idPublication}")
def generate_file(id_connected_user: int, idPublication: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0],
        "id_publication" : idPublication
    }

    publication, authors, concepts  = FileGenerateAPI(research).generateXML()


    return {"publication" : publication, 
            "authors" : authors,
            "concepts" :  concepts}


@app.get("/graph/{id_connected_user}")
def get_graph(id_connected_user: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0]
    }

    PG = PowerGraph(research)

    fig = PG.generatePublicationCoAuthors()

    buf = BytesIO()
    buf.flush()
    fig.savefig(buf, format="png")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")

@app.get("/cloud/{id_connected_user}")
def get_graph(id_connected_user: int):

    myDB = DB()
    getUserProfil = myDB.getFieldsWithId(id_connected_user, "user","id","*","one")
    getAuthorProfil = myDB.getFieldsWithId(getUserProfil[4], "author","id_author","*","one")

    research = {
        "author_name" : getAuthorProfil[2],
        "author_forename" : getAuthorProfil[3],
        "id_connected_user" : getUserProfil[0],
        "id_author_as_user" : getAuthorProfil[0]
    }

    unWordCloud = PowerCloud(myDB)
    
    cloud = unWordCloud.generatePublicationConcept(research["id_author_as_user"])

    buf = BytesIO()
    buf.flush()
    cloud.save(buf, format="png")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")