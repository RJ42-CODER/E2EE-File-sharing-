from database import Base, engine
from models import User,Session

try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
except Exception as e:
    print("Error creating tables:", e)