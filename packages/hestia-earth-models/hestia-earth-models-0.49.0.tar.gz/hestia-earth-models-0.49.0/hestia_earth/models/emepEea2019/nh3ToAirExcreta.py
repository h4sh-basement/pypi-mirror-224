from hestia_earth.schema import EmissionMethodTier, TermTermType, EmissionStatsDefinition
from hestia_earth.utils.lookup import column_name, download_lookup, get_table_value
from hestia_earth.utils.model import filter_list_term_type
from hestia_earth.utils.tools import safe_parse_float, list_sum

from hestia_earth.models.log import logRequirements, debugMissingLookup, logShouldRun
from hestia_earth.models.utils import _filter_list_term_unit
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import total_excreta_tan
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "inputs": [{
            "@type": "Input",
            "value": "",
            "term.termType": "excreta",
            "term.units": "kg N",
            "properties": [
                {"@type": "Property", "value": "", "term.@id": "totalAmmoniacalNitrogenContentAsN"}
            ]
        }],
        "practices": [
            {"@type": "Practice", "value": "", "term.termType": "excretaManagement"}
        ]
    }
}
LOOKUPS = {
    "excretaManagement-excreta-NH3_EF_2019": "product @id"
}
RETURNS = {
    "Emission": [{
        "value": "",
        "methodTier": "tier 2",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'nh3ToAirExcreta'
TIER = EmissionMethodTier.TIER_2.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _get_nh3_factor(term_id: str, input: dict):
    input_term_id = input.get('term', {}).get('@id')
    lookup_name = f"{list(LOOKUPS.keys())[0]}.csv"
    value = get_table_value(download_lookup(lookup_name), 'termid', term_id, column_name(input_term_id))
    debugMissingLookup(lookup_name, 'termid', term_id, input_term_id, value, model=MODEL, term=TERM_ID)
    return safe_parse_float(value, None)


def _run(excreta_EF_product: float):
    value = excreta_EF_product * get_atomic_conversion(Units.KG_NH3, Units.TO_N)
    return [_emission(value)]


def _should_run(cycle: dict):
    practices = filter_list_term_type(cycle.get('practices', []), TermTermType.EXCRETAMANAGEMENT)
    practice_id = practices[0].get('term', {}).get('@id') if len(practices) > 0 else None

    # total of excreta including the NH3 factor
    excreta = filter_list_term_type(cycle.get('inputs', []), TermTermType.EXCRETA)
    excreta = _filter_list_term_unit(excreta, Units.KG_N)
    excreta_values = [
        (i.get('term', {}).get('@id'), total_excreta_tan([i]), _get_nh3_factor(practice_id, i)) for i in excreta
    ]
    excreta_logs = ';'.join([f"id:{id}_value:{v}_EF:{f}" for id, v, f in excreta_values])
    excreta_EF_products = [v * f for id, v, f in excreta_values if f is not None]
    has_excreta_EF_products = len(excreta_EF_products) > 0
    excreta_EF_product = list_sum(excreta_EF_products)

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    practice_id=practice_id,
                    excreta=excreta_logs,
                    excreta_EF_product=excreta_EF_product,
                    has_excreta_EF_products=has_excreta_EF_products)

    should_run = all([has_excreta_EF_products])
    logShouldRun(cycle, MODEL, TERM_ID, should_run, methodTier=TIER)
    return should_run, excreta_EF_product


def run(cycle: dict):
    should_run, excreta_EF_product = _should_run(cycle)
    return _run(excreta_EF_product) if should_run else []
