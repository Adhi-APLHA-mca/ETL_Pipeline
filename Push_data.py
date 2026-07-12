import os 
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
load_dotenv()

from DS_Main_Components.exception.exception import custom_exception

MONGO_DB = os.getenv('MONGO_DB_URL')
ca=certifi.where()

class ETL_DataPusher():
    def __init__(self):
        pass

    def csv_to_json(self,file_path): #  csv -> dataframe -> reset index -> convert row into dict -> return
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise custom_exception(e,sys)
           
    
    def mongodb_uploader(self, records, database_name, collection_name):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB)
            db = self.mongo_client[database_name]
            coll = db[collection_name]
            coll.insert_many(records)
        except Exception as e:
            raise custom_exception(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data\Indian_Agriculture_Dataset.csv"
    DATABASE = "AdhiMachineLearning"
    collection = "Indian_Agriculture_Dataset"
    etl_datapusher_obj = ETL_DataPusher()
    records = etl_datapusher_obj.csv_to_json(file_path=FILE_PATH)
    etl_datapusher_obj.mongodb_uploader(records=records,database_name=DATABASE,collection_name=collection)
    print("process completed")