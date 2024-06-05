import requests
import pandas as pd

# Tu token de acceso de Facebook
ACCESS_TOKEN = 'EAAF8KrhrBe8BO8ykyFgXTaikrgQp3XYanwZAZCHnaMZASnLhOEgaJZBEHwtu3ZBVp7WLZCvmy7Ml1oVL9HqS1iDgWBpkPvtlRdhJ05NQolLZC0WKwZAlZCCre8VsmjmfyHOxfBkRSZBrnO1ARTXMO4eemKEAWqcxZCBDtJjKZATNt8kt38IZAydb5gaOi9VmxFhhgW6iTd1L2h8PZB22C3Y4H8GkU3nLikVHcZD'

# Endpoint de la API de Graph de Facebook
BASE_URL = 'https://graph.facebook.com/v20.0/'

# Función para obtener datos de la API de Facebook
def get_facebook_data(endpoint, params):
    response = requests.get(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Parámetros de consulta
params = {
    'access_token': ACCESS_TOKEN,
    'fields': 'created_time,message,from{name,id},id',
    'limit': 100
}

# Buscar publicaciones que mencionan hospitales en Manabí
search_query = 'hospital Manabí'
search_endpoint = f'search?q={search_query}&type=page_post'

# Realizar la consulta
all_posts = []
data = get_facebook_data(search_endpoint, params)
while 'data' in data:
    posts = data['data']
    for post in posts:
        # Verificar que el campo 'message' existe antes de usarlo
        if 'message' in post:
            all_posts.append(post)
            print(f"Fecha: {post['created_time']}")
            print(f"Usuario: {post['from']['name']}")
            print(f"Mensaje: {post['message']}\n")
    # Verificar si hay más páginas de datos para procesar
    if 'paging' in data and 'next' in data['paging']:
        next_page = data['paging']['next']
        data = requests.get(next_page).json()
    else:
        break

# Convertir los datos a un DataFrame de Pandas para análisis adicional
df = pd.DataFrame(all_posts)
df.to_csv('facebook_hospital_reviews.csv', index=False)
print(df.head())
