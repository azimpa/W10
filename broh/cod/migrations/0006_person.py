# Generated by Django 4.2.3 on 2023-07-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cod', '0005_delete_monday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
