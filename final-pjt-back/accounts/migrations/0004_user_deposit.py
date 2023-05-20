from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0003_remove_depositproducts_joined_user'),
        ('accounts', '0003_remove_user_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deposit',
            field=models.ManyToManyField(blank=True, related_name='joined', to='deposits.DepositProducts'),
        ),
    ]
