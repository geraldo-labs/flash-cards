# Generated by Django 3.0.8 on 2020-07-19 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=250)),
                ('description', models.TextField(db_column='description')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='card.Category')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=250)),
                ('description', models.TextField(db_column='description')),
                ('image', models.ImageField(max_length=250, upload_to='image_cards')),
                ('audio', models.FileField(max_length=250, upload_to='audio_cards')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card.Category')),
            ],
            options={
                'db_table': 'cards',
            },
        ),
    ]