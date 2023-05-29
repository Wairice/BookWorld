from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, Bookks, CartItem
from django.db.models import Q


def books_home(request):
    genre = request.GET.get('genre')
    search_query = request.GET.get('search')
    books = Bookks.objects.order_by('-date')
    if genre:
        books = books.filter(genre=genre)
    if search_query:
        books = books.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
    return render(request, 'books/books_home.html', {'books': books})


class BooksDetailView(DetailView):
    model = Bookks
    template_name = 'books/books_view.html'
    context_object_name = 'books'


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'books/cart.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request, pk):
    book = get_object_or_404(Bookks, id=pk)
    cart, created = Cart.objects.get_or_create(user=request.user.pk)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return redirect('cart')


def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')
