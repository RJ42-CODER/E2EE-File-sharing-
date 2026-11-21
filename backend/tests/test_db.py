from sqlalchemy import text
from database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database();")
        )

        print("database connection successful");
        # scalar() method is used to retrieve a single value from the result set. In this case, it retrieves the name of the current database that the connection is connected to. The result is then printed to the console.
        print("Database name:", result.scalar())
except Exception as e:
    print("Error connecting to the database:", e)
    print("Error:", e)