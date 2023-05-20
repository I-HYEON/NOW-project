from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0002_depositproducts_joined_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depositproducts',
            name='joined_user',
        ),
    ]
