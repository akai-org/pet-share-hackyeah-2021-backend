# Generated by Django 4.0 on 2021-12-11 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('is_organization', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('posted', models.BooleanField()),
                ('item_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.item')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='ItemNeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('item_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.item')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='brand_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.itembrand'),
        ),
        migrations.AddField(
            model_name='item',
            name='type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='petapp.itemtype'),
        ),
    ]