# Generated by Django 5.0.6 on 2024-05-25 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0009_delete_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=100, null=True, verbose_name='Trip remark')),
            ],
            options={
                'verbose_name': 'Remark',
                'verbose_name_plural': 'Remarks',
            },
        ),
        migrations.AddField(
            model_name='trip',
            name='remark',
            field=models.ManyToManyField(related_name='remark', to='photogallery.remark'),
        ),
    ]
