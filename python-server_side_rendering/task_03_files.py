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
    id=request.args.get('id', type=int)
    try:
        products_found = []
        if source == 'json':
            with open('products.json', 'r') as f:
                data = json.load(f)
                return render_template('product_display.html', products=[product for product in data if (id and product['id'] == id or not id)] )
        elif source == 'csv':
            with open('products.csv', 'r') as f:
                data = csv.DictReader(f)
                for product in data:
                    if id and int(product['id']) == id:
                        products_found.append(product)
                    if not id:
                        products_found.append(product)
                return render_template('product_display.html', products=[product for product in data if (id and product['id'] == id or not id)] )
        elif source not in ['json', 'csv']:
            return render_template('product_display.html', error="Wrong source")

        if id and not products_found:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products_found)
    except Exception:
        return render_template('product_display.html', products=None)


    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
