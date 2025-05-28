import requests
import json
import os
from dotenv import load_dotenv


class MovieAPI:
    def __init__(self):
        load_dotenv()  # Carrega variáveis de ambiente do .env
        token = os.getenv("TMDB_TOKEN") 
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}" 
      }



    def movie_list(self,page:int = 1 ):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=pt-BR&page={page}&sort_by=popularity.desc"

        response = requests.get(url, headers=self.headers).json()#esse .json vai formatar no arquivo de forma correta

        return self.to_json(response)
    
    def series_list(self, page:int=1):
        url = f"https://api.themoviedb.org/3/tv/popular?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)

    def movie_search(self,query:str, page:int = 1):
       url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=pt-BR&page={page}"

       response = requests.get(url, headers=self.headers).json()

       return self.to_json(response)

    def movie_image(self,image_id:str):
        return f'https://image.tmdb.org/t/p/w500/{image_id}'
    
    def to_json(self, response: dict[str,str]): #essa função vai ser chamada sempre que fizer 
        try:
            with open('response.json','w') as file: #criando o arquivo .json onde ficara os filmes
                json.dump(response,file,indent=4)

            with open('response.json', 'r') as file:
                response_text = json.load(file)    
            return response_text    

        except Exception as e:
            return e


if __name__ =="__main__": 
    MovieAPI().movie_list()
