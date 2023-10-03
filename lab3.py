from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    if user == '':
        errors['user'] = 'Заполните поле!'

    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    # order = ''
    # drink = request.args.get('drink')

    # if drink == 'coffee':
    #     order = 'Кофе'
    # elif drink == 'black-tea':
    #     order = 'Черный чай'
    # else:
    #     order = 'Зеленый чай'

    # if request.args.get('milk') == 'on':
    #     order = 'с молоком'
    # if request.args.get('sugar') == 'on':
    #     order = 'с сахаром'

    
    return render_template('order.html', order=order)


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price = price)

@lab3.route('/lab3/success')
def success():
    return render_template('success.html')