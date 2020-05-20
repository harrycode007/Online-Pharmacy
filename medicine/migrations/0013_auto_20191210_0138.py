# Generated by Django 2.2.1 on 2019-12-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_auto_20191210_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineordered',
            name='Ashwagandha',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Chyawanprash',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Cofsils',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Crocin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Dettol',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='DigeneGel',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='DigeneTablet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Hajmola',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Lubrifresh',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Moov',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Paracetamol',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Seacod',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Shelcal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Vicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='Zandu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicineordered',
            name='totalSum',
            field=models.IntegerField(default=0),
        ),
    ]
