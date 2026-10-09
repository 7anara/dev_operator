from sqladmin import ModelView
from mysite.database.models import UserProfile, Product, Order, RefreshToken


class UserAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.username, UserProfile.email, UserProfile.phone_number, UserProfile.registered_date]
    column_searchable_list = [UserProfile.username, UserProfile.email, UserProfile.phone_number]
    column_sortable_list = [UserProfile.id, UserProfile.username, UserProfile.registered_date]
    form_excluded_columns = [UserProfile.user_token]
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.category, Product.store, Product.product_name, Product.price, Product.created_date]
    column_searchable_list = [Product.category, Product.store, Product.product_name]
    column_sortable_list = [Product.id, Product.price, Product.created_date]
    name = "Product"
    name_plural = "Products"
    icon = "fa-solid fa-box"


class OrderAdmin(ModelView, model=Order):
    column_list = [Order.id, Order.product_id, Order.user_id, Order.status, Order.created_date]
    column_sortable_list = [Order.id, Order.status, Order.created_date]
    name = "Order"
    name_plural = "Orders"
    icon = "fa-solid fa-truck"


class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.user_id, RefreshToken.created_date]
    column_sortable_list = [RefreshToken.id, RefreshToken.created_date]
    form_excluded_columns = [RefreshToken.token_user]
    name = "Refresh Token"
    name_plural = "Refresh Tokens"
    icon = "fa-solid fa-key"
