from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_rating', '0002_remove_book_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='book_rating.book'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('book', 'user')},
        ),
    ]
