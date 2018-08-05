import pandas as pd
import json
from jsonencoder import ComplexEncoder
from pymongo import MongoClient
from card import Card

# Lendo o CSV e transformando-o em um dicionário
my_array = pd.DataFrame(pd.read_csv("./files/Card.csv"))
my_array = my_array.to_dict(orient='records')

# conectando no BD
client = MongoClient('localhost', 27017)
db = client['cards']
card_collection = db['card']

# Inserindo os registros no BD
for data in my_array:
    newCard = Card().dictToCard(data)
    jsonCard = json.dumps(newCard.reprJSON(), cls=ComplexEncoder)
    card_collection.insert_one(json.loads(jsonCard))

