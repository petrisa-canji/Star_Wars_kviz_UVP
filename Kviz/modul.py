import json
import random

class Model():
    def __init__(self, data_path="vprasanja.json"):
        self.update_seznam_vprasanj(data_path="vprasanja.json")
        self.reset_odgovorov()

    def update_seznam_vprasanj(self, data_path="vprasanja.json", st_vprasanj=10):
        with open(data_path, 'r') as datoteka:
            vprasanja = json.load(datoteka)
            seznam = [vprasanja[random.randint(0, len(vprasanja)-1)] for i in range(10)]
            self.seznam_vprasanj = seznam
    
    def reset_odgovorov(self):
        self.seznam_odgovorov = []

def mejava_osebnost_junak(seznam, data_path='Star_Wars_Junaki.json'):
    with open(data_path, 'r') as datoteka:
        junaki = json.load(datoteka)
        slovar = dict([[i['MBTI'], i['ime']] for i in junaki])

        novi_seznam = [[slovar[i[0]], i[1]] for i in seznam]

        return novi_seznam


