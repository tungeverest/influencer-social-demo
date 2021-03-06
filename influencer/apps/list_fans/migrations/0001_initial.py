# Generated by Django 2.2.2 on 2019-06-24 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('influencers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_range_min', models.IntegerField(default=0)),
                ('age_range_max', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'age_range',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_local', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'interest',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FanInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fans_quantity', models.IntegerField(default=0)),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan_interest_influencer', to='influencers.Influencers')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest', to='list_fans.Interest')),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan_interest_social', to='influencers.Social')),
            ],
            options={
                'db_table': 'fan_interest',
            },
        ),
        migrations.CreateModel(
            name='FanAgeRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fans_quantity', models.IntegerField(default=0)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='age_range', to='list_fans.AgeRange')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan_age_influencer', to='influencers.Influencers')),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan_age_social', to='influencers.Social')),
            ],
            options={
                'db_table': 'fan_age_range',
            },
        ),
    ]
