from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.cycle import land_occupation_per_ha
from .utils import get_emission_factor
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "or": [
            {
                "@doc": "if the [cycle.functionalUnit](https://hestia.earth/schema/Cycle#functionalUnit) = 1 ha, additional properties are required",  # noqa: E501
                "cycleDuration": "",
                "products": [{
                    "@type": "Product",
                    "primary": "True",
                    "value": "> 0",
                    "economicValueShare": "> 0"
                }],
                "site": {
                    "@type": "Site",
                    "practices": [{"@type": "Practice", "value": "", "term.@id": "longFallowRatio"}]
                }
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
        ],
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"}
        }
    }
}
LOOKUPS = {
    "crop": ["isOrchard", "cropGroupingFaostatArea"],
    "region-crop-cropGroupingFaostatArea-n2oforestBiomassBurning": "use crop grouping above or default to site.siteType"
}
RETURNS = {
    "Emission": [{
        "value": "",
        "methodTier": "tier 1",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'n2OToAirNaturalVegetationBurningDirect'
TIER = EmissionMethodTier.TIER_1.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _run(land_occupation: float, n2o_forest_biomass_burning: float):
    value = land_occupation * n2o_forest_biomass_burning
    return [_emission(value)]


def _should_run(cycle: dict):
    land_occupation = land_occupation_per_ha(MODEL, TERM_ID, cycle)
    n2o_forest_biomass_burning = get_emission_factor(TERM_ID, cycle, 'n2oforestBiomassBurning')

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    land_occupation=land_occupation,
                    n2o_forest_biomass_burning=n2o_forest_biomass_burning)

    should_run = all([land_occupation, n2o_forest_biomass_burning is not None])
    logShouldRun(cycle, MODEL, TERM_ID, should_run, methodTier=TIER)
    return should_run, land_occupation, n2o_forest_biomass_burning


def run(cycle: dict):
    should_run, land_occupation, n2o_forest_biomass_burning = _should_run(cycle)
    return _run(land_occupation, n2o_forest_biomass_burning) if should_run else []
