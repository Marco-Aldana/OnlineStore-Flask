"""
Create structures and initialize databases using SQLAlchemy libraries
"""
# ---------------------------------------------------------------------------------------------------------------Imports
import datetime

from project import db


# -----------------------------------------------------------------------Declaring tables details for Database structure
class BaseTable:
    @classmethod
    def get_attributes(cls):
        attr = UsersTable.__dict__.keys()
        attributes_list = [a for a in attr if a[0] != '_' and a != 'id']
        return attributes_list


class ProductsTable(db.Model, BaseTable):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, title, price, description='No description', image='No image', category='No category',
                 quantity=0):
        self.title = title
        self.price = price
        self.description = description
        self.image = image
        self.category = category
        self.quantity = quantity

    def __repr__(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'category': self.category,
            'quantity': self.quantity
        }


class UsersTable(db.Model, BaseTable):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_validated = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.datetime.now(), nullable=False)

    def __init__(self, username, full_name, email, password, image="no image", is_active=True, is_validated=False,
                 created_at=datetime.datetime.now()):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.password = password
        self.image = image
        self.is_active = is_active
        self.is_validated = is_validated
        self.created_at = created_at

    def __repr__(self):
        return {
            'id': self.id,
            'username': self.username,
            'full_name': self.full_name,
            'email': self.email,
            'image': self.image,
        }


class ContactsTable(db.Model, BaseTable):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.ForeignKey('users.id'), nullable=False)
    phone = db.Column(db.NVARCHAR(10), nullable=True)
    country = db.Column(db.Text, nullable=True, default="")
    city = db.Column(db.Text, nullable=True, default="")
    zipcode = db.Column(db.Text, nullable=True, default="")
    street = db.Column(db.Text, nullable=True, default="")
    number = db.Column(db.Text, nullable=True, default="")

    def __init__(self, id_user, phone=None, country=None, city=None, zipcode=None, street=None, number=None):
        self.id_user = id_user
        self.phone = phone
        self.country = country
        self.city = city
        self.zipcode = zipcode
        self.street = street
        self.number = number

    def __repr__(self):
        return {
            'id': self.id,
            'id_user': self.id_user,
            'phone': self.phone,
            'country': self.country,
            'city': self.city,
            'zipcode': self.zipcode,
            'street': self.street,
            'number': self.number
        }


class CategoriesProductsTable(db.Model, BaseTable):
    __tablename__ = "categories_products"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.ForeignKey('categories.id'))
    product = db.Column(db.ForeignKey('products.id'))

    def __init__(self, category, product):
        self.category = category
        self.product = product

    def __repr__(self):
        return {
            'id': self.id,
            'category': self.category,
            'product': self.product
        }


class CategoriesTable(db.Model, BaseTable):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }


class CartsTable(db.Model, BaseTable):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, date):
        self.user_id = user_id
        self.date = date

    def __repr__(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'date': self.date,
        }


class ToSellTable(db.Model, BaseTable):
    __tablename__ = "to_sell"
    id = db.Column(db.Integer, primary_key=True)
    id_cart = db.Column(db.ForeignKey('carts.id'), nullable=False)
    id_product = db.Column(db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, id_cart, id_product, quantity):
        self.id_cart = id_cart
        self.id_product = id_product
        self.quantity = quantity

    def __repr__(self):
        return {
            'id': self.id,
            'id_cart': self.id_cart,
            'id_product': self.id_product,
            'quantity': self.quantity,
        }


class AuditsTable(db.Model, BaseTable):
    __tablename__ = "audits"
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    id_session = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)

    def __init__(self, request, time, id_session, status):
        self.request = request
        self.time = time
        self.id_session = id_session
        self.status = status

    def __repr__(self):
        return {
            'id': self.id,
            'request': self.request,
            'time': self.time,
            'id_session': self.id_session,
            'status': self.status,
        }
