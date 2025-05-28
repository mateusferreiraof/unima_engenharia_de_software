import requests
import json
import os
from dotenv import load_dotenv



class TMDBAPI:
    def __init__(self):
        load_dotenv()  # Carrega variáveis de ambiente do .env
        token = os.getenv("TMDB_TOKEN") 
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}" 
      }

    #lista de filmes
    def movie_list(self,page:int = 1 ):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=pt-BR&page={page}&sort_by=popularity.desc"

        response = requests.get(url, headers=self.headers).json()#esse .json vai formatar no arquivo de forma correta

        return self.to_json(response, "movie.json")
    
    #lista de séries
    def series_list(self, page:int=1):
        url = f"https://api.themoviedb.org/3/tv/popular?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response,"series.json")
    
    #pesquisar filmes
    def movie_search(self,query:str, page:int = 1):
       url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=pt-BR&page={page}"
       response = requests.get(url, headers=self.headers).json()
       return self.to_json(response,"movie.json")
    
    #imagem dos posters
    def movie_image(self,image_id:str):
        return f'https://image.tmdb.org/t/p/w500/{image_id}'
    
    #categoria filmes
    def movie_category(self,query:str, page:int =1):
        url = f"https://api.themoviedb.org/3/discover/movie?with_genres={query}&language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response,"movie.json") 

    #excolhendo o caminho do json, vai ser executado sempre     
    def to_json(self, response: dict, filename): 
        try:
            if filename == "movie.json":
                filepath = os.path.join("D:/unima engenharia/unima_engenharia_de_software/Api", 'movie.json')
            elif filename == "series.json":
                filepath = os.path.join("D:/unima engenharia/unima_engenharia_de_software/Api", 'series.json')
            else:
                filepath = os.path.join("D:/unima engenharia/unima_engenharia_de_software/Api", filename)

            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(response, file, indent=4)

            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)

        except Exception as e:
            print(f"[ERRO to_json] {e}")
        return {}

if __name__ == "__main__":
    api = TMDBAPI()
    api.movie_list()
    api.series_list()
