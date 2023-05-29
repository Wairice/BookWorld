from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_home, name='books_home'),
    path("<int:pk>", views.BooksDetailView.as_view(), name='books-detail'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>', views.remove_from_cart, name='remove_from_cart '),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
]
