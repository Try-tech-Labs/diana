# Generated by Django 3.1.5 on 2021-01-25 02:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20210124_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=280)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('source_url', models.URLField()),
                ('thumbnail', models.URLField()),
                ('content', models.CharField(max_length=512)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='content.post')),
                ('tags', models.ManyToManyField(to='content.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]