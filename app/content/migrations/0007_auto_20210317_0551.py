# Generated by Django 3.1.7 on 2021-03-17 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0006_news"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="post",
        ),
        migrations.RemoveField(
            model_name="news",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="post",
            name="title",
        ),
        migrations.RemoveField(
            model_name="tweet",
            name="post",
        ),
        migrations.RemoveField(
            model_name="tweet",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="video",
            name="post",
        ),
        migrations.RemoveField(
            model_name="video",
            name="tags",
        ),
        migrations.AddField(
            model_name="news",
            name="trending_topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="news",
                to="content.twittertrendingtopic",
            ),
        ),
        migrations.AddField(
            model_name="tag",
            name="twitter_trending_topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="content.twittertrendingtopic",
            ),
        ),
        migrations.AddField(
            model_name="tweet",
            name="trending_topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tweets",
                to="content.twittertrendingtopic",
            ),
        ),
        migrations.AddField(
            model_name="video",
            name="trending_topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="content.twittertrendingtopic",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="content.postcategory",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="postcategory",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="twittertrendingtopic",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="twittertrendingtopic",
            name="post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trending_topics",
                to="content.post",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]