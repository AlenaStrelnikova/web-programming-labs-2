from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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

        <footer>
            &copy; Алёна Стрельникова, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""