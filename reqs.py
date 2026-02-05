# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()
# api=os.getenv("API_KEY")
# quote_uri="https://quotes-api-self.vercel.app/quote"
# class Req:
#     def __init__(self):
#         response=requests.get(url=quote_uri)
#         if response.status_code!=200:
#             self.error=response.raise_for_status()
#             data={'quote':"Technology is best when it brings people together",
#                   'author':"Matt Mullenweg"}
#         else:
#             data=response.json()
#         self.quote=data['quote']
#         self.author=data['author']
        

import requests
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("API_KEY")
quote_uri="https://api.api-ninjas.com/v2/randomquotes"

class Req:
    def __init__(self):
        try:
            response=requests.get(url,headers={"X-Api-Key":API_KEY})
            response.raise_for_status()

            data = response.json()

        except requests.exceptions.RequestException as e:
            print("Quote API failed:", e)

            # fallback quote
            data = {
                'quote': "Technology is best when it brings people together",
                'author': "Matt Mullenweg"
            }

        self.quote = data[0]['quote']
        self.author = data[0]['author']

        
