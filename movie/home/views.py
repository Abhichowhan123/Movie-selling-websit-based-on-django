from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib.auth.hashers import make_password ,check_password


# Create your views here.
def index(request):
    if request.method == "POST":
        product_id = request.POST.get("product")  #(name= product) in index.html addtocart name
        # print(product_id)
        cart_item = request.session.get("cart_item")
        if cart_item:
            quantity = cart_item.get(product_id)
            if quantity:                                # if product is already in cart then increment the quantity
                cart_item[product_id] = quantity
            else:
                cart_item[product_id] = 1
        else:
            cart_item = {}
            cart_item[product_id] = 1
        request.session["cart_item"] = cart_item
        print(request.session["cart_item"])
        return redirect('index')

    elif request.method == "GET":
        category1 = Category.objects.all()
        categoryID = request.GET.get("category")
        if categoryID:
            product1 = Product.objects.filter(sub_category = categoryID)
        else:
            product1 = Product.objects.all()
        context = {

            "category2":category1,
            "product2":product1
        }
        # print(request.session.get("customer_id"))
        # print(request.session.get("customer_email"))
        return render(request,"store/index.html",context)


#logout
def logout(request):
    request.session.clear()
    return redirect('login')


#login
def login(request):
    if request.method == "GET":
        return render(request, "store/login.html")
    elif request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        customer_login = Customer.get_customer_by_email(Email)
        error_message= None
        if customer_login:
            temp = Customer.password_checking(Password,customer_login.password)
            if temp:
                request.session["customer_id"] = customer_login.id
                return redirect("index")
            else:
                error_message = "Email or Password is invalid"
        else:
            error_message = "Email or Password is invalid"

        return render(request,"store/login.html",{"error":error_message})


# signup
def signup(request):
    if request.method == "GET":
        return render(request,"store/signup.html")
    else:
        First_name = request.POST.get("firstname")
        Last_name = request.POST.get("lastname")
        Phone = request.POST.get("phone")
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        Confirm_Password = request.POST.get("confirmpassword")
        value =  {
            "f_name" : First_name,
            "l_name" : Last_name,
            "p_no" : Phone,
            "E_mail" : Email
        }
# customer_signup object
        customer_signup = Customer(first_name=First_name,
                                   last_name=Last_name,
                                   phone=Phone,
                                   email=Email,
                                   password=Password)
# validation
        error_message = None

        if not First_name:
            error_message = "First name Required"
        elif not Last_name:
            error_message = "Last name Required"
        elif not Phone:
            error_message = "Phone Required"
        elif not len(Phone)==10:
            error_message = "Phone Number must be 10 char Long"
        elif not Email:
            error_message = "Email Required"
        elif not Password:
            error_message = "Password Required"
        elif not Confirm_Password:
            error_message = "Confirm Password Required"
        elif Password != Confirm_Password:
            error_message = "Not Matching"
        elif customer_signup.isExists():
            error_message = "Email Already Exists"

# saving customer data
        if not error_message:
            customer_signup.password  = make_password(customer_signup.password)
            customer_signup.save()
            return render(request,"store/index.html")
        else:
            data = {
                "error" : error_message,
                "Value" : value
            }
            return render(request,"store/signup.html", data)


#account
def account(request):
    return render(request,"store/account.html")

#cart
def cart(request):
    if request.method=="GET":
        ids = list(request.session.get("cart_item").keys())
        all_products = Product.product_ids_for_cart(ids)
        all_Price = Product.price_all_product(all_products)
        print(all_Price)
        context = {
            "all_ids": all_products,
            "all_prices":all_Price
        }
        return render(request,"store/cart.html",context)
    else:
        render(request,"store/cart.html")

#view
def product_view(request):
    if request.method == "POST":
        product_v = request.POST.get("product_view")
        print(product_v)
        pro_detail= Product.product_detail(product_v)


    return render(request,"store/view.html",{"product_detail_view":pro_detail})


#about
def about(request):
    return render(request,"store/about.html")