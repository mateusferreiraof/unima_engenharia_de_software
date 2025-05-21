#consumir a api
from dotenv import load_dotenv
import os
import requests

load_dotenv()


def consumir_api():
    url='https://api.themoviedb.org/3/movie/top_rated' 
    
    params = {
        'api_key': 'bf1e991755f817543033fdc441f26cad',
        'language': 'pt-BR',
        'page': 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consumir a API: {e}")
        return None
