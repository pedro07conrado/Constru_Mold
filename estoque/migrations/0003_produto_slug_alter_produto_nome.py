from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('estoque', '0002_imagem'),
    ]
    operations = [
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]