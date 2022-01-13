"""
Create structures and initialize databases using SQLAlchemy libraries
"""
# ---------------------------------------------------------------------------------------------------------------Imports
import datetime

from sqlalchemy import Table, Column, MetaData, Integer, String, Text, DateTime, Boolean, DATETIME, NVARCHAR, ForeignKey

# ------------------------------------------------------------------------------------Initializing objects and variables
metadata = MetaData()

# -----------------------------------------------------------------------Declaring tables details for Database structure
users_table = Table("users", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("username", String(20), nullable=False),
                    Column("full_name", Text, nullable=False),
                    Column("email", Text, nullable=False),
                    Column("password", Text, nullable=False),
                    Column("image", Text, nullable=True),
                    Column("is_active", Boolean, default=True, nullable=False),
                    Column("is_validated", Boolean, default=False, nullable=False),
                    Column("created_at", DATETIME, default=datetime.datetime.now(), nullable=False),
                    )

contacts_table = Table("contacts", metadata,
                       Column("id", Integer, primary_key=True, autoincrement=True),
                       Column("id_user", ForeignKey('user.id'), nullable=False),
                       Column("phone", NVARCHAR(10), nullable=True),
                       Column("country", Text, nullable=True, default=""),
                       Column("city", Text, nullable=True, default=""),
                       Column("zipcode", Text, nullable=True, default=""),
                       Column("street", Text, nullable=True, default=""),
                       Column("number", Text, nullable=True, default=""),
                       )

products_table = Table("products", metadata,
                       Column("id", Integer, primary_key=True, autoincrement=True),
                       Column("title", String(50), nullable=False),
                       Column("price", Integer, default=0, nullable=False),
                       Column("description", Text, nullable=False),
                       Column("image", String(50), nullable=False),
                       Column("category", String(50), nullable=False),
                       Column("quantity", Integer, default=0, nullable=False),
                       )

categories_products_table = Table("categories_products", metadata,
                                  Column("id", Integer, primary_key=True, autoincrement=True),
                                  Column("category", ForeignKey('categories.id')),
                                  Column("product", ForeignKey('products.id'))
                                  )

categories_table = Table("categories", metadata,
                         Column("id", Integer, primary_key=True, autoincrement=True),
                         Column("title", String(50), nullable=False),
                         Column("description", Text, nullable=False),
                         )

carts_table = Table("carts", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("user_id", ForeignKey('users.id'), nullable=False),
                    Column("date", Text, nullable=False),
                    )

to_sell_table = Table("to_sell", metadata,
                      Column("id", Integer, primary_key=True, autoincrement=True),
                      Column("id_cart", ForeignKey('carts.id'), nullable=False),
                      Column("id_product", ForeignKey("products.id"), nullable=False),
                      Column("quantity", Integer, nullable=False),
                      )

audits_table = Table("audits", metadata,
                     Column("id_audit", Integer, primary_key=True, autoincrement=True),
                     Column("request", Text, nullable=False),
                     Column("time", DateTime, nullable=False),
                     Column("id_session", Text, nullable=False),
                     Column("status", Text, nullable=False)
                     )
