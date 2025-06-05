import requests
import json

API_KEY = 'bf1e991755f817543033fdc441f26cad'
BASE_URL = 'https://api.themoviedb.org/3'

class Categoria:
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZjFlOTkxNzU1ZjgxNzU0MzAzM2ZkYzQ0MWYyNmNhZCIsIm5iZiI6MTc0NzQ5MjcyOC44Miwic3ViIjoiNjgyODlmNzhlMjU3NDZlODY1ZjU1Mzc1Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.jpdKsUZBXwaCkjImZxunyQGKbO25nXVxi2XfhaTNgu8"
      }


    def obter_generos(self):
        url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-br"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)

    def obter_generos_tv(self):
        url = "https://api.themoviedb.org/3/genre/tv/list?language=pt-br"
        response = requests.get(url, headers=self.headers).json()
        return self.to_json(response)


    def to_json(self, response: dict[str,str]): 
        try:
            with open('categoria.json', 'w', encoding='utf-8') as file:
                json.dump(response, file, indent=4, ensure_ascii=False)

            with open('categoria.json', 'r', encoding='utf-8') as file:
                response_text = json.load(file)    
            return response_text    

        except Exception as e:
            return e


if __name__ =="__main__": 
    MovieCategoria().obter_generos()
