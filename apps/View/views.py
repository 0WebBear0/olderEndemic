from django.shortcuts import render, get_object_or_404

from .models import Category, Product, Firm

from .form import FiltrForm


def Home(request):
    data = {"categ": Category.objects.order_by('name'),
            "prod": Product.objects.order_by('name')[0:5]}
    return render(request, 'products/Home.html', context=data)


def categoryDetail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    prodDet = Product.objects.filter(category=category_id)
    filtForm = FiltrForm()
    data = {
        "categ": category,
        "prod": prodDet,
        "filtForm": filtForm,
    }
    return render(request, "products/categoryList.html", context=data)


def productsDetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/productList.html", {'product': product})


def Catalog(request):
    prodDet = Product.objects.order_by('price')
    data = {
        "prod": prodDet,
    }
    return render(request, "products/Catalog.html", context=data)


def Map(request):
    firm = Firm.objects.order_by('name')
    data = {
        "firm": firm,
    }
    return render(request, "products/Map.html", context=data)


def firmView(request, firm_id):
    firm = get_object_or_404(Firm, id=firm_id)
    return render(request, "products/firm.html", {'firm': firm})
