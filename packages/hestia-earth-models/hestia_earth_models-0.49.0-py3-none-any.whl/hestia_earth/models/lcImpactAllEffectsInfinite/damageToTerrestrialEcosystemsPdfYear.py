from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.impact_assessment import impact_endpoint_value
from . import MODEL

REQUIREMENTS = {
    "ImpactAssessment": {
        "impacts": [{
            "@type": "Indicator",
            "value": "",
            "methodModel": {"@type": "Term", "@id": "lcImpactAllEffectsInfinite"}
        }]
    }
}
RETURNS = {
    "Indicator": {
        "value": ""
    }
}
LOOKUPS = {
    "characterisedIndicator": "pdfYearsDamageToTerrestrialEcosystemsLCImpact"
}
TERM_ID = 'damageToTerrestrialEcosystemsPdfYear'


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def run(impact_assessment: dict):
    value = impact_endpoint_value(MODEL, TERM_ID, impact_assessment, LOOKUPS['characterisedIndicator'])
    logRequirements(impact_assessment, model=MODEL, term=TERM_ID,
                    value=value)
    logShouldRun(impact_assessment, MODEL, TERM_ID, True)
    return _indicator(value)
