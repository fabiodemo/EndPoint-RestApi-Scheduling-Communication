from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
from datetime import datetime
import json

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
            #Acessa os identificadores da página html e adiciona uma a uma lista de argumentos e separa os argumentos em variáveis, para poder inserir no banco de dados.
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, help='title to create event')
            parser.add_argument('recipient', type=str, help='recipient of the event')
            parser.add_argument('description', type=str, help='description of the event')
            parser.add_argument('date', type=str, help='date of the event')
            parser.add_argument('time', type=str, help='time of the event')
            parser.add_argument('email', type=str, help='option of notification to the event')
            parser.add_argument('sms', type=str, help='option of notification to the event')
            parser.add_argument('push', type=str, help='option of notification to the event')
            parser.add_argument('whatsapp', type=str, help='option of notification to the event')
            args = parser.parse_args()
            _eventTitle = args['title']
            _eventRec = args['recipient']
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
            cursor.execute("insert into tblCommunication (Title, Recipient, Description, Date, Time, Means) values ('"+_eventTitle+"','"+_eventRec+"','"+_eventDesc+"','"+_eventDate+"','"+_eventTime+"','"+_eventMeans+"')")
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
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str, help='id to search for the event')
            parser.add_argument('title', type=str, help='title to search for the event')
            parser.add_argument('recipient', type=str, help='recipient of the event')
            parser.add_argument('date', type=str, help='date of the event')
            parser.add_argument('time', type=str, help='time of the event')
            args = parser.parse_args()
            _eventId = args['id']
            _eventTitle = args['title']
            _eventRec = args['recipient']
            _eventDate = args['date']
            _eventTime = args['time']

            #Interpretação do botão de busca um determinado agendamento
            if(request.form['submit'] == 'Buscar'):
                cursor.execute("SELECT * FROM tblCommunication WHERE Id = %s", (_eventId,))
                data = cursor.fetchall()
                #Tratamento dos resultados da busca, para retornar os dados da forma mais clara possível no json
                for row in data:
                    day = row[4].strftime("%d")
                    #Como no banco de dados a data está em formato yyyy-mm-dd, deve-se realizar a conversão para melhor interpretação
                    str_date = row[4].strftime("%d-%m-%Y")
                    str_hour = str(row[5])
                    means = row[6].lstrip(', ')
                    return jsonify(id=row[0], title=row[1], recipient=row[2], description = row[3], date=str_date, hour=str_hour, means=means)
            #return {'StatusCode':'200', 'Message': 'Buscar'}

            #Interpretação do botão para deletar determinado agendamento
            elif(request.form['submit'] == 'Deletar'):
                cursor.execute("DELETE FROM tblCommunication WHERE Id = %s AND Recipient = %s AND Date = %s AND Time = %s", (_eventId, _eventRec, _eventDate, _eventTime,))
                conn.commit()
                return {'StatusCode':'200', 'Message': 'OK'}

            else:
                return {'StatusCode':'202', 'Message': 'The request has been accepted for processing, but the processing has not been completed.'}

        except Exception as e:
            return {'error': str(e)}

#Especificação dos endereços/rotas que serão acessados
api.add_resource(CreateEvent, '/CreateEvent')
api.add_resource(GetEvent, '/GetEvent')
#Endereço para criação de um evento
@app.route('/CreateEvent', methods=['GET', 'POST'])
def CreateEvent(name=None):
    return render_template('form1.html', name=name)
#Endereço para consulta de um evento
@app.route('/GetEvent', methods=['GET', 'POST'])
def GetEvent(name=None):
    return render_template('form2.html', name=name)

if __name__ == '__main__':
    #Biblioteca Waitress, estabelece um servidor para fins de desenvolvimento
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)
#    server de desenvolvimento built-in do Flask
#    app.run(debug=True)
