from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from home.models import CartTwo, Products




# Create your views here.
def index(request):
    cartSync = CartTwo.objects.all()
    total = 0
    
    
        #   niit dung bodoog total variable dotor hiigeed yovuulj bna (home/views.py index function dotor 
        #   doorh uildel bas baigaa)
    if cartSync:
        for neg in cartSync:
            total = total + int(neg.price) * int(neg.count)
            
            
    
    return render(request, "cart/index.html", {
        "cart": cartSync,
        "total": total
    })
    


def delete(request, number):
    del_pro = CartTwo.objects.filter( number=number )
    del_pro.delete()
    print(f"PSDAAAAAAAAAAAAAAAAAAAAAAAAA:  {del_pro}")
    return redirect("/cart")



def buy(request):
    cart = CartTwo.objects.all()
    products = Products.objects.all()
    # for x in cart:
    #     for p in products:
    #         if p.id == x.number:
    #             p.availableAmount = p.availableAmount - x.count
    #             print(f"BEFORE:____{p.availableAmount}")
    #             print(f"AFTER:________{p.availableAmount}")
    
    
    for x in cart:
        for p in products:
            if x.number == p.id:
                p.availableAmount = int(p.availableAmount) - int(x.count)
                p.save()
    
    
    for c in cart:
        c.delete()
        
        # print(f"PRODUCTS IN CART:_________  {x.number}_______ ")
    
    return HttpResponse("end geriin hayg edr avah form garch ireh yostoi!")