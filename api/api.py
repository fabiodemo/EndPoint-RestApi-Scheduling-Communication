from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

class CreateEvent(Resource):
    def post(self):
        try:
            print("create")

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
