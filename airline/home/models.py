from django.db import models
from matplotlib.style import available

# Create your models here.
    # buh baraanuud baidag table
class Products(models.Model):
    availableAmount = models.IntegerField()
    detail = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    displayPrice = models.CharField(max_length=200)
    
    def __str__(self):
        return str([self.availableAmount, self.detail, self.img, self.name, self.price, self.displayPrice])
    
    
    
    # Cart table    ENE TABLE IIG ASHIGLAHGUI!!!!!!!!!!!!!!!
# class Cart(models.Model):
#     availableAmount = models.IntegerField()
#     detail = models.CharField(max_length=200)
#     img = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     price = models.IntegerField()
#     displayPrice = models.CharField(max_length=200)
    
#     def __str__(self):
#         return str([self.availableAmount, self.detail, self.img, self.name, self.price, self.displayPrice])



    # cart table
class CartTwo(models.Model):
    availableAmount = models.IntegerField()
    number = models.IntegerField()
    detail = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    displayPrice = models.CharField(max_length=200)
    count = models.IntegerField()
    
    def __str__(self):
        return str([self.detail, self.img, self.name, self.price, self.displayPrice, self.count])







    #  zugeerl turshilt
class Humuus(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
    #  zugeerl turshilt
class Lalruud(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
    #  zugeerl turshilt
class Details(models.Model):
    type = models.CharField(max_length=20, default="", null=False)
    name = models.CharField(max_length=30, default="", null=False)
    
    
    #  doorh  database faildsen bolgoo
class CartTest(models.Model):
    count = models.IntegerField()


class CartTestTwo(models.Model):
    number = models.IntegerField()
    count = models.IntegerField()
    
    def __str__(self):
        return str([self.number, self.count])

    
    
 
    
# Products(availableAmount=100, detail="Урт оосортой жижиг цүнх", img="https://cdn3.shoppy.mn/spree/images/1307725/product/open-uri20220415-1859205-ouc9lb.", name="TRAVEL KIT PACK M", price=99900, displayPrice="99,900 ₮")

#  must insert to db:
# Products(availableAmount=12, detail="wireless", img="https://cdn3.shoppy.mn/spree/images/1308465/small/open-uri20220418-1906795-n3z550.", name="Чихэвч", price=120000, displayPrice="120,000 ₮")



# Products(availableAmount=43, detail="Скүүтэр - Цахилгаан", img="https://cdn3.shoppy.mn/spree/images/634439/large/DSC09464.JPG", name="ЦАХИЛГААН СКҮҮТЭР", price=1600000, displayPrice="1,600,000 ₮")






# Products(availableAmount=1, detail="3 CULOTTES", img="https://cdn3.shoppy.mn/spree/images/1311992/large/4990600.jpg", name="Дотоож", price=67860, displayPrice="67,860 ₮")






# Products(availableAmount=10, detail="Кет (Сникерс)", img="https://cdn3.shoppy.mn/spree/images/1311772/large/221K-F12-2945-1.jpg", name="ПҮҮЗ", price=109800, displayPrice="109,800 ₮")





# Products(availableAmount=43, detail="VILDKORN PILLOW", img="https://cdn3.shoppy.mn/spree/images/1310886/large/open-uri20220419-2005718-709vo6.", name="Дэр", price=46200, displayPrice="46,200 ₮")





# Products(availableAmount=243, detail="GORE-TEX O.D. CAP", img="https://cdn3.shoppy.mn/spree/images/1306695/large/open-uri20220415-1797231-1a7ax6u.", name="Малгай", price=149000, displayPrice="149,000 ₮")






# Products(availableAmount=8, detail="УТАСГҮЙ ЧИХЭВЧ", img="https://cdn3.shoppy.mn/spree/images/1308468/large/open-uri20220418-1906795-18s7t1k.", name="Чихэвч", price=119800, displayPrice="119,800 ₮")



# (12, 'wireless',  'https://cdn3.shoppy.mn/spree/images/1308465/small/open-uri20220418-1906795-n3z550.',  'Чихэвч', "120,000 ₮" )
# (43, 'Скүүтэр - Цахилгаан',   'https://cdn3.shoppy.mn/spree/images/634439/large/DSC09464.JPG',  'ЦАХИЛГААН СКҮҮТЭР', "1,600,000 ₮")
# (1, 'Дотоож', 1276967456756,  'https://cdn3.shoppy.mn/spree/images/1311992/large/4990600.jpg',  '3 CULOTTES', '67,860 ₮')
# (10, 'Кет (Сникерс)',  59679346346,  'https://cdn3.shoppy.mn/spree/images/1311772/large/221K-F12-2945-1.jpg',  'ПҮҮЗ', '109,800 ₮')
# (43, 'Дэр',  909679864837648,  'https://cdn3.shoppy.mn/spree/images/1310886/large/open-uri20220419-2005718-709vo6.',  'VILDKORN PILLOW', '46,200 ₮' )
# (234, 'Малгай', 60456549679737,  'https://cdn3.shoppy.mn/spree/images/1306695/large/open-uri20220415-1797231-1a7ax6u.',  'GORE-TEX O.D. CAP', '149,000 ₮')
# (8, 'Чихэвч',  7356796798678,  'https://cdn3.shoppy.mn/spree/images/1308468/large/open-uri20220418-1906795-18s7t1k.',  'УТАСГҮЙ ЧИХЭВЧ', '119,800 ₮' )