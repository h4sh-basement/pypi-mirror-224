"""
Flowing Water

This model returns a measurement of fast flowing water or slow flowing water depending on the type of the site.
"""
from hestia_earth.schema import MeasurementStatsDefinition, MeasurementMethodClassification, SiteSiteType

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from hestia_earth.models.utils.site import WATER_TYPES
from . import MODEL

REQUIREMENTS = {
    "Site": {
        "siteType": ["pond", "river or stream", "lake", "sea or ocean"]
    }
}
RETURNS = {
    "Measurement": [{
        "value": "1",
        "statsDefinition": "modelled",
        "methodClassification": "modelled using other physical measurements"
    }]
}
TERM_ID = 'slowFlowingWater,fastFlowingWater'
BIBLIO_TITLE = 'Reducing food’s environmental impacts through producers and consumers'
SITE_TYPE_TO_TERM_ID = {
    SiteSiteType.RIVER_OR_STREAM.value: 'fastFlowingWater'
}


def measurement(term_id: str):
    data = _new_measurement(term_id, None, BIBLIO_TITLE)
    data['value'] = [1]
    data['statsDefinition'] = MeasurementStatsDefinition.MODELLED.value
    data['methodClassification'] = MeasurementMethodClassification.MODELLED_USING_OTHER_PHYSICAL_MEASUREMENTS.value
    return data


def _run(site: dict):
    site_type = site.get('siteType')
    term_id = SITE_TYPE_TO_TERM_ID.get(site_type, 'slowFlowingWater')
    return measurement(term_id)


def _should_run(site: dict):
    site_type = site.get('siteType')

    logRequirements(site, model=MODEL, term=TERM_ID,
                    site_type=site_type)

    should_run = site_type in WATER_TYPES
    logShouldRun(site, MODEL, TERM_ID, should_run)
    return should_run


def run(site: dict): return _run(site) if _should_run(site) else None
