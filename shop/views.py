from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def globalfunction(request):
    data = category.objects.all()
    if request.user.is_authenticated:
        cartcount = cart.objects.filter(user=request.user).count()
        wishlistcount = wishlist.objects.filter(user=request.user).count()
        context = {
            'data': data,
            'cartcount': cartcount,
            'wishlistcount': wishlistcount,
        }
    else:
        context = {
            'data': data,
        }
    return context

def home(request):
    trending_product = product.objects.filter(trending=1)
    context = {
        'trending_product': trending_product,
    }
    return render(request, 'dashboared.html', context)

def Category(request, slug):
    if( category.objects.filter( slug=slug ) ):
        products = product.objects.filter(category__slug=slug)
        category_name = category.objects.filter(slug=slug).first()
        context = {
            'products': products,
            'category_name': category_name,
        }
        return render(request, 'category.html', context)

def productdetail(request, pk):
    products = product.objects.get(id=pk)
    context = {
        'products': products,
    }
    return render(request, 'productview.html', context)

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "regestrated successfully")
            return redirect("login")
    context = {
        'form': form,
    }
    return render(request, "register.html", context)

def signin(request):

    if request.method == 'POST':
        name = request.POST.get("username")
        passwd = request.POST.get("password")

        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "invalid username or password")
            return redirect('login')
    return render(request, "login.html")

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged out successfully")
        return redirect('home')

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = product.objects.get(id=prod_id)
            if(product_check):
                if(cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "product already in cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "product added successfully"})
                    else:
                        return JsonResponse({'status': "only " + str(product_check.quantity) + "quantity avalaible"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "login to continue"})
    return redirect('home')

def viewcart(request):
    carts = cart.objects.filter(user=request.user)
    context = {
        'carts': carts,
    }
    return render(request, "cart.html", context)

def deletecart(request, pk):
    cartitem = cart.objects.get(product__id=pk, user=request.user)
    cartitem.delete()
    return redirect('cart')

@login_required(login_url='login')
def addtowishlist(request, pk):
    if request.user.is_authenticated:
        product_check = product.objects.get(id=pk)
        if (product_check):
            if (wishlist.objects.filter(user=request.user.id, product_id=pk)):
                messages.success(request, "the item is already in wishlist")
                return redirect('home')
            else:
                wishlist.objects.create(user=request.user, product_id=pk)
                messages.success(request, "added to wishlist successfully")
                return redirect('home')
        else:
            messages.error(request,"no such product found")
            return redirect('home')
    else:
        messages.error(request,"login to continue")
        return redirect('login')

def viewwishlist(request):
    carts = wishlist.objects.filter(user=request.user)
    context = {
        'carts': carts,
    }
    return render(request, "viewwishlist.html", context)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(descreption__icontains=q) | Q(name__icontains=q))
        products = product.objects.filter(multiple_q).order_by('-id')
        page_num = request.GET.get("page")
        paginator = Paginator(products, 3)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {
            'q': q,
            'products': products,
        }
        return render(request, 'search.html', context)
    else:
        messages.error(request, "there is no product!")
        return render(request, 'search.html', {})



