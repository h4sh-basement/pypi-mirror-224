"""
Compute Annual value based on Monthly values.
"""
from hestia_earth.schema import MeasurementStatsDefinition, MeasurementMethodClassification
from hestia_earth.utils.tools import flatten

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from .utils import _slice_by_year
from . import MODEL

REQUIREMENTS = {
    "Site": {
        "measurements": [
            {"@type": "Measurement", "term.id": "temperatureMonthly"}
        ]
    }
}
RETURNS = {
    "Measurement": [{
        "value": "",
        "startDate": "",
        "endDate": "",
        "statsDefinition": "modelled",
        "methodClassification": "modelled using other physical measurements"
    }]
}
TERM_ID = 'temperatureAnnual'
MEASUREMENT_ID = 'temperatureMonthly'


def _measurement(value: float, start_date: str, end_date: str):
    data = _new_measurement(TERM_ID)
    data['value'] = [value]
    data['startDate'] = start_date
    data['endDate'] = end_date
    data['statsDefinition'] = MeasurementStatsDefinition.MODELLED.value
    data['methodClassification'] = MeasurementMethodClassification.MODELLED_USING_OTHER_PHYSICAL_MEASUREMENTS.value
    return data


def _run(measurement: dict):
    values = measurement.get('value', [])
    dates = measurement.get('dates', [])
    term_id = measurement.get('term', {}).get('@id')
    results = _slice_by_year(term_id, dates, values)
    return [_measurement(value, start_date, end_date) for (value, start_date, end_date) in results]


def _should_run(site: dict):
    measurements = [m for m in site.get('measurements', []) if m.get('term', {}).get('@id') == MEASUREMENT_ID]
    has_monthly_measurements = len(measurements) > 0

    logRequirements(site, model=MODEL, term=TERM_ID,
                    has_monthly_measurements=has_monthly_measurements)

    should_run = all([has_monthly_measurements])
    logShouldRun(site, MODEL, TERM_ID, should_run)
    return should_run, measurements


def run(site: dict):
    should_run, measurements = _should_run(site)
    return flatten(map(_run, measurements)) if should_run else []
