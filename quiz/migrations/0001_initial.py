# Generated by Django 4.0.5 on 2022-07-03 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quiz.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('difficulty', models.CharField(choices=[('H', 'Hard'), ('M', 'Medium'), ('E', 'Easy')], default='M', max_length=1)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_text', models.TextField(primary_key=True, serialize=False)),
                ('is_right', models.BooleanField()),
                ('updated_date', models.DateField(auto_now=True)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.question')),
            ],
        ),
    ]
