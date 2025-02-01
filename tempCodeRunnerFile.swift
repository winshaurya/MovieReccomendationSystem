

import pickle as pp 
import pandas as pd
import requests



url = "https://api.themoviedb.org/3/find/external_id?external_source=5656"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NDE5ZmUzZjBmY2JiYWMxMDBhYTQyYjEwZTVkNjFkNyIsIm5iZiI6MTczNzM1Mjg3OC40NzEsInN1YiI6IjY3OGRlNmFlZGNiNmU4MzlmMzQzMDkxZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XuB_SgJkRD1ecJiuePuF_R-DGlVrSovoty4y2NasolE"
}

response = requests.get(url, headers=headers)

print(response.text)