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
    return render(request, 'app/addtocart.html')


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
    return render(request, 'app/orders.html')


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
    return render(request, 'app/checkout.html')
