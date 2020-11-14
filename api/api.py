from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()

#Configuração do banco de dados MySQL
app.config['MYSQL_DATABASE_USER'] = 'fabio'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fd'
app.config['MYSQL_DATABASE_DB'] = 'Communication'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#inicialização do Mysql, do conector e do cursor que acessará as posições para realizar as operações
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

class CreateEvent(Resource):
    def post(self):
        try:
            #Acessa os identificadores da página html e adiciona uma a uma lista de argumentos
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, help='title to create event')
            parser.add_argument('description', type=str, help='title to create event')
            parser.add_argument('date', type=str, help='title to create event')
            parser.add_argument('time', type=str, help='title to create event')
            parser.add_argument('email', type=str, help='title to create event')
            parser.add_argument('sms', type=str, help='title to create event')
            parser.add_argument('push', type=str, help='title to create event')
            parser.add_argument('whatsapp', type=str, help='title to create event')
            args = parser.parse_args()

            #Separa os argumentos em variáveis, para poder inserir no banco de dados
            _eventTitle = args['title']
            _eventDesc = args['description']
            _eventDate = args['date']
            _eventTime = args['time']
            _eventMeans = ", "
            if(args['email']):
                _eventMeans = _eventMeans + (args['email'])
            if(args['sms']):
                _eventMeans = _eventMeans + ", " + (args['sms'])
            if(args['push']):
                _eventMeans = _eventMeans + ", " + (args['push'])
            if(args['whatsapp']):
                _eventMeans = _eventMeans + ", " + (args['whatsapp'])

            #Inserção dos dados no banco de dados
            cursor.execute("insert into tblCommunication (Title, Description, Date, Time, Means) values ('"+_eventTitle+"','"+_eventDesc+"','"+_eventDate+"','"+_eventTime+"','"+_eventMeans+"')")

            #Verificando se o cursos está em uma posição disponível do banco de dados
            data = cursor.fetchall()
            #Caso sim, faz o commit da inserção no banco de dados e retorna os argumentos em Json
            if (len(data) == 0):
                conn.commit()
                return args
            #Caso não, retorna o código de erro
            else:
                return {'StatusCode':'400', 'Message': 'Bad Request'}

        except Exception as e:
            return {'error': str(e)}

class GetEvent(Resource):
    def get(self):
        try:
            print("get")

        except Exception as e:
            return {'error': str(e)}

#Especificação dos endereços/rotas que serão acessados
api.add_resource(CreateEvent, '/CreateEvent')
api.add_resource(GetEvent, '/GetEvent')

@app.route('/CreateEvent', methods=['GET', 'POST'])
def CreateEvent(name=None):
    return render_template('form1.html', name=name)

@app.route('/GetEvent')
def GetEvent(name=None):
    return render_template('form2.html', name=name)

if __name__ == '__main__':
    #Biblioteca Waitress como alternativa ao server de desenvolvimento built-in do Flask
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)
#    app.run(debug=True)
