import os
from dotenv import load_dotenv

load_dotenv()

def env_vars(request):
    return {
        'CATALOG_LINK': os.getenv('CATALOG_LINK'),
        'REGISTER_LINK': os.getenv('REGISTER_LINK'),
        'GIFT_LINK': os.getenv('GIFT_LINK'),
        'SITE_LINK': os.getenv('SITE_LINK'),
        'SITE_NAME': os.getenv('SITE_NAME'),
        'SITE_TITLE_2': os.getenv('SITE_TITLE_2'),
        'CONSULTANT_TELEGRAM_LINK': os.getenv('CONSULTANT_TELEGRAM_LINK'),
        'CONSULTANT_WHATSAPP_LINK': os.getenv('CONSULTANT_WHATSAPP_LINK'),
        'CONSULTANT_VIBER_LINK': os.getenv('CONSULTANT_VIBER_LINK'),
    }