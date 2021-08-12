# Generated by Django 2.2.2 on 2019-06-24 08:21

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_local', models.CharField(db_index=True, max_length=100)),
                ('name_en', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'careers',
                'ordering': ['name_local', 'name_en'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_local', models.CharField(db_index=True, max_length=100)),
                ('name_en', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'category',
                'ordering': ['name_local', 'name_en'],
            },
        ),
        migrations.CreateModel(
            name='InfluencerCareers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career', to='influencers.Career')),
            ],
            options={
                'db_table': 'influencer_careers',
            },
        ),
        migrations.CreateModel(
            name='InfluencerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='influencers.Category')),
            ],
            options={
                'db_table': 'influencer_category',
            },
        ),
        migrations.CreateModel(
            name='InfluencerLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'influencer_location',
            },
        ),
        migrations.CreateModel(
            name='Influencers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('influencer_code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(blank=True, db_index=True, max_length=30, null=True)),
                ('country', django_countries.fields.CountryField(default='VN', max_length=2)),
                ('rating', models.FloatField(default=0)),
                ('reach', models.FloatField(default=0)),
                ('relevance', models.FloatField(default=0)),
                ('resonance', models.FloatField(default=0)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('careers', models.ManyToManyField(related_name='careers', through='influencers.InfluencerCareers', to='influencers.Career')),
                ('categories', models.ManyToManyField(related_name='categories', through='influencers.InfluencerCategory', to='influencers.Category')),
            ],
            options={
                'db_table': 'influencers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=10, unique=True)),
                ('name_local', models.CharField(db_index=True, max_length=100)),
                ('name_en', models.CharField(db_index=True, max_length=100)),
                ('country', django_countries.fields.CountryField(default='VN', max_length=2)),
            ],
            options={
                'db_table': 'location',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'social',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TopicTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_local', models.CharField(db_index=True, max_length=100)),
                ('name_en', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'topic_tags',
                'ordering': ['name_local', 'name_en'],
            },
        ),
        migrations.CreateModel(
            name='InfluencerTopicTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencers.Influencers')),
                ('topic_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_tag', to='influencers.TopicTag')),
            ],
            options={
                'db_table': 'influencer_topic_tag',
            },
        ),
        migrations.CreateModel(
            name='InfluencerSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, unique=True)),
                ('currency', models.CharField(max_length=3)),
                ('price', models.IntegerField(default=0)),
                ('fans_quantity', models.IntegerField(default=0)),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencers.Influencers')),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='influencers.Social')),
            ],
            options={
                'db_table': 'influencer_social',
            },
        ),
        migrations.AddField(
            model_name='influencers',
            name='locations',
            field=models.ManyToManyField(related_name='locations', through='influencers.InfluencerLocation', to='influencers.Location'),
        ),
        migrations.AddField(
            model_name='influencers',
            name='socials',
            field=models.ManyToManyField(related_name='socials', through='influencers.InfluencerSocial', to='influencers.Social'),
        ),
        migrations.AddField(
            model_name='influencers',
            name='topic_tags',
            field=models.ManyToManyField(related_name='topic_tags', through='influencers.InfluencerTopicTag', to='influencers.TopicTag'),
        ),
        migrations.AddField(
            model_name='influencerlocation',
            name='influencer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencers.Influencers'),
        ),
        migrations.AddField(
            model_name='influencerlocation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='influencers.Location'),
        ),
        migrations.AddField(
            model_name='influencercategory',
            name='influencer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencers.Influencers'),
        ),
        migrations.AddField(
            model_name='influencercareers',
            name='influencer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencers.Influencers'),
        ),
    ]
