# to connect the data with the database. It uses the psycopg2 library to establish a connection to a PostgreSQL database using the provided credentials and connection details. The function returns a connection object that can be used to interact with the database.

import os
from unittest.mock import Base
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

# creates database session for interacting with the database. It is used to manage transactions and perform database operations such as querying, inserting, updating, and deleting records. The session is configured to not autocommit changes and not autoflush changes to the database until explicitly requested.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# base class for our database models
Base = declarative_base()