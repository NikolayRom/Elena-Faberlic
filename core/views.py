from django.shortcuts import render

def home(request):
    return render(request=request,template_name="home.html")

def news(request):
    return render(request=request,template_name="news.html")

def work_as_leader(request):
    return render(request=request, template_name='work-as-leader.html')

def family_shopping(request):
    return render(request=request, template_name='family-shopping.html')

def money_by_phone(request):
    return render(request=request, template_name='money-by-phone.html')

def about_products(request):
    return render(request=request, template_name='about-products.html')