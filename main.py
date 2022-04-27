from flask import request, render_template
from duombaze import db, Query, app


@app.route('/login', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        vardas = request.form['vardas']
        email = request.form['email']
        message = request.form['message']
        query = Query(vardas, email, message)
        db.session.add(query)
        db.session.commit()
        psl = render_template("greetings.html", html_vardas=vardas)
    else:
        psl = render_template("login.html")
    return psl


if __name__ == "__main__":
    app.run()
