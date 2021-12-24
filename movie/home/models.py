from django.contrib.auth.hashers import check_password
from django.db import models

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default="")
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE,null=False,default="")
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length= 200)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length= 800,null=True,default="")

    def __str__(self):
        return self.name

    @staticmethod
    def product_ids_for_cart(ids):
        return Product.objects.filter(id__in= ids)# ((id__in)) ka matlab (ids) mai jo list aayega wo sare product humko miljaye ga

    @staticmethod
    def price_all_product(all_products):
        sum = 0
        for p in all_products:
            sum += p.price
        return sum
    @staticmethod
    def product_detail(product_v):
        return Product.objects.filter(id = product_v)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField (max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name

    def isExists(self):
        if Customer.objects.filter(email =self.email):
            return True

    def get_customer_by_email(Email):
        try:
            return Customer.objects.get(email = Email)
        except:
            return False

    def password_checking(Password,password):
        if check_password(Password,password):
            return True

