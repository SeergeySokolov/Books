from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rating', '0005_remove_book_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='value',
            field=models.PositiveIntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], default=0),
        ),
    ]
