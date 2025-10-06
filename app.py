#Importe de un paquete llamado flask, una clase llamada Flask
from flask import Flask, render_template
from entities.animal import Animal
from entities.comida import Comida

#Estamos creando un objeto a partir del constructor de la clase Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animals')
def animals():
    animals = Animal.get_list()
    return render_template('animals.html', animals = animals)

@app.route('/restaurant')
def restaurant():
    platillos = Comida.get_list()
    return render_template('restaurant.html', platillos = platillos)

if __name__ == "__main__":
    app.run()