import googletrans
translator = googletrans.Translator() 
from flask import Flask, render_template, request
import Main

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return render_template('home.html', welcome='welcome.png')

@app.route('/', methods=['post'])
def get():
    keyWord1 = request.form['keyword1']
    keyWord2 = request.form['keyword2']
    enkeyWord1 = translator.translate(keyWord1, dest='en')
    enkeyWord2 = translator.translate(keyWord2, dest='en')
    resultKeyword = [keyWord1, enkeyWord1.text, keyWord2, enkeyWord2.text]
    Main.Main(resultKeyword)
    return render_template('home.html', trend='trend.png', word0='0.png',
                                                           word1='1.png',
                                                           word2='2.png',
                                                           word3='3.png',
                                                           word4='4.png',
                                                           word5='5.png',
                                                           word6='6.png',
                                                           word7='7.png')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)