# Generated by Django 4.1.1 on 2022-09-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('college', models.CharField(choices=[('COLLEGE OF EDUCATION', 'COLLEGE OF EDUCATION'), ('COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION', 'COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION'), ('COLLEGE OF HEALTH AND ALLIED SCIENCES', 'COLLEGE OF HEALTH AND ALLIED SCIENCES'), ('COLLEGE OF HUMANITIES AND SOCIAL SCIENCES', 'COLLEGE OF HUMANITIES AND SOCIAL SCIENCES'), ('COLLEGE OF EARTH SCIENCES', 'COLLEGE OF EARTH SCIENCES')], default='COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION', max_length=255, unique=True)),
                ('description', models.TextField()),
                ('years_of_study', models.SmallIntegerField()),
                ('fee', models.PositiveIntegerField()),
                ('knowledge', models.TextField()),
                ('skills', models.TextField()),
                ('competences', models.TextField()),
                ('special_requirements', models.TextField()),
                ('fields_of_work', models.TextField()),
            ],
        ),
    ]