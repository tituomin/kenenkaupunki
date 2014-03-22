# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Respondent'
        db.create_table('geoanswers_respondent', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('property_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('life_situation', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['munigeo.AdministrativeDivision'])),
            ('nonlocal_home', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('transport_mode_first', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('transport_mode_second', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('transport_mode_third', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('scale_agree_high_rise', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_probability_stay_five_years', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_enjoy_outdoors_large_woods', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_enjoy_culture_urban_meetings', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_prefer_daily_shopping_near', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_would_use_rail_transport_more', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_agree_suburbs_build_near_stations', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_enjoy_metropolis_fascinating_possibilities', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_agree_bulevardisation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_agree_add_density', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_agree_add_my_area_density_for_less_cars', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('scale_my_area_could_be_built_more', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('geoanswers', ['Respondent'])


    def backwards(self, orm):
        # Deleting model 'Respondent'
        db.delete_table('geoanswers_respondent')


    models = {
        'geoanswers.respondent': {
            'Meta': {'object_name': 'Respondent'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'life_situation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['munigeo.AdministrativeDivision']"}),
            'nonlocal_home': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'scale_probability_stay_five_years': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'scale_would_use_rail_transport_more': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'transport_mode_first': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'transport_mode_second': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'transport_mode_third': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'munigeo.administrativedivision': {
            'Meta': {'object_name': 'AdministrativeDivision', 'unique_together': "(('origin_id', 'type', 'parent'),)"},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'null': 'True', 'max_length': '100'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'null': 'True', 'max_length': '50'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'null': 'True', 'max_length': '50'}),
            'ocd_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'null': 'True', 'unique': 'True', 'max_length': '200'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': "orm['munigeo.AdministrativeDivision']"}),
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