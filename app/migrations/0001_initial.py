# Generated by Django 3.2 on 2021-04-23 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='img/dog.jpg', upload_to='uploads/avatars/')),
                ('nickname', models.CharField(default='Quest', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='default_tag', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Question_Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(1, 'like'), (-1, 'dislike'), (0, 'none')], default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
            options={
                'verbose_name': 'Оценка Вопроса',
                'verbose_name_plural': 'Оценки Вопросов',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.CreateModel(
            name='Answer_Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(1, 'like'), (-1, 'dislike'), (0, 'none')], default=0)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
            options={
                'verbose_name': 'Оценка Ответа',
                'verbose_name_plural': 'Оценки Ответов',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
    ]
