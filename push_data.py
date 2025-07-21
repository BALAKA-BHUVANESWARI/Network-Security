import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

# Load MongoDB connection string
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(f"MongoDB URL: {MONGO_DB_URL}")

import certifi
ca = certifi.where()

import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract:
    def __init__(self):
        try:
            # Initialize MongoDB client
            self.mongo_client = None
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            # Read CSV and convert to JSON-like records
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            # Connect to MongoDB
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)

            # Test the connection
            self.mongo_client.admin.command('ping')
            print("✅ Connected to MongoDB successfully!")

            db = self.mongo_client[database]
            col = db[collection]

            # Insert records
            insert_result = col.insert_many(records)
            print(f"✅ Inserted {len(insert_result.inserted_ids)} records.")

            return len(insert_result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        finally:
            if self.mongo_client:
                self.mongo_client.close()
                print("✅ MongoDB connection closed.")

if __name__ == "__main__":
    # ✅ Use raw string for Windows file path
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE = "bhanureddy"
    COLLECTION = "NetworkData"

    try:
        network_obj = NetworkDataExtract()

        # Convert CSV to JSON
        records = network_obj.csv_to_json_convertor(file_path=FILE_PATH)

        # Insert records into MongoDB
        no_of_records = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"✅ Total records inserted: {no_of_records}")

    except Exception as e:
        print(f"❌ Error: {e}")
