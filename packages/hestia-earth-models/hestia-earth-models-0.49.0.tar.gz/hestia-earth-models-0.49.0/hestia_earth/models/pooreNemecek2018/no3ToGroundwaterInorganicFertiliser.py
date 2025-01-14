from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition

from hestia_earth.models.utils.cycle import get_inorganic_fertiliser_N_total
from hestia_earth.models.utils.emission import _new_emission
from .no3ToGroundwaterSoilFlux import _should_run, _get_value
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "completeness.products": "",
        "completeness.cropResidue": "True",
        "completeness.fertiliser": "",
        "products": [{
            "@type": "Product",
            "value": "",
            "term.termType": ["cropResidue", "excreta"],
            "properties": [{"@type": "Property", "value": "", "term.@id": "nitrogenContent"}]
        }],
        "inputs": [{
            "@type": "Input",
            "value": "",
            "term.units": ["kg", "kg N"],
            "term.termType": ["organicFertiliser", "inorganicFertiliser", "excreta"],
            "optional": {
                "properties": [{"@type": "Property", "value": "", "term.@id": "nitrogenContent"}]
            }
        }],
        "site": {
            "@type": "Site",
            "measurements": [
                {"@type": "Measurement", "value": "", "term.@id": "clayContent"},
                {"@type": "Measurement", "value": "", "term.@id": "sandContent"},
                {"@type": "Measurement", "value": "", "term.@id": [
                    "precipitationAnnual", "precipitationLongTermAnnualMean"
                ]}
            ]
        }
    }
}
RETURNS = {
    "Emission": [{
        "value": "",
        "methodTier": "tier 2",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'no3ToGroundwaterInorganicFertiliser'
TIER = EmissionMethodTier.TIER_2.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _run(cycle: dict, N_total: float, content_list_of_items: list):
    no3ToGroundwaterSoilFlux = _get_value(cycle, N_total, content_list_of_items, TERM_ID)
    N_inorganic_fertiliser = get_inorganic_fertiliser_N_total(cycle)
    return [_emission(N_inorganic_fertiliser / N_total * no3ToGroundwaterSoilFlux if N_total > 0 else 0)]


def run(cycle: dict):
    should_run, N_total, content_list_of_items = _should_run(cycle, TERM_ID, TIER)
    return _run(cycle, N_total, content_list_of_items) if should_run else []
