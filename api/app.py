from flask import Flask, render_template

app = Flask(__name__)

#Retorna a renderização da página armazenada no diretório templates, conforme o endereço
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

if __name__ == '__main__':
    app.run()
