from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <ol>
            <li><a href="/lab1">Первая лабораторная</a></li>
        </ol>
        
        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Стрельникова Алёна Александровна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <div>Flask — фреймворк для создания веб-приложений на языке 
        программирования Python, использующий набор инструментов Werkzeug,
        а также шаблонизатор Jinja2. Относится к категории так называемых
        микрофреймворков — минималистичных каркасов веб-приложений, 
        cознательно предоставляющих лишь самые базовые возможности.</div>

        <a href="/menu">Меню</a>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="/lab1/student">/lab1/student - студент</a></li>
            <li><a href="/lab1/python">/lab1/python - питон</a></li>
            <li><a href="/lab1/sea">/lab1/sea - море</a></li>
        </ul>


        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <header>
                НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Дуб</h1>
        <img class='dub'src="''' + url_for('static', filename='oak.jpg') + '''">

        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <header>
                НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Студент:</h1>
        <div class='text'>Стрельникова Алена Александровна</div><br>
        <img class='logo_nstu' src="''' + url_for('static', filename='logo_nstu.png') + '''">

        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <header>
                НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Про язык программирования Python</h1>
        <div class='text'>Python — это язык программирования, который широко используется 
        в интернет-приложениях, разработке программного обеспечения, науке о данных и машинном 
        обучении (ML). Разработчики используют Python, потому что он эффективен, прост в изучении
        и работает на разных платформах. Программы на языке Python можно скачать бесплатно, они 
        совместимы со всеми типами систем и повышают скорость разработки.</div><br>

        <div class='text'>Язык Python имеет следующие преимущества:</div><br>

        <ul class='text'>
            <li>Разработчики могут легко читать и понимать программы на Python, поскольку язык имеет 
            базовый синтаксис, похожий на синтаксис английского. </li>
            <li>Python помогает разработчикам быть более продуктивными, поскольку они могут писать программы на Python, 
            используя меньше строк кода, чем в других языках.</li>
            <li>Python имеет большую стандартную библиотеку, содержащую многократно используемые коды практически для любой задачи. 
            В результате разработчикам не требуется писать код с нуля.</li>
            <li>Разработчики могут легко сочетать Python с другими популярными языками программирования: Java, C и C++.</li>
        </ul>
        <img class='python_pic' src="''' + url_for('static', filename='python_pic.jpeg') + '''">

        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/sea')
def sea():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <header>
                НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h2>А. С. Пушкин</h2>
        <h1>"Я помню море пред грозою"</h1>
        <div class='text'>Я помню море пред грозою:<br>
        Как я завидовал волнам,<br>
        Бегущим бурной чередою<br>
        С любовью лечь к ее ногам!</div><br>

        <div class='text'>Как я желал тогда с волнами<br>
        Коснуться милых ног устами!<br>
        Нет, никогда средь пылких дней<br>
        Кипящей младости моей<br>
        Я не желал с таким мученьем<br>
        Лобзать уста младых Армид,<br>
        Иль розы пламенных ланит,<br>
        Иль перси, полные томленьем;<br>
        Нет, никогда порыв страстей<br>
        Так не терзал души моей!</div><br>
        <img class='sea' src="''' + url_for('static', filename='sea.jpg') + '''">

        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Алёна Стрельникова'
    return render_template('example.html', name=name)