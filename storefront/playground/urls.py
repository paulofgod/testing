from argparse import Namespace
from pathlib import Path
from django.urls import path, include
from django.views.generic import TemplateView
from carts.views import cart_home
from products.views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    ProductDetailSlugView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
)
from .views import (
    register_page,
    say_hello,
    about_page,
    contact_page,
    login_page,
    register_page,
)

# URLConf
urlpatterns = [
    path("hello/", say_hello, name='home'),
    path("about/", about_page, name='about'),
    path("contact/", contact_page, name= 'Contact'),
    path("login/", login_page, name='login'),
    path("cart/", include("carts.urls")),
    path("cart/", cart_home, name='cart'),
    path("products-fbv/", product_list_view),
    path("featured/", ProductFeaturedListView.as_view()),
    path("featured/<int:pk>/", ProductFeaturedDetailView.as_view()),
    path("products/", ProductListView.as_view(), name='products'),
    path("products-fbv/<int:pk>/", product_detail_view),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<slug:slug>/", ProductDetailSlugView.as_view(), name="detail"),
    path("register/", register_page, name='register'),
    path("bootstrap/", TemplateView.as_view(template_name="Bootstrap/example.html")),

    path("search/", include("search.urls")),
]