from flask import Blueprint, render_template, abort,  request

lab9 = Blueprint ("lab9", __name__)


@lab9.route('/lab9/')
def main ():
    return render_template ('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error404.html'), 404


@lab9.app_errorhandler(500)
def server_error(e):
    return render_template('lab9/error500.html'), 500


@lab9.route('/lab9/500')
def error_500():
    abort(500)


@lab9.route('/lab9/card')
def card ():
    errors = {}

    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    sex = request.args.get('sex')
    happy = "Будь счастлив в Новом Году!" if sex == "man" else "Будь счастлива в Новом Году!"

    if name1 == '':
        errors['name'] = 'Заполните поле!'
        
    if name2 == '':
        errors['name'] = 'Заполните поле!'

    return render_template('lab9/card.html', name1=name1, name2=name2, sex=sex, happy=happy, errors=errors)