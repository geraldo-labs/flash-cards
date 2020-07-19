from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'categories'

    name = models.CharField(max_length=250, db_column='name')
    description = models.TextField(db_column='description')
    category = models.ForeignKey('Category', null=True, related_name='categories', on_delete=models.PROTECT)


class Card(models.Model):
    class Meta:
        db_table = 'cards'

    name = models.CharField(max_length=250, db_column='name')
    description = models.TextField(db_column='description')
    image = models.ImageField(upload_to='image_cards', max_length=250)
    audio = models.FileField(upload_to='audio_cards', max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
