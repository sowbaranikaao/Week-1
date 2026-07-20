import os
from dotenv import load_dotenv
load_dotenv()
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
print(f"DB_USER: {db_user}")
print(f"DB_PASSWORD: {db_password}")