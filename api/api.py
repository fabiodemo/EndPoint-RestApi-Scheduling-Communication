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
            args = parser.parse_args()

            _eventTitle = args['title']
            _eventDesc = args['description']
            _eventDate = args['date']
            _eventTime = args['time']
            _eventMeans = args['email']

            cursor.execute("insert into tblCommunication (Title, Description) values ('"+_eventTitle+"','"+_eventDesc+"')")

            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return jsonify(args)
            else:
                return {'StatusCode':'400','Bad Request'}

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
