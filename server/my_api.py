from fastapi import FastAPI
from connection_mongo import DataAccess

app = FastAPI()


@app.get("/unique_countries") # http://127.0.0.1:8000/unique_countries
def get_list_of_countries():
    unique_countries = DataAccess.get_unique_countries()
    return unique_countries


@app.get("/country/{country}")
# par exemple : http://127.0.0.1:8000/country/France
def get_all_documents_for_country(country: str):
    documents = DataAccess.get_all_documents_by_country(country)
    return documents


@app.post("/add_document")
def create_document(document: dict):
    DataAccess.add_new_document_to_db(document)
    return {"message": "Entry added successfully"}


@app.put("/update_document/{country}")
def update_document(country: str, new_document: dict):
    DataAccess.update_document_by_country(country, new_document)
    return {"message": "Document updated successfully"}


@app.delete("/delete_document/{country}")
def delete_document(country: str):
    DataAccess.delete_document_by_country(country)
    return {"message": "Document deleted successfully"}


@app.get("/latest_data/{country}")
def get_latest(country: str):
    document = DataAccess.get_latest_data(country)
    return document


@app.get("/total_co2_2022") 
def get_total_co2():
    total = DataAccess.get_co2_emissions_sum()
    print(total)
    return total



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
