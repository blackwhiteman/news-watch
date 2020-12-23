from flask import Flask
from flask import render_template
from flask import redirect, request
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

"""@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")  
@app.route("/jinja")
def jinja():
    my_name="bob"
    langs = ["urdu", "arabic", "english", "turkish"]
    return render_template("jinja.html", my_name=my_name, langs=langs)"""

@app.route("/", methods=["GET", "POST"])
def sign_up():
    source = requests.get('https://www.bbc.co.uk/news').text
    soup = BeautifulSoup(source, 'html5lib')
    h3 = soup.find('body').find_all('h3')
    result = []
    if request.method == "POST":
        choose = request.form.get("choose")
        for i in h3:
            if choose in i.text:
                result.append(i.text)
        return render_template("index.html",**locals())

        return redirect(request.url)

    return render_template("index.html", **locals())


if __name__ == "__main__":
    app.run(debug=True)
