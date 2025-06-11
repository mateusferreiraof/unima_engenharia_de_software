import requests
import json
from datetime import datetime


class MovieAPI:
    def __init__(self,):
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZjFlOTkxNzU1ZjgxNzU0MzAzM2ZkYzQ0MWYyNmNhZCIsIm5iZiI6MTc0NzQ5MjcyOC44Miwic3ViIjoiNjgyODlmNzhlMjU3NDZlODY1ZjU1Mzc1Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.jpdKsUZBXwaCkjImZxunyQGKbO25nXVxi2XfhaTNgu8"
      }
#fomatando a data    
    @staticmethod
    def datetimeformat(value, format='%d-%m-%Y'):
        if isinstance(value, str):
            try:
                date_obj = datetime.strptime(value, '%Y-%m-%d')
                return date_obj.strftime(format)
            except ValueError:
                return value
        return value

    def movie_list(self,page:int = 1 ):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=pt-BR&page={page}&sort_by=popularity.desc"
        response = requests.get(url, headers=self.headers).json()   
        
        #formatando a data
        for filme in response.get('results', []):
            if 'release_date' in filme and filme['release_date']:
                filme['data_formatada'] = self.datetimeformat(filme['release_date'])
        return self.to_json(response)        
    
    def series_list(self, page:int=1):
        url = f"https://api.themoviedb.org/3/tv/popular?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
       
        #formato data
        for serie in response.get('results', []):
            if 'first_air_date' in serie and serie['first_air_date']:
                serie['data_formatada'] = self.datetimeformat(serie['first_air_date'])
        return self.to_json(response)

    def movie_search(self,query:str, page:int = 1):
       url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=pt-BR&page={page}"
       response = requests.get(url, headers=self.headers).json()
       

       #formatando a data
       for filme in response.get('results', []):
            if 'release_date' in filme and filme['release_date']:
                filme['data_formatada'] = self.datetimeformat(filme['release_date'])
       return self.to_json(response)         
    
    
    def filmes_bem_avaliados(self, page:int=1):
        url = f"https://api.themoviedb.org/3/movie/top_rated?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        
        #formatando a data
        for filme in response.get('results', []):
            if 'release_date' in filme and filme['release_date']:
                filme['data_formatada'] = self.datetimeformat(filme['release_date'])
        return self.to_json(response)   
        
    
    def filmes_populares_tmdb(self, page:int=1):
        url = f"https://api.themoviedb.org/3/trending/movie/day?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
       
        #formatando a data
        for filme in response.get('results', []):
            if 'release_date' in filme and filme['release_date']:
                filme['data_formatada'] = self.datetimeformat(filme['release_date'])
        return self.to_json(response)   
    #filmes por categoria   
 
    def genero_id(self):
            url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-BR"
            response = requests.get(url, headers=self.headers).json()
            return self.to_json(response)
    
    #em cartaz
    def filmes_em_cartaz(self, page:int=1):
        url = f"https://api.themoviedb.org/3/movie/now_playing?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
       
        #formatando a data
        for filme in response.get('results', []):
            if 'release_date' in filme and filme['release_date']:
                filme['data_formatada'] = self.datetimeformat(filme['release_date'])
        return self.to_json(response)  
    
 #se der erro excluir
 # redirecionar para pagina solo   

    def get_detalhes_filme(self,filme_id):
        url = f"https://api.themoviedb.org/3/movie/{filme_id}"
        headers = {
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZjFlOTkxNzU1ZjgxNzU0MzAzM2ZkYzQ0MWYyNmNhZCIsIm5iZiI6MTc0NzQ5MjcyOC44Miwic3ViIjoiNjgyODlmNzhlMjU3NDZlODY1ZjU1Mzc1Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.jpdKsUZBXwaCkjImZxunyQGKbO25nXVxi2XfhaTNgu8"
        }
        params = {"language": "pt-BR"}
        response = requests.get(url, headers=headers, params=params).json()
        # formatando a data pois é só um filme
        if 'release_date' in response and response['release_date']:
            response['data_formatada'] = self.datetimeformat(response['release_date'])
        return self.to_json(response)
        

    def to_json(self, response: dict[str,str]): 
        try:
            with open('filmes.json', 'w', encoding='utf-8') as file:
                json.dump(response, file, indent=4, ensure_ascii=False)

            with open('filmes.json', 'r', encoding='utf-8') as file:
                response_text = json.load(file)    
            return response_text    

        except Exception as e:
            return e

if __name__ =="__main__": 
    MovieAPI().movie_list()
