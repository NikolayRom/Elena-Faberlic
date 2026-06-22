from django.db import models

class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to="news_images/",
        verbose_name="Фото"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

class AboutProducts(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to="about_products_images/",
        verbose_name="Фото"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = 'О продукции'
        verbose_name_plural = 'О продукции'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

class MoneyByPhone(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        default='Заработок по телефону',
    )
    image = models.ImageField(
        upload_to="money_by_phone/",
        verbose_name="Фото"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = 'Заработок по телефону'
        verbose_name_plural = 'Заработок по телефону'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

class WorkAsLeader(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        default='Работа лидером',
    )
    image = models.ImageField(
        upload_to="work_as_leader/",
        verbose_name="Фото"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = 'Работа лидером'
        verbose_name_plural = 'Работа лидером'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

class FamilyShopping(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        default='Покупки для семьи',
    )
    image = models.ImageField(
        upload_to="family_shopping/",
        verbose_name="Фото"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = 'Покупки для семьи'
        verbose_name_plural = 'Покупки для семьи'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

class HomeGiftsSection(models.Model):
    image_1 = models.ImageField(
        upload_to='home/gifts/',
        verbose_name="Фото 1 (Беларусь)"
    )
    image_2 = models.ImageField(
        upload_to='home/gifts/',
        verbose_name="Фото 2 (Россия)"
    )
    image_3 = models.ImageField(
        upload_to='home/gifts/',
        verbose_name="Фото 3 (Казахстан)"
    )
    image_4 = models.ImageField(
        upload_to='home/gifts/',
        verbose_name="Фото 4 (Таджикистан)"
    )
    image_5 = models.ImageField(
        upload_to='home/gifts/',
        verbose_name="Фото 5 (Кыргызстан)"
    )

    class Meta:
        verbose_name = "Главная: Подарки для новичков"
        verbose_name_plural = "Главная: Подарки для новичков"

    def __str__(self):
        return "Настройки блока 'Подарки для новичков'"

class HomeStarterSection(models.Model):
    image_1 = models.ImageField(
        upload_to='home/starter/',
        verbose_name="Фото 1 (Беларусь)"
    )
    image_2 = models.ImageField(
        upload_to='home/starter/',
        verbose_name="Фото 2 (Россия)"
    )
    image_3 = models.ImageField(
        upload_to='home/starter/',
        verbose_name="Фото 3 (Казахстан)"
    )
    image_4 = models.ImageField(
        upload_to='home/starter/',
        verbose_name="Фото 4 (Таджикистан)"
    )
    image_5 = models.ImageField(
        upload_to='home/starter/',
        verbose_name="Фото 5 (Кыргызстан)"
    )

    class Meta:
        verbose_name = "Главная: Стартовая программа"
        verbose_name_plural = "Главная: Стартовая программа"

    def __str__(self):
        return "Настройки блока 'Стартовая программа'"

class HomeDealOffer(models.Model):
    image = models.ImageField(
        upload_to='home/deals/',
        verbose_name="Фото предложения"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        verbose_name = "Главная: Выгодные предложения"
        verbose_name_plural = "Главная: Выгодные предложения"
        ordering = ['-created_at']

    def __str__(self):
        return f"Предложение от {self.created_at.strftime('%d.%m.%Y')}"