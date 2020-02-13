from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def Egor():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def prom():
    return """Человечество вырастает из детства.<br>
              Человечеству мала одна планета.<br>
              Мы сделаем обитаемыми безжизненные пока планеты.<br>
              И начнем с Марса!<br>
              Присоединяйся!"""


@app.route('/image sample')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <title>Жди нас, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                </html>""" \
           '''<img src="{}" alt="здесь должна была быть картинка, 
           но не нашлась">'''.format(url_for('static', filename='img/MARS.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
