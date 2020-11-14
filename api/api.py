from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

mysql = MySQL()

#Configuração do banco de dados MySQL
app.config['MYSQL_DATABASE_USER'] = 'fabio'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fd'
app.config['MYSQL_DATABASE_DB'] = 'Communication'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

class CreateEvent(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, help='title to create event')
            parser.add_argument('description', type=str, help='title to create event')
            parser.add_argument('date', type=str, help='title to create event')
            parser.add_argument('time', type=str, help='title to create event')
            parser.add_argument('email', type=str, help='title to create event')
            parser.add_argument('sms', type=str, help='title to create event')
            parser.add_argument('push', type=str, help='title to create event')
            parser.add_argument('whatsapp', type=str, help='title to create event')


        except Exception as e:
            return {'error': str(e)}
        return {'status': 'success'}


class GetEvent(Resource):
    def get(self):
        try:
            print("get")

        except Exception as e:
            return {'error': str(e)}

#Especificação dos endereços/rotas que serão acessados
@app.route('/CreateEvent')
def CreateUser(name=None):
    return render_template('form1.html', name=name)

@app.route('/GetEvent')
def GetUser(name=None):
    return render_template('form2.html', name=name)

if __name__ == '__main__':
    #Biblioteca Waitress como alternativa ao server de desenvolvimento built-in do Flask
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)
