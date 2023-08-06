from flask import Flask, render_template, request
import requests

api_key = "FIXER.IO API KEY"

url = "http://data.fixer.io/api/latest?access_key=" + api_key
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")

        amount = request.form.get("amount")
        response = requests.get(url)

        data = response.json()

        firstValue = data["rates"][firstCurrency]
        secondValue = data["rates"][secondCurrency]

        result = (secondValue / firstValue) * float(amount)

        info = dict()
        info["firstCurrency"] = firstCurrency
        info["secondCurrency"] = secondCurrency
        info["amount"] = amount
        info["result"] = result

        return render_template("index.html", info = info)
    
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)