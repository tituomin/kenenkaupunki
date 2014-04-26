import csv
import re

from munigeo.models import (
    AdministrativeDivision,
    AdministrativeDivisionType,
    AdministrativeDivisionGeometry
)
from .models import Respondent, MapAnswer

def get_int(row, key):
    try:
        return int(row.get(key))
    except ValueError:
        return None

def get_string(row, key):
    result = row.get(key).strip()
    if len(result) == 0:
        return None
    return result

def slider_value(row, key):
    result = row.get(key).strip()
    if len(result) == 0:
        return None
    if result == 'slider_default_value':
        return 50.0
    return float(result.replace(',', '.'))

def age(row, key):
    s = row.get(key).strip()
    if len(s) == 0:
        return None, None
    low, high = s.split("-")
    if low == 'alle': low = None
    if high == '': high = None
    return low, high

def get_neighborhood(row, key):
    neighborhood_name_match = re.match(r'([^(]*) ?(\([^)]+\))?', row[key])
    if neighborhood_name_match:
        neighborhood_name = neighborhood_name_match.group(1).strip()
        division = None
        if len(neighborhood_name) == 0:
            return division
        neighborhood_type = AdministrativeDivisionType.objects.get(
            type='neighborhood'
        )
        division = AdministrativeDivision.objects.get(
            name_fi=neighborhood_name,
            type=neighborhood_type
        )
        return division
    return None

def import_background_answers(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            age_low, age_high = age(row, 'ika')
            respondent = Respondent(
                id=int(row.get(
                    'user_id'
                )),
                property_id=int(row.get(
                    'propertyid'
                )),
                createtime=row.get(
                    'createtime'
                ),
                age_low=age_low,
                age_high=age_high,
                language=get_string(row,
                    'user-language'
                ),
                life_situation=get_string(row,
                    'elamantilanne-asumismuoto'
                ),
                neighborhood=get_neighborhood(
                    row, 'missa-kaupunginosassa-asut'
                ),
                nonlocal_home=get_string(row,
                    'jos-asut-muualla-kuin-helsingissa-missa-asu'
                ),
                transport_mode_first=get_string(row,
                    'tarkein'
                ),
                transport_mode_second=get_string(row,
                    'toiseksi-tarkein'
                ),
                transport_mode_third=get_string(row,
                    'kolmenneksi-tarkein'
                ),
                probability_stay_five_years=get_string(row,
                    'kuinka-todennakoisesti-asut-alueella-'
                    'viela-5-vuoden-kuluttua'
                ),
                scale_agree_high_rise=slider_value(row,
                    'min-erittain-korkea-asuinalue-sopii-helsinkiin'
                ),
                scale_enjoy_outdoors_large_woods=slider_value(row,
                    'min-mieluiten-ulkoilen-laajassa-metsassa-'
                    'vaikka-se-olisi-vahan-kauempana-kotoa'
                ),
                scale_enjoy_culture_urban_meetings=slider_value(row,
                    'min-kiinnostavin-uusi-kulttuuri-'
                    'syntyy-kohtaamisista-kaupungissa'
                ),
                scale_prefer_daily_shopping_near=slider_value(row,
                    'min-haluan-tehda-paivittaiset-ostokseni-'
                    'vahan-kerrallaan-lahella-kotia'
                ),
                scale_would_use_rail_transport_more=slider_value(row,
                    'min-jos-raideliikenteen-yhteyksia-parannetaan-'
                    'kayttaisin-raideliikennetta-nykyista-enemman-'
                    'seka-tyomatkoihini-etta-vapaa-ajalla'
                ),
                scale_agree_suburbs_build_near_stations=slider_value(row,
                    'min-esikaupungeissa-tehokkain-rakentaminen-'
                    'kannattaisi-keskittaa-asemien-laheisyyteen'
                ),
                scale_enjoy_metropolis_fascinating_possibilities=slider_value(
                    row,
                    'min-suurkaupunki-ja-sen-monet-mahdollisuudet-'
                    'ovat-kiehtovia'
                ),
                scale_agree_bulevardisation=slider_value(row,
                    'min-helsingin-keskustaan-johtavien-isojen-teiden-'
                    'muuttaminen-puistokaduiksi-on-hyva-idea'
                ),
                scale_agree_add_density=slider_value(row,
                    'min-koska-helsinki-kasvaa-pitaa-sita-tiiviistaa'
                ),
                scale_agree_add_my_area_density_for_less_cars=slider_value(row,
                    'min-autoilun-tarpeen-vahentamiseksi-olen-valmis-'
                    'hyvaksymaan-tiiviimpaa-rakentamista-asuinalueellani'
                ),
                scale_my_area_could_be_built_more=slider_value(row,
                    'min-asuinalueeltani-loytyy-viela-paikkoja-'
                    'joita-voisi-kayttaa-rakentamiseen'
                )
            )
            respondent.save()

def clean_text(head, tail):
    tail = tail.rstrip()
    if tail == 'x':
        tail = ''
    return (head + tail).replace('  LINEBREAK ', "\n")

def import_map_answers(filename):
    answers = []
    print('Reading answers.')
    with open(filename, 'r') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter="\t")
        for row in reader:
            text_content = clean_text(row.get('Kerro-lisää:'), row.get(''))
            try:
                respondent = Respondent.objects.get(pk=int(row.get('user_id')))
            except Respondent.DoesNotExist as e:
                respondent = None
            mapanswer = MapAnswer(
                id=int(row.get('feature_id')),
                respondent=respondent,
                createtime=row.get('createtime'),
                geometry_original=row.get('wkt'),
                category=row.get('valuename'),
                text_content=text_content
            )
            mapanswer.geometry = mapanswer.geometry_original.transform(
                4326, clone=True)
            answers.append(mapanswer)

    print('Bulk creating.')
    MapAnswer.objects.bulk_create(answers)
    connect_dots(MapAnswer.objects.all())

def connect_dots(answers):
    print('Connecting the dots.')
    for mapanswer in answers:
        if (mapanswer.geometry.geom_type == 'Point' or
            mapanswer.geometry.length == 0
        ):
            qs = AdministrativeDivisionGeometry.objects.filter(
                boundary__contains_properly=mapanswer.geometry)
        else:
            qs = AdministrativeDivisionGeometry.objects.filter(
                boundary__intersects=mapanswer.geometry)
        for d_geom in qs:
            if d_geom is not None:
                mapanswer.divisions.add(d_geom.division)
