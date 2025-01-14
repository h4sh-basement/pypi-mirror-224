from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition

from hestia_earth.models.log import debugValues, logRequirements, logShouldRun
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.measurement import most_relevant_measurement_value
from .utils import get_pcorr, get_p_ef_c1, get_ef_p_c2, get_practice_factor, get_water, calculate_R, calculate_A
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "endDate": "",
        "inputs": [
            {"@type": "Input", "value": "", "term.termType": "water"}
        ],
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"},
            "measurements": [
                {"@type": "Measurement", "value": "", "term.@id": "nutrientLossToAquaticEnvironment"},
                {"@type": "Measurement", "value": "", "term.@id": "heavyWinterPrecipitation"},
                {"@type": "Measurement", "value": "", "term.@id": "totalNitrogenPerKgSoil"},
                {"@type": "Measurement", "value": "", "term.@id": "precipitationAnnual"},
                {"@type": "Measurement", "value": "", "term.@id": "erodibility"},
                {"@type": "Measurement", "value": "", "term.@id": "slopeLength"},
                {"@type": "Measurement", "value": "", "term.@id": "slope"}
            ]
        }
    }
}
RETURNS = {
    "Emission": [{
        "value": "",
        "methodTier": "tier 1",
        "statsDefinition": "modelled"
    }]
}
LOOKUPS = {
    "region": ["P_EF_C1", "EF_P_C2", "Practice_Factor"],
    "tillage": "C2_FACTORS",
    "organicFertiliser": "OrganicFertiliserClassification"
}
TERM_ID = 'nErosionSoilFlux'
TIER = EmissionMethodTier.TIER_1.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _run(cycle: dict, list_of_contents_for_A: list, list_of_contents_for_R: list, list_of_contents_for_value: list):
    heavy_winter_precipitation, water = list_of_contents_for_R
    R = calculate_R(heavy_winter_precipitation, water)

    practice_factor, erodibility, slope_length, pcorr, p_ef_c1, ef_p_c2 = list_of_contents_for_A
    A = calculate_A(R, practice_factor, erodibility, slope_length, pcorr, p_ef_c1, ef_p_c2)

    nla_environment, N_content = list_of_contents_for_value
    debugValues(cycle, model=MODEL, term=TERM_ID,
                R=R,
                A=A,
                nla_environment=nla_environment,
                N_content=N_content)
    value = A * nla_environment / 100 * 2 * N_content
    return [_emission(value)]


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])

    def _get_measurement_content(term_id: str):
        return most_relevant_measurement_value(measurements, term_id, end_date)

    nla_environment = _get_measurement_content('nutrientLossToAquaticEnvironment')
    soil_nitrogen_content = _get_measurement_content('totalNitrogenPerKgSoil')
    erodibility = _get_measurement_content('erodibility')
    slope = _get_measurement_content('slope')
    slope_length = _get_measurement_content('slopeLength')
    heavy_winter_precipitation = _get_measurement_content('heavyWinterPrecipitation')

    precipitation = _get_measurement_content('precipitationAnnual')
    water = get_water(cycle, precipitation)

    practice_factor = get_practice_factor(site)
    pcorr = get_pcorr(slope / 100) if slope is not None else None
    p_ef_c1 = get_p_ef_c1(cycle)
    ef_p_c2 = get_ef_p_c2(cycle)

    list_of_contents_for_A = [
        practice_factor, erodibility, slope_length,
        pcorr, p_ef_c1, ef_p_c2]
    list_of_contents_for_R = [heavy_winter_precipitation, water]
    list_of_contents_for_value = [nla_environment, soil_nitrogen_content]

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    practice_factor=practice_factor,
                    erodibility=erodibility,
                    slope_length=slope_length,
                    pcorr=pcorr,
                    p_ef_c1=p_ef_c1,
                    ef_p_c2=ef_p_c2,
                    heavy_winter_precipitation=heavy_winter_precipitation,
                    water=water,
                    nla_environment=nla_environment,
                    soil_nitrogen_content=soil_nitrogen_content)

    should_run = all([
        all(list_of_contents_for_A),
        all(list_of_contents_for_R),
        all(list_of_contents_for_value)
    ])
    logShouldRun(cycle, MODEL, TERM_ID, should_run, methodTier=TIER)
    return should_run, list_of_contents_for_A, list_of_contents_for_R, list_of_contents_for_value


def run(cycle):
    should_run, list_of_contents_for_A, list_of_contents_for_R, list_of_contents_for_value = _should_run(cycle)
    return _run(cycle, list_of_contents_for_A, list_of_contents_for_R, list_of_contents_for_value) if should_run else []
