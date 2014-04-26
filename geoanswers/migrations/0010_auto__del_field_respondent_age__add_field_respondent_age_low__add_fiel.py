# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Respondent.age'
        db.delete_column('geoanswers_respondent', 'age')

        # Adding field 'Respondent.age_low'
        db.add_column('geoanswers_respondent', 'age_low',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Respondent.age_high'
        db.add_column('geoanswers_respondent', 'age_high',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Respondent.age'
        db.add_column('geoanswers_respondent', 'age',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'Respondent.age_low'
        db.delete_column('geoanswers_respondent', 'age_low')

        # Deleting field 'Respondent.age_high'
        db.delete_column('geoanswers_respondent', 'age_high')


    models = {
        'geoanswers.mapanswer': {
            'Meta': {'object_name': 'MapAnswer'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '84'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['munigeo.AdministrativeDivision']", 'symmetrical': 'False'}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'default': 'None'}),
            'geometry_original': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '3067'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'respondent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['geoanswers.Respondent']", 'default': 'None'}),
            'text_content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'geoanswers.respondent': {
            'Meta': {'object_name': 'Respondent'},
            'age_high': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'age_low': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '2'}),
            'life_situation': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['munigeo.AdministrativeDivision']"}),
            'nonlocal_home': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200'}),
            'probability_stay_five_years': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30'}),
            'property_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'scale_agree_add_density': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_agree_add_my_area_density_for_less_cars': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_agree_bulevardisation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_agree_high_rise': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_agree_suburbs_build_near_stations': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_enjoy_culture_urban_meetings': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_enjoy_metropolis_fascinating_possibilities': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_enjoy_outdoors_large_woods': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_my_area_could_be_built_more': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_prefer_daily_shopping_near': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_would_use_rail_transport_more': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'transport_mode_first': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30'}),
            'transport_mode_second': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30'}),
            'transport_mode_third': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30'})
        },
        'munigeo.administrativedivision': {
            'Meta': {'object_name': 'AdministrativeDivision', 'unique_together': "(('origin_id', 'type', 'parent'),)"},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'db_index': 'True', 'blank': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'db_index': 'True', 'blank': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'db_index': 'True', 'blank': 'True'}),
            'ocd_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'unique': 'True', 'db_index': 'True', 'max_length': '200'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'null': 'True', 'to': "orm['munigeo.AdministrativeDivision']", 'related_name': "'children'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['munigeo.AdministrativeDivisionType']"})
        },
        'munigeo.administrativedivisiontype': {
            'Meta': {'object_name': 'AdministrativeDivisionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['geoanswers']