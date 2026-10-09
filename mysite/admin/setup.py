from fastapi import FastAPI
from sqladmin import Admin
from mysite.admin.views import UserAdmin, RefreshTokenAdmin
from mysite.database.db import engine


def setup_admin(mysite: FastAPI):
    admin = Admin(mysite, engine)
    admin.add_view(UserAdmin)
from mysite.database.db import engine
from mysite.admin.views import UserAdmin, ProductAdmin, OrderAdmin, RefreshTokenAdmin

def setup_admin(app: FastAPI):
    admin = Admin(app=app, engine=engine, title="Delivery Operator Admin")
    admin.add_view(UserAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(RefreshTokenAdmin)