#Importe de un paquete llamado flask, una clase llamada Flask
from flask import Flask, render_template
from entities.animal import Animal
from entities.comida import Comida
from entities.palindrome import Palindrome
from entities.suerte import Suerte
from flask import request

#Estamos creando un objeto a partir del constructor de la clase Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animals')
def animals():
    animals = Animal.get_list()
    return render_template('animals.html', animals = animals)

#Metodos permitidos GET y POST en la ruta /palindrome
@app.route('/palindrome' , methods=['GET', 'POST'])
def palindrome():
    if request.method == 'POST':
        #La comillas bacias, es por si no encuentra input_phrase ingresa un valor vacio
        input_phrase = request.form.get('input_phrase', '')

        p = Palindrome(input_phrase)
        result = p.is_palindrome()
        return render_template('result.html', result=result)
    return render_template('palindrome.html')

@app.route('/sorteo', methods=['GET', 'POST'])
def sorteo():
    if request.method == 'POST':
        input_number1 = request.form.get('input_number1', '')
        input_number2 = request.form.get('input_number2', '')
        input_number3 = request.form.get('input_number3', '')

        s = Suerte(input_number1, input_number2, input_number3)
        ganador = s.ganador() 
        return render_template('ganador.html', ganador=ganador)
    return render_template('sorteo.html')


@app.route('/restaurant')
def restaurant():
    platillos = Comida.get_list()
    return render_template('restaurant.html', platillos = platillos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5150)