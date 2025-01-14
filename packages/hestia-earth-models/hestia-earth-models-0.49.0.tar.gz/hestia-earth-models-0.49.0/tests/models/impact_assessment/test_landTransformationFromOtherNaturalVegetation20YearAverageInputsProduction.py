from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_indicator, fake_load_impacts

from hestia_earth.models.impact_assessment.landTransformationFromOtherNaturalVegetation20YearAverageInputsProduction import (  # noqa: E501
    TERM_ID, run
)

class_path = f"hestia_earth.models.impact_assessment.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/impact_assessment/{TERM_ID}"


@patch('hestia_earth.models.utils.input.load_impacts', side_effect=fake_load_impacts)
@patch('hestia_earth.models.impact_assessment.utils._new_indicator', side_effect=fake_new_indicator)
def test_run(*args):
    with open(f"{fixtures_folder}/impact-assessment.jsonld", encoding='utf-8') as f:
        impact = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(impact)
    assert value == expected
