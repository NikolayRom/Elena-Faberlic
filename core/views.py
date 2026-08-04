from django.shortcuts import render
from django.core.paginator import Paginator
from core.models import AboutProducts, News, MoneyByPhone, WorkAsLeader, FamilyShopping, HomeStarterSection, HomeGiftsSection, HomeDealOffer
from dotenv import load_dotenv
import os

load_dotenv()

def home(request):
    gifts_obj = HomeGiftsSection.objects.first()
    starter_obj = HomeStarterSection.objects.first()

    gifts_images = []
    if gifts_obj:
        gifts_images = [gifts_obj.image_1, gifts_obj.image_2, gifts_obj.image_3, gifts_obj.image_4, gifts_obj.image_5]

    starter_images = []
    if starter_obj:
        starter_images = [starter_obj.image_1, starter_obj.image_2, starter_obj.image_3, starter_obj.image_4,
                          starter_obj.image_5]

    INITIAL_SIZE = int(os.getenv('LOAD_MORE_INITIALLY'))

    deals = HomeDealOffer.objects.all()[:INITIAL_SIZE]
    has_more_deals = HomeDealOffer.objects.count() > INITIAL_SIZE #type:ignore

    context = {
        'gifts_images': gifts_images,
        'starter_images': starter_images,
        'deals': deals,
        'has_more_deals': has_more_deals,
        'next_offset': INITIAL_SIZE,
    }
    return render(request=request, template_name='core/home.html', context=context)

def load_more_deals(request):
    offset = int(request.GET.get('offset', os.getenv('LOAD_MORE_INITIALLY'))) #type:ignore
    limit = int(os.getenv('LOAD_MORE_EXTEND'))

    deals = HomeDealOffer.objects.all()[offset:offset + limit]
    has_more = (offset + limit) < HomeDealOffer.objects.count()

    context = {
        'deals': deals,
        'next_offset': offset + limit,
        'has_more': has_more,
    }
    return render(request=request, template_name='core/partials/deals_chunk.html', context=context)

def news(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, per_page=os.getenv('PAGINATION_NUMBER')) #type:ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request=request,template_name="core/news.html", context=context)

def work_as_leader(request):
    page_data = WorkAsLeader.objects.first()
    context = {
        'page_data': page_data,
    }
    return render(request=request, template_name='core/work-as-leader.html', context=context)

def family_shopping(request):
    page_data = FamilyShopping.objects.first()
    context = {
        'page_data': page_data,
    }
    return render(request=request, template_name='core/family-shopping.html', context=context)

def money_by_phone(request):
    page_data = MoneyByPhone.objects.first()
    context = {
        'page_data': page_data,
    }
    return render(request=request, template_name='core/money-by-phone.html', context=context)

def about_products(request):
    products_list = AboutProducts.objects.all()
    paginator = Paginator(products_list, per_page=os.getenv('PAGINATION_NUMBER'))  # type:ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request=request, template_name='core/about-products.html', context=context)