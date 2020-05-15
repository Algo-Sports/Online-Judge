# Generated by Django 3.0.6 on 2020-05-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0006_testcases'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_code',
            field=models.CharField(blank=True, help_text='Code for the question', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='question_name',
            field=models.CharField(blank=True, help_text='Name of the question', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='question_score',
            field=models.IntegerField(blank=True, default=0, help_text='Score for solving this problem'),
        ),
    ]