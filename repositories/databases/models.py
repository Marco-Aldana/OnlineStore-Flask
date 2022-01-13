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
                    Column("phone", NVARCHAR(10), nullable=True),
                    Column("country", Text, nullable=True, default=""),
                    Column("city", Text, nullable=True, default=""),
                    Column("postal_code", Text, nullable=True, default=""),
                    Column("street", Text, nullable=True, default=""),
                    Column("number", Text, nullable=True, default=""),
                    Column("is_active", Boolean, default=True, nullable=False),
                    Column("is_validated", Boolean, default=False, nullable=False),
                    Column("created_at", DATETIME, default=datetime.datetime.now(), nullable=False),
                    )

products_table = Table("products", metadata,
                       Column("id", Integer, primary_key=True, autoincrement=True),
                       Column("title", String(50), nullable=False),
                       Column("description", String(50), nullable=False),
                       Column("image", String(50), nullable=False),
                       Column("category", String(50), nullable=False),
                       Column("quantity", Integer, default=0, nullable=False),
                       Column("price", Integer, default=0, nullable=False),
                       )

cart_table = Table("carts", metadata,
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

audits_table = Table("AUDITS", metadata,
                     Column("IdAudit", Integer, primary_key=True, autoincrement=True),
                     Column("Request", Text, nullable=False),
                     Column("Time", DateTime, nullable=False),
                     Column("IdSession", Text, nullable=False),
                     Column("Status", Text, nullable=False)
                     )
