from django.shortcuts import render
from django.core.paginator import Paginator
from core.models import AboutProducts, News, MoneyByPhone, WorkAsLeader, FamilyShopping
from dotenv import load_dotenv
import os

load_dotenv()

def home(request):
    return render(request=request,template_name="home.html")

def news(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, per_page=os.getenv('PAGINATION_NUMBER')) #type:ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request=request,template_name="news.html", context=context)

def work_as_leader(request):
    page_data = WorkAsLeader.objects.first()
    context = {
        'page_data': page_data,
    }
    return render(request=request, template_name='work-as-leader.html', context=context)

def family_shopping(request):
    page_data = FamilyShopping.objects.first()
    context = {
        'page_data': page_data,
    }
    return render(request=request, template_name='family-shopping.html', context=context)

def money_by_phone(request):
    page_data = MoneyByPhone.objects.first()
    context = {
        'page_data': page_data,
    }
    return render(request=request, template_name='money-by-phone.html', context=context)

def about_products(request):
    products_list = AboutProducts.objects.all()
    paginator = Paginator(products_list, per_page=os.getenv('PAGINATION_NUMBER'))  # type:ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request=request, template_name='about-products.html', context=context)