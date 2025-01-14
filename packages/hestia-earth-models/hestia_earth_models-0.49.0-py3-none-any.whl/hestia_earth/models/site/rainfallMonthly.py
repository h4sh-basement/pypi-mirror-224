"""
Compute Monthly value based on Daily values.
"""
from hestia_earth.schema import MeasurementStatsDefinition, MeasurementMethodClassification
from hestia_earth.utils.tools import flatten

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from .utils import _group_by_month
from . import MODEL

REQUIREMENTS = {
    "Site": {
        "measurements": [
            {"@type": "Measurement", "term.id": "rainfallDaily"}
        ]
    }
}
RETURNS = {
    "Measurement": [{
        "value": "",
        "dates": "",
        "statsDefinition": "modelled",
        "methodClassification": "modelled using other physical measurements"
    }]
}
TERM_ID = 'rainfallMonthly'
MEASUREMENT_ID = 'rainfallDaily'


def _measurement(value: list, dates: list):
    data = _new_measurement(TERM_ID)
    data['value'] = value
    data['dates'] = dates
    data['statsDefinition'] = MeasurementStatsDefinition.MODELLED.value
    data['methodClassification'] = MeasurementMethodClassification.MODELLED_USING_OTHER_PHYSICAL_MEASUREMENTS.value
    return data


def _run(measurement: dict):
    values = measurement.get('value', [])
    dates = measurement.get('dates', [])
    term_id = measurement.get('term', {}).get('@id')
    result = _group_by_month(term_id, dates, values)
    return _measurement(result[0], result[1]) if len(result[0]) > 0 else None


def _should_run(site: dict):
    measurements = [m for m in site.get('measurements', []) if m.get('term', {}).get('@id') == MEASUREMENT_ID]
    has_daily_measurements = len(measurements) > 0

    logRequirements(site, model=MODEL, term=TERM_ID,
                    has_daily_measurements=has_daily_measurements)

    should_run = all([has_daily_measurements])
    logShouldRun(site, MODEL, TERM_ID, should_run)
    return should_run, measurements


def run(site: dict):
    should_run, measurements = _should_run(site)
    return flatten(map(_run, measurements)) if should_run else []
