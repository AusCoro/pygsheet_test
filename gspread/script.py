import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# import psycopg2

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)
# client = pysheet.Client(client)

# Open the Google Sheet
sheet = client.open("datos").sheet1

#  Get all records from the sheet
data = sheet.get_all_records()

print(data)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Mostrar la tabla
print(df)