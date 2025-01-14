from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils import sum_values, multiply_values
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.impact_assessment import convert_value_from_cycle, get_product, get_site
from hestia_earth.models.utils.cycle import land_occupation_per_kg
from hestia_earth.models.utils.input import sum_input_impacts
from .utils import get_region_factor
from . import MODEL

REQUIREMENTS = {
    "ImpactAssessment": {
        "site": {
            "@type": "Site",
            "siteType": "",
            "or": {
                "ecoregion": "",
                "country": {"@type": "Term", "termType": "region"}
            }
        },
        "cycle": {
            "@type": "Cycle",
            "products": [{
                "@type": "Product",
                "primary": "True",
                "value": "> 0",
                "economicValueShare": "> 0"
            }],
            "or": [
                {
                    "@doc": "if the [cycle.functionalUnit](https://hestia.earth/schema/Cycle#functionalUnit) = 1 ha, additional properties are required",  # noqa: E501
                    "cycleDuration": "",
                    "practices": [{"@type": "Practice", "value": "", "term.@id": "longFallowRatio"}]
                },
                {
                    "@doc": "for orchard crops, additional properties are required",
                    "inputs": [
                        {"@type": "Input", "value": "", "term.@id": "saplings"}
                    ],
                    "practices": [
                        {"@type": "Practice", "value": "", "term.@id": "nurseryDuration"},
                        {"@type": "Practice", "value": "", "term.@id": "orchardBearingDuration"},
                        {"@type": "Practice", "value": "", "term.@id": "orchardDensity"},
                        {"@type": "Practice", "value": "", "term.@id": "orchardDuration"},
                        {"@type": "Practice", "value": "", "term.@id": "rotationDuration"}
                    ]
                }
            ]
        }
    }
}
RETURNS = {
    "Indicator": {
        "value": ""
    }
}
LOOKUPS = {
    "@doc": "Different lookup files are used depending on the situation",
    "ecoregion-siteType-LandOccupationChaudaryBrooks2018CF": "using `ecoregion`",
    "region-siteType-LandOccupationChaudaryBrooks2018CF": "using `country`"
}
TERM_ID = 'damageToTerrestrialEcosystemsLandOccupation'
LOOKUP_SUFFIX = 'LandOccupationChaudaryBrooks2018CF'


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def _run(impact_assessment: dict):
    cycle = impact_assessment.get('cycle', {})
    product = get_product(impact_assessment)
    site = get_site(impact_assessment)
    land_occupation_m2_kg = land_occupation_per_kg(MODEL, TERM_ID, cycle, site, product)
    factor = get_region_factor(TERM_ID, impact_assessment, LOOKUP_SUFFIX, 'medium_intensity')
    inputs_value = convert_value_from_cycle(
        product, sum_input_impacts(cycle.get('inputs', []), TERM_ID), model=MODEL, term_id=TERM_ID
    )
    logRequirements(impact_assessment, model=MODEL, term=TERM_ID,
                    landOccupation=land_occupation_m2_kg,
                    factor=factor,
                    inputs_value=inputs_value)
    value = sum_values([
        multiply_values([land_occupation_m2_kg, factor]),
        inputs_value
    ])
    return _indicator(value)


def _should_run(impact_assessment: dict):
    site = get_site(impact_assessment)
    # does not run without a site as data is geospatial
    should_run = all([site])
    logShouldRun(impact_assessment, MODEL, TERM_ID, should_run)
    return should_run


def run(impact_assessment: dict):
    return _run(impact_assessment) if _should_run(impact_assessment) else None
