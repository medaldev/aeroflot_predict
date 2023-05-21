# Generated by Django 4.2.1 on 2023-05-21 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('like', models.IntegerField(verbose_name='Тип судна')),
            ],
            options={
                'verbose_name': 'Воздушные судна',
                'verbose_name_plural': 'Воздушные судна',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Аэропорт',
                'verbose_name_plural': 'Аэропорты',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Города',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('time_depart', models.DateTimeField(verbose_name='Время вылета')),
                ('time_arrive', models.DateTimeField(verbose_name='Время прилета')),
                ('time_left', models.DateField(verbose_name='Время до отправления')),
                ('visible', models.BooleanField()),
                ('available', models.BooleanField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights_airplane', to='predict.airplane', verbose_name='Самолет')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights_from', to='predict.airport', verbose_name='Город вылета')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights_to', to='predict.airport', verbose_name='Город прилета')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airports', to='predict.city', verbose_name='Город'),
        ),
    ]
