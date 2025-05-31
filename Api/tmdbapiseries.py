import requests
import json

class SeriesAPI:
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZjFlOTkxNzU1ZjgxNzU0MzAzM2ZkYzQ0MWYyNmNhZCIsIm5iZiI6MTc0NzQ5MjcyOC44Miwic3ViIjoiNjgyODlmNzhlMjU3NDZlODY1ZjU1Mzc1Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.jpdKsUZBXwaCkjImZxunyQGKbO25nXVxi2XfhaTNgu8"
      }

    def series_list(self, page:int=1):
        url = f"https://api.themoviedb.org/3/tv/popular?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)
    
    def series_bem_avaliadas(self,page:int=1):
        url = f"https://api.themoviedb.org/3/tv/top_rated?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)
    
    def series_populares_tmdb(self,page:int=1):
        url = f"https://api.themoviedb.org/3/trending/tv/day?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)

    def series_exibidas_hj(self, page:int=1):
        url = f"https://api.themoviedb.org/3/tv/airing_today?language=pt-BR&page={page}"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)



#essa função vai executar sempre e criar o arquivo 
#     
    def to_json(self, response: dict[str,str]): 
        try:
            with open('series.json','w') as file: #criando o arquivo .json onde ficara os filmes
                json.dump(response,file,indent=4)

            with open('series.json', 'r') as file:
                response_text = json.load(file)    
            return response_text    

        except Exception as e:
            return e

if __name__ =="__main__": 
   SeriesAPI().series_list()
