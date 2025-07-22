import pandas as pd
import pygsheets
import requests
import datetime

# URL de la API desde donde se obtendrán los datos
url = 'https://fakestoreapi.com/products'

# Configuración de las columnas requeridas y sus tipos
required_columns = ['Concept', 'Quantity', 'Amount', 'Date', 'Category']
column_types = {
    'Concept': str,
    'Quantity': int,
    'Amount': float,
    'Date': str,
    'Category': str
}

# Autorizar al cliente de pygsheets para usar las credenciales de Google
gc = pygsheets.authorize(service_file='credentials.json')

# Abrir la hoja de cálculo
sh = gc.open('datos')

# Verificar si existe una hoja llamada 'Hoja1', si no, crearla
worksheet_names = [ws.title for ws in sh.worksheets()]
if 'Hoja1' not in worksheet_names:
    print("Hoja1 no existe, creando...")
    sh.add_worksheet('Hoja1')
    print("Hoja1 creada..")

# Seleccionar la hoja con nombre 'Hoja1'
wks = sh.worksheet_by_title('Hoja1')

# Obtener los datos de la hoja de cálculo
df = wks.get_as_df()
print(df)

# Verificar y agregar columnas si faltan
for col in required_columns:
    if col not in df.columns:
        df[col] = pd.Series(dtype=column_types[col])

wks.set_dataframe(df, (1, 1))

# Obtener datos desde una API externa
try:
    print("Obteniendo datos desde la API...")
    request = requests.get(url, timeout=10)
    products = request.json()
    print("respuesta exitosa de la API.")
except Exception as e:
    print(f"Error al obtener los datos de la API: {e}")
    exit(0)


product_df = pd.DataFrame(products)
print("Datos obtenidos de la API:")
print(product_df)

# Create rows to insert into the Google Sheet
rows_to_insert = []
for _, product in product_df.iterrows():
    concept = product['title']
    quantity = 1
    amount = product['price']
    date = datetime.date.today().isoformat()
    category = product['category']
    rows_to_insert.append([concept, quantity, amount, date, category])

print("Filas a insertar:")
print(rows_to_insert)

# Insertar los datos en la hoja de cálculo
if rows_to_insert:
    wks.append_table(rows_to_insert)
    print("Datos insertados en la hoja de cálculo.")
    print(wks.get_as_df())
else:
    print("No hay datos para insertar en la hoja de cálculo.")
    exit(0)