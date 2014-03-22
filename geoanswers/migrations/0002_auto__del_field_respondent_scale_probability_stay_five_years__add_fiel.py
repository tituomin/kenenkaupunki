# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Respondent.scale_probability_stay_five_years'
        db.delete_column('geoanswers_respondent', 'scale_probability_stay_five_years')

        # Adding field 'Respondent.probability_stay_five_years'
        db.add_column('geoanswers_respondent', 'probability_stay_five_years',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Respondent.scale_probability_stay_five_years'
        db.add_column('geoanswers_respondent', 'scale_probability_stay_five_years',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Deleting field 'Respondent.probability_stay_five_years'
        db.delete_column('geoanswers_respondent', 'probability_stay_five_years')


    models = {
        'geoanswers.respondent': {
            'Meta': {'object_name': 'Respondent'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'life_situation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['munigeo.AdministrativeDivision']", 'null': 'True'}),
            'nonlocal_home': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'probability_stay_five_years': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
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
            'transport_mode_first': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'transport_mode_second': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'transport_mode_third': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'munigeo.administrativedivision': {
            'Meta': {'unique_together': "(('origin_id', 'type', 'parent'),)", 'object_name': 'AdministrativeDivision'},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'ocd_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'unique': 'True', 'db_index': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['munigeo.AdministrativeDivision']", 'null': 'True', 'related_name': "'children'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['munigeo.AdministrativeDivisionType']"})
        },
        'munigeo.administrativedivisiontype': {
            'Meta': {'object_name': 'AdministrativeDivisionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True', 'unique': 'True'})
        }
    }

    complete_apps = ['geoanswers']