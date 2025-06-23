# ✅ Fixed Flask Code for add_to_cart route

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pymysql


app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

USERNAME = 'admin'
PASSWORD = 'pass'

db = SQLAlchemy(app)

# MODELS
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))
    image = db.Column(db.String(100))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    status = db.Column(db.String(50))

with app.app_context():
    db.create_all()

# AUTH
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = "Invalid credentials!"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

def render_protected(template, **kwargs):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template(template, **kwargs)

# ROUTES
@app.route('/')
def home():
    return render_protected('home.html')

@app.route('/shop')
def shop():
    items = ShopItem.query.all()
    return render_template('shop.html', flowers=items)

@app.route('/add_to_cart/<int:flower_id>', methods=['POST'])
def add_to_cart(flower_id):
    flower = Flower.query.filter_by(id=flower_id).first()

    if flower is None:
        flash("Flower not found!", "error")
        return redirect(url_for('shop'))

    quantity = int(request.form.get('quantity', 1))

    cart_item = {
        'name': flower.name,
        'price': flower.price,
        'quantity': quantity
    }

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(cart_item)
    session.modified = True

    flash("Item added to cart!", "success")
    return redirect(url_for('shop'))


@app.route('/view_cart')
def view_cart():
    if 'cart' not in session:
        session['cart'] = []

    return render_template('view_cart.html', flowers=session['cart'])


@app.route('/shop/delete/<int:item_id>')
def delete_item(item_id):
    item = ShopItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('shop'))

@app.route('/populate_flowers')
def populate_flowers():
    db.session.query(ShopItem).delete()
    flowers = [
        ('Spider Chrysanthemum', 50, 'spider.jpg'),
        ('Pompon Chrysanthemum', 45, 'pompon.jpg'),
        ('Spoon Chrysanthemum', 55, 'spoon.jpg'),
        ('Quill Chrysanthemum', 60, 'quill.jpg'),
        ('Brush and Thistle Chrysanthemum', 50, 'brush.jpg'),
        ('Anemone Chrysanthemum', 65, 'anemone.jpg'),
        ('Single and Semi-Double Chrysanthemum', 40, 'single.jpg'),
        ('Intermediate Incurve Chrysanthemum', 70, 'intermediate.jpg'),
        ('Decorative Chrysanthemum', 75, 'decorative.jpg'),
        ('Regular Incurve Chrysanthemum', 80, 'regular.jpg'),
        ('Reflex Chrysanthemum', 65, 'reflex.jpg'),
        ('Irregular Incurve Chrysanthemum', 85, 'irregular.jpg'),
        ('Unclassified', 30, 'unclassified.jpg')
    ]

    for name, price, image in flowers:
        db.session.add(ShopItem(name=name, price=price, image=image))
    db.session.commit()
    return redirect(url_for('shop'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
