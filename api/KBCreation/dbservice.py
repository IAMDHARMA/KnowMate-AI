import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():

    conn=psycopg2.connect(
        dbname=os.getenv("Postgress_DB"),
        user = os.getenv("Postgress_User"),
        password= os.getenv("Postgress_Password"),
        host = os.getenv("Postgress_Host"),
        port = os.getenv("Postgress_Port")
    )
    
    return conn
