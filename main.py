from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        aprobado = promedio >= 40 and asistencia >= 75

        return render_template('ejercicio1.html', promedio=promedio, aprobado=aprobado)
    else:
        return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [(nombre1, len(nombre1)), (nombre2, len(nombre2)), (nombre3, len(nombre3))]
        nombres.sort(key=lambda x: x[1], reverse=True)

        return render_template('ejercicio2.html', nombre=nombres[0][0], longitud=nombres[0][1])
    else:
        return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)