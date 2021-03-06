# Generated by Django 3.0.4 on 2020-03-04 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import partiu.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', partiu.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('entrance', 'Entrance'), ('exit', 'Exit')], max_length=8)),
                ('value', models.IntegerField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on')),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated on')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
            },
        ),
    ]
