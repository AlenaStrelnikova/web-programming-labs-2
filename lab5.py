from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, Blueprint, render_template, request, session
import psycopg2

lab5 = Blueprint('lab5', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='knowledge_base_for_alena',
        user='alena_knowledge_base',
        password='12345')

    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route('/lab5/')
def main():
    visibleUser = "Anon"
    return render_template("lab5.html", username=visibleUser)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"


@lab5.route('/lab5/users/')
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users;")

    users = cur.fetchall()

    dbClose(cur, conn)

    return render_template("users.html", users=users)



@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template("register.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)


    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
   
        dbClose(cur, conn)

        return render_template("register.html", errors=errors)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');")

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login_lab5")



@lab5.route('/lab5/login_lab5', methods=["GET", "POST"])
def loginPage():
    errors = []


    if request.method == "GET":
        return render_template("login_lab5.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("login_lab5.html", errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("login_lab5.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5/")

    else:
        errors.append("Неправильный логин или пароль!")
        return render_template("login_lab5.html", errors=errors)



@lab5.route('/lab5/new_article', methods=["GET", "POST"])
def createArticle():
    errors = []


    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html", errors=errors)

        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = requesst.form.get("title_article")

            if len(text_article) == 0:
                errors.append("Заполните текст")
                return render_template("new_article.html", errors=errors)

            if len(title) == 0:
                errors.append("Введите название")
                return render_template("new_article.html", errors=errors)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")

    return redirect("/lab5/login")


@lab5.route('/lab5/articles/<int:article_id>')
def getArticle(article_id):
    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute(f"SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"

        text = articleBody[1].splitlines()

        return render_template("article.html", article_text=text, article_title=articleBody[0], username=session.get('username'))


