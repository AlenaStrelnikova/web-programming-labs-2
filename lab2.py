from flask import Blueprint, render_template, app
lab2 = Blueprint('lab2', __name__)


@app.route('/lab2/example')
def example():
    name = 'Алёна Стрельникова' 
    labnumber = 'Лабораторная работа 2'
    group = 'ФБИ-14'
    kurs = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120}, 
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321}]
    books = [
        {'title': 'Улисс', 'author': 'Джеймс Дж.', 'genre': 'роман', 'pages': 1056 },
        {'title': 'Трилогия желания', 'author': 'Драйзер Т.', 'genre': 'роман', 'pages': 1152},
        {'title': 'Война и мир', 'author': 'Толстой Л.', 'genre': 'роман', 'pages': 1360},
        {'title': 'Сага о Форсайтах', 'author': 'Голсуорси Дж.', 'genre': 'роман', 'pages': 1376},
        {'title': 'Архипелаг ГУЛАГ', 'author': 'Солженицын А.', 'genre': 'художественно-историческое произведение', 'pages': 1424},
        {'title': 'Квинканкс', 'author': 'Палиссер Ч.', 'genre': 'роман', 'pages': 1472},
        {'title': 'Иосиф и его братья', 'author': 'Манн Т. ', 'genre': 'роман', 'pages': 1492},
        {'title': 'Человек без свойств', 'author': ' Музиль Р.', 'genre': 'роман', 'pages': 1774},
        {'title': 'В поисках утраченного времени', 'author': 'Пруст М.', 'genre': 'роман', 'pages': 3031},
        {'title': 'Моя борьба', 'author': 'Кнаусгор К.', 'genre': 'автобиография', 'pages': 3600}]
    return render_template('example.html', name=name, labnumber=labnumber, group=group, kurs=kurs, fruits=fruits, books=books)
    

@app.route('/lab2/')
def lab_2():
    return render_template('lab2.html')


@app.route('/lab2/dogs')
def show_dogs():
    return render_template('dogs.html')