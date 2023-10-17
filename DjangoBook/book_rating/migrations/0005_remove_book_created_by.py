from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_rating', '0004_book_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created_by',
        ),
    ]
