# Generated by Django 2.0.2 on 2020-08-02 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionnaireColorCueNew', '0003_auto_20200802_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassifyStimuiTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField(default=None)),
                ('block_number', models.IntegerField(default=None)),
                ('sequence_number', models.IntegerField(default=None)),
                ('file_name', models.CharField(default=None, max_length=150)),
                ('user_option', models.CharField(default=None, max_length=10)),
                ('time_taken', models.FloatField(default=None)),
                ('timestamp', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionnaireColorCueNew.UserDetails')),
            ],
            options={
                'verbose_name_plural': 'Classify Stimluli Table',
            },
        ),
    ]