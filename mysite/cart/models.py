from django.db import models
from ..accounts.models import Account
from ..store.models import Product, Variation
# Create your models here.

class Cart(models.Model): # mo ta gio hang cua nguoi dung
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.cart_id

class CartItem(models.Model): # tuong ung vs cac muc trong gop hang
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank= True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __unicode__(self):
        return self.product