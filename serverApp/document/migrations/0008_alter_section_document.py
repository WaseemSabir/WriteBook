# Generated by Django 4.0.1 on 2022-01-16 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0007_alter_section_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='document',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.document'),
        ),
    ]
