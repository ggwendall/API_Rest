from pymongo import MongoClient
from bson import json_util
import json

class DataAccess:
    user = "root"
    mdp = "pass12345"
    db_name = "environment"
    collection_name = "worldcarbon"

    
    @classmethod
    def connexion(cls):
        # cls.client = MongoClient(f"mongodb://{cls.user}:{cls.mdp}@127.0.0.1:27017")   # connection string for local
        cls.client = MongoClient(f"mongodb://{cls.user}:{cls.mdp}@mongo:27017")         # connection string for container
        cls.db = cls.client[cls.db_name]
        cls.worldcarbon = cls.db[cls.collection_name]

    
    @classmethod
    def deconnexion(cls):
        cls.client.close()


    # Returns a list of all the unique values for the "Country" key in the database
    @classmethod 
    def get_unique_countries(cls):
        cls.connexion()
        unique_countries = cls.worldcarbon.distinct("Country")
        cls.deconnexion()
        return unique_countries
    
    
    @classmethod
    def get_all_documents_by_country(cls, country):
        cls.connexion()
        # Retrieve all the unique values for the "Country" key in the database
        unique_countries = cls.worldcarbon.distinct("Country")
        # Check if the specified country value is in the list of unique countries
        if country not in unique_countries:
            cls.deconnexion()
            return {"message": f"{country} not found in database"}
        # Retrieve all the documents that have the specified country value for the "Country" key
        documents = cls.worldcarbon.find({"Country": country})
        # Convert each document to a JSON object and append it to a list of JSON documents
        json_docs = []
        for document in documents:
            json_doc = json.loads(json_util.dumps(document))
            json_docs.append(json_doc)
        cls.deconnexion()
        # Return the list of JSON documents
        return json_docs

    
    @classmethod
    def add_new_document_to_db(cls, document):
        cls.connexion()
        cls.worldcarbon.insert_one(document)
        cls.deconnexion()


    @classmethod
    def update_document_by_country(cls, country, new_document):
        cls.connexion()
        # Convert the new document to a JSON string
        new_document_json = json.dumps(new_document)
        # Parse the JSON string as a dictionary
        new_document_dict = json.loads(new_document_json)
        # Update the document in the database
        cls.worldcarbon.update_one({"Country": country}, {"$set": new_document_dict})
        cls.deconnexion()


    @classmethod
    def delete_document_by_country(cls, country):
        cls.connexion()
        # Delete the document from the database
        cls.worldcarbon.delete_one({"Country": country})
        cls.deconnexion()


    @classmethod
    def get_latest_data(cls, country):
        cls.connexion()
        # Retrieve the document with the latest year (2022) for the specified country
        document = cls.worldcarbon.find_one({"Country": country}, sort=[("Year", -1)])
        if document is None:
            cls.deconnexion()
            return {"message": f"{country} not found in database"}
        json_doc = json.loads(json_util.dumps(document))
        cls.deconnexion()
        return json_doc


    @classmethod
    def get_co2_emissions_sum(cls):
        cls.connexion()
        # Retrieve all the documents for the specified year
        documents = cls.worldcarbon.find({"Year": 2020})
        # Loop over all the documents and sum the values of the "CO2 emission (Tons)" field
        co2_emissions_sum = sum(document["CO2 emission (Tons)"] for document in documents)
        cls.deconnexion()
        json_doc = json.loads(str(co2_emissions_sum))
        return json_doc
    

print(DataAccess.get_co2_emissions_sum())
