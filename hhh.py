from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


profs = ['инженер-исполнитель', "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
         "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог",
         "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
@app.route('/list_prof/<list>')
def profs_list(list):
    return render_template('list_prof.html', list=list, profs=profs)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
