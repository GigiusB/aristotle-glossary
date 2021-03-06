# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0002_auto_20150409_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlossaryAdditionalDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('definition', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GlossaryItem',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('index', models.ManyToManyField(related_name='related_glossary_items', null=True, to='aristotle_mdr._concept', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.AddField(
            model_name='glossaryadditionaldefinition',
            name='glossaryItem',
            field=models.ForeignKey(related_name='alternate_definitions', to='aristotle_glossary.GlossaryItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glossaryadditionaldefinition',
            name='registrationAuthority',
            field=models.ForeignKey(to='aristotle_mdr.RegistrationAuthority'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='glossaryadditionaldefinition',
            unique_together=set([('glossaryItem', 'registrationAuthority')]),
        ),
    ]
