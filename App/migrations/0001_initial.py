# Generated by Django 3.2 on 2022-02-10 13:05

import App.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_projet', models.CharField(max_length=30, verbose_name='Titre Projet')),
                ('duree_projet', models.IntegerField(default=0, verbose_name='Duree Estimee')),
                ('temps_alloue_par_projet', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Temps Alloue')),
                ('besoins', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('est_valide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, validators=[App.models.is_esprit_email], verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='App.user')),
            ],
            bases=('App.user',),
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='App.user')),
                ('groupe', models.CharField(max_length=30)),
            ],
            bases=('App.user',),
        ),
        migrations.CreateModel(
            name='MembershipInProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated_by_member', models.IntegerField(verbose_name='temps alloué par les membres')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.projet')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='projet',
            name='createur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to='App.etudiant'),
        ),
        migrations.AddField(
            model_name='projet',
            name='members',
            field=models.ManyToManyField(related_name='les_membres', through='App.MembershipInProject', to='App.Etudiant'),
        ),
        migrations.AddField(
            model_name='projet',
            name='superviseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_coach', to='App.coach'),
        ),
    ]
