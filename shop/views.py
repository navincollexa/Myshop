from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from shop.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse



def user_login(request):

    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('product_list'))
        else:
            context["error"] = "Please enter correct username and password!!"
            return render(request, "auth/login.html", context)

    else:
        return render(request, "auth/login.html", context)

@login_required(login_url="/login/")
def user_success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

def user_logout(request):
    
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
def product_list(request, category_slug=None):
	
    users= User.objects.all()
   
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'user': users, 'category': category,
                                                      'categories': categories,
                                                      'products': products})

 
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
