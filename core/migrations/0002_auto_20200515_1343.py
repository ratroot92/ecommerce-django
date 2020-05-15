# Generated by Django 2.2 on 2020-05-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport Wear'), ('OW', 'Outwear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('pri', 'primary'), ('sec', 'secondary'), ('inf', 'info'), ('dan', 'danger'), ('dar', 'dark'), ('suc', 'successs'), ('war', 'warning')], default='pri', max_length=3),
            preserve_default=False,
        ),
    ]
