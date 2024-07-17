from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            return render_template('items.html', items=data['items'])
    except Exception:
        return render_template('items.html', items=None)


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id', type=int)
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")
    if id:
        data = [product for product in data if product['id'] == id]
        if not data:
            return render_template('product_display.html', error="Product not found")
    return render_template('product_display.html', products=data)

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
