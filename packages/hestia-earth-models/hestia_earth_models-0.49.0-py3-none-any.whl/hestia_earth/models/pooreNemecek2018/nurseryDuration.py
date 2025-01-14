from hestia_earth.schema import PracticeStatsDefinition
from hestia_earth.utils.tools import safe_parse_float

from hestia_earth.models.utils.practice import _new_practice
from hestia_earth.models.utils.crop import get_crop_lookup_value
from .utils import run_products_average
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{"@type": "Product", "value": "", "term.termType": "crop"}],
        "site": {"@type": "Site", "siteType": "cropland"}
    }
}
LOOKUPS = {
    "crop": "Nursery_duration"
}
RETURNS = {
    "Practice": [{
        "value": "",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'nurseryDuration'


def _get_value(product: dict):
    term_id = product.get('term', {}).get('@id', '')
    return safe_parse_float(get_crop_lookup_value(MODEL, TERM_ID, term_id, LOOKUPS['crop']), None)


def _practice(value: float):
    practice = _new_practice(TERM_ID, MODEL)
    practice['value'] = [value]
    practice['statsDefinition'] = PracticeStatsDefinition.MODELLED.value
    return practice


def run(cycle: dict):
    value = run_products_average(cycle, TERM_ID, _get_value)
    return [_practice(value)] if value is not None else []
