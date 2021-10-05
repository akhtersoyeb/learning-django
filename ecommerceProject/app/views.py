from django.shortcuts import redirect, render

from .forms import CustomerRegistrationForm, CustomerProfileForm

from .models import Customer, Product, Cart, OrderPlaced

from django.views import View

# def home(request):
#  return render(request, 'app/home.html')

# HOME View


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')

        context = {
            'topwears': topwears,
            'bottomwears': bottomwears,
            'mobiles': mobiles
        }
        return render(request, 'app/home.html', context)

# def product_detail(request):
#  return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product
        }
        return render(request, 'app/productdetail.html', context)


def add_to_cart(request):
    user = request.user 
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(
        user=user , 
        product=product, 
    ).save() 
    return redirect('showcart')

def show_cart(request): 
    if request.user.is_authenticated: 
        user = request.user
        cart = Cart.objects.filter(user=user)
        print (cart)
        amount = 0.0 
        shipping_amount = 70.0 
        total_amount = 0.0
        if cart: 
            for p in cart: 
                tempamount = (p.quantity * p.product.discounted_price) 
                amount += tempamount
                total_amount = amount + shipping_amount
        print (total_amount)
        context = {
            "carts": cart , 
            "amount": amount, 
            "totalamount" : total_amount, 
            "shippingamount": shipping_amount, 
        }
        return render(request, 'app/addtocart.html', context)
    else: 
        return redirect('login')

def buy_now(request):
    return render(request, 'app/buynow.html')


# def profile(request):
#     return render(request, 'app/profile.html')


class ProfileView(View): 
    def get(self, request): 
        form = CustomerProfileForm() 
        context = {
            'form': form 
        }
        return render(request, 'app/profile.html', context)

    def post(self, request):  
        form = CustomerProfileForm(request.POST)
        if form.is_valid() : 
            user = self.request.user 
            # print (user.username)
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            new_customer = Customer(
                user=user ,
                name=name, 
                locality=locality, 
                city=city, 
                state=state, 
                zipcode=zipcode
            )
            new_customer.save() 
        return redirect('address')

            

def address(request):
    add = Customer.objects.filter(user=request.user)
    context = {
        'add': add
    }
    return render(request, 'app/address.html', context)


def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    context = {
        'order_placed': op
    }
    return render(request, 'app/orders.html', context)


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request, data=None): 
    if data == None: 
        mobiles = Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung': 
        mobiles = Product.objects.filter(category='M').filter(brand=data)

    context = {
        'mobiles': mobiles
    }
    return render(request, 'app/mobile.html', context)


# def login(request):
#     return render(request, 'app/login.html')


# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View): 
    def get(self, request): 
        form = CustomerRegistrationForm() 
        context = {
            'form': form 
        }
        return render(request, 'app/customerregistration.html', context)

    def post(self, request): 
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid() : 
            form.save() 
         
        return redirect('login')

# form base 
# class base

def checkout(request):
    user = request.user 
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    if cart_items : 
        for p in cart_items: 
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount 
            total_amount = amount + shipping_amount
    context = {
        'cart_items' : cart_items, 
        'add': add, 
        'totalamount': total_amount
    }
    return render(request, 'app/checkout.html', context)


def payment_done(request): 
    user = request.user 
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart : 
        OrderPlaced(
            user = user , 
            customer = customer, 
            product = c.product, 
            quantity = c.quantity
        ).save() 
        c.delete() 
    return redirect('orders')