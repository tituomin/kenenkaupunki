# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MapAnswer'
        db.create_table('geoanswers_mapanswer', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('respondent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geoanswers.Respondent'])),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.GeometryField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=84)),
            ('text_content', self.gf('django.db.models.fields.TextField')(null=True)),
            ('geom_source', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('geoanswers', ['MapAnswer'])

        # Adding M2M table for field divisions on 'MapAnswer'
        m2m_table_name = db.shorten_name('geoanswers_mapanswer_divisions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mapanswer', models.ForeignKey(orm['geoanswers.mapanswer'], null=False)),
            ('administrativedivision', models.ForeignKey(orm['munigeo.administrativedivision'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mapanswer_id', 'administrativedivision_id'])


    def backwards(self, orm):
        # Deleting model 'MapAnswer'
        db.delete_table('geoanswers_mapanswer')

        # Removing M2M table for field divisions on 'MapAnswer'
        db.delete_table(db.shorten_name('geoanswers_mapanswer_divisions'))


    models = {
        'geoanswers.mapanswer': {
            'Meta': {'object_name': 'MapAnswer'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '84'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            'divisions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['munigeo.AdministrativeDivision']"}),
            'geom_source': ('django.db.models.fields.TextField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'respondent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geoanswers.Respondent']"}),
            'text_content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'geoanswers.respondent': {
            'Meta': {'object_name': 'Respondent'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'life_situation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['munigeo.AdministrativeDivision']", 'null': 'True'}),
            'nonlocal_home': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'probability_stay_five_years': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
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
            'transport_mode_first': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'transport_mode_second': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'transport_mode_third': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        'munigeo.administrativedivision': {
            'Meta': {'unique_together': "(('origin_id', 'type', 'parent'),)", 'object_name': 'AdministrativeDivision'},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True', 'null': 'True'}),
            'name_fi': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True', 'null': 'True'}),
            'name_sv': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True', 'null': 'True'}),
            'ocd_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '200', 'null': 'True'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'related_name': "'children'", 'to': "orm['munigeo.AdministrativeDivision']", 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['munigeo.AdministrativeDivisionType']"})
        },
        'munigeo.administrativedivisiontype': {
            'Meta': {'object_name': 'AdministrativeDivisionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        }
    }

    complete_apps = ['geoanswers']