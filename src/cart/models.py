from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.
#add functionality to be able to change its quantity

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    @classmethod
    def get_cart(cls, request):
        if 'cart_id' in request.session:
            return cls.objects.get(id=request.session['cart_id'])
        else:
            return cls.get_new_cart(request)

    @classmethod
    def get_new_cart(cls, request):
        cart = cls()
        cart.save()
        request.session['cart_id'] = cart.id
        return cart

    def get_items(self):
        return self.cart_items.prefetch_related('product').all()

    def get_items_count(self):
        return len(self.get_items())



class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.product.title + ' cart item from cart object ' + str(self.cart.id)

    def find_total_cost(self):
        current_price = self.product.current_price
        tax = 1.12
        self.total_cost = self.quantity * current_price * tax
        return self.total_cost

    def update_quantity(self, quantity):
        self.update(quantity=quantity)



class CheckoutDetails(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, related_name='checkout_details', null=True, on_delete=models.SET_NULL)
    name_of_receiver = models.CharField(max_length=100)
    main_address = models.CharField(max_length=200)
    secondary_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=12)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return  'products to ' + self.main_address + ' for ' + self.name_of_receiver
    
