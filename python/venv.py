import os
os_version = os.getenv('OS')
print(os_version)

# using dotenv

# .env file
DATABASE=Sample_Connection_String

#app.py
from dotenv import load_env
import os
load_env()
database = os.getenv('DATABASE')
print(database)
