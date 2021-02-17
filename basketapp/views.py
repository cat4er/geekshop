from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    # content = {}
    # return render(request, "basketapp/basket.html", content)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request):
    # content = {}
    # return render(request, "basketapp/basket.html", content)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

# def basket_get_price(request):
#     total_price = 0
#     for i in range(len(Product.objects.all())):
#         qty_price = Product.objects.filter(basket__product=i).values("price").union(
#             Basket.objects.filter(user=request.user, product__id=i)).values("quantity")
#
#         if qty_price:
#             sub = qty_price[0].get("quantity") * qty_price[1].get("quantity")
#             total_price += sub
#     # print(f' на {total_price}')
#     return total_price