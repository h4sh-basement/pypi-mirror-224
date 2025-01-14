# Generated by Django 4.1.4 on 2023-08-04 04:52

from django.db import migrations, models
import django.db.models.deletion
import rest.models.base
import rest.models.metadata


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0013_memberdevice_ip'),
        ('medialib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('path', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField()),
                ('body', models.TextField(blank=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.group')),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.member')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='wiki.page')),
            ],
            bases=(models.Model, rest.models.base.RestModel, rest.models.metadata.MetaDataModel),
        ),
        migrations.CreateModel(
            name='PageMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_index=True, default=None, max_length=32, null=True)),
                ('key', models.CharField(db_index=True, max_length=80)),
                ('value_format', models.CharField(max_length=16)),
                ('value', models.TextField()),
                ('int_value', models.IntegerField(blank=True, default=None, null=True)),
                ('float_value', models.IntegerField(blank=True, default=None, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='wiki.page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='wiki.page')),
                ('group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.group')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='medialib.mediaitem')),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.member')),
            ],
            bases=(models.Model, rest.models.base.RestModel),
        ),
    ]
