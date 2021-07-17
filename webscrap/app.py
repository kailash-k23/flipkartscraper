from email.mime import text
from flask import Flask, render_template, request, redirect
from scrape import return_result

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def basic():
    if request.method == 'GET':
        return render_template('main.html', text = 'Enter Product to get details')
    else:
        product_name = request.form['product']
        email_id = request.form['email']
        return_result(product_name, email_id)
        return render_template('main.html', text = "Check Mail!")


if __name__ == "__main__":
    app.run(debug=True)



