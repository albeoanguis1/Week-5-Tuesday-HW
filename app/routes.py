from app import app
from flask import render_template, request
from app.forms import PokemonSearchForm
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/searchpokemon', methods = ["GET", "POST"])
def searchPokemon():
    form = PokemonSearchForm()
    my_dict = {}
    if request.method == 'POST':

        print('Post request made.')
        if form.validate():

            poke_name = form.name.data
            url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
            res = requests.get(url)
            if res.ok:
                data = res.json()
                my_dict = {
                    'Name': data['forms'][0]['name'].title(),
                    'Ability': data['abilities'][0]['ability']['name'].title(),
                    'PictureID': data['sprites']['front_shiny'],
                    'Attack': data['stats'][0]['base_stat'],
                    'HP': data['stats'][1]['base_stat'],
                    'Defense': data['stats'][2]['base_stat']
                }
                


    return render_template('searchpokemon.html', form = form, pokemon = my_dict)