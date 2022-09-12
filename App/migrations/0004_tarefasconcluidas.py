# Generated by Django 4.0.6 on 2022-08-14 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0003_delete_tarefasconcluidas_tarefa_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarefasConcluidas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tarefa', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('prioridade', models.CharField(choices=[('Alta', 'Alta'), ('Normal', 'Normal'), ('Baixa', 'Baixa')], max_length=6)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]