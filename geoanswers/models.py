from django.contrib.gis.db import models

from munigeo.models import AdministrativeDivision

# Create your models here.
class Respondent(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    property_id = models.PositiveIntegerField(null=False, unique=True)
    createtime = models.DateTimeField(null=False)
    age = models.PositiveIntegerField(null=True)
    language = models.CharField(max_length=2, null=True)

    life_situation = models.CharField(max_length=200, null=True)
    neighborhood = models.ForeignKey(AdministrativeDivision, db_index=True, null=True)
    nonlocal_home = models.CharField(max_length=200, null=True)
    transport_mode_first = models.CharField(max_length=30, null=True)
    transport_mode_second = models.CharField(max_length=30, null=True)
    transport_mode_third = models.CharField(max_length=30, null=True)
    probability_stay_five_years = models.CharField(max_length=30, null=True)

    scale_agree_high_rise = models.FloatField(null=True)
    scale_enjoy_outdoors_large_woods = models.FloatField(null=True)
    scale_enjoy_culture_urban_meetings = models.FloatField(null=True)
    scale_prefer_daily_shopping_near = models.FloatField(null=True)
    scale_would_use_rail_transport_more = models.FloatField(null=True)
    scale_agree_suburbs_build_near_stations = models.FloatField(null=True)
    scale_enjoy_metropolis_fascinating_possibilities = models.FloatField(null=True)
    scale_agree_bulevardisation = models.FloatField(null=True)
    scale_agree_add_density = models.FloatField(null=True)
    scale_agree_add_my_area_density_for_less_cars = models.FloatField(null=True)
    scale_my_area_could_be_built_more = models.FloatField(null=True)

    def __str__(self):
        def field_str(field):
            fieldname = field.name
            return fieldname + ": " + str(getattr(self, fieldname, '<empty>'))
        return "\n".join(map(field_str, __class__._meta.fields))


class MapAnswer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    respondent = models.ForeignKey(Respondent, db_index=True, null=True, default=None)
    createtime = models.DateTimeField(null=False)
    geometry = models.GeometryField(null=True, default=None)
    geometry_original = models.GeometryField(srid=3067)
    type = models.CharField(max_length=10, null=False)  # todo
    category = models.CharField(max_length=84, null=False)
    text_content = models.TextField(null=True)
    divisions = models.ManyToManyField('munigeo.AdministrativeDivision')

