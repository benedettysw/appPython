from flask import Flask , render_template

Myweb = Flask(__name__)

@Myweb.route('/')
def Inicio():
    return render_template('index.html')

@Myweb.route('/Menu')
def segunda():
    return render_template('index2.html')



if __name__ == '__main__':
    Myweb.run(debug=True)