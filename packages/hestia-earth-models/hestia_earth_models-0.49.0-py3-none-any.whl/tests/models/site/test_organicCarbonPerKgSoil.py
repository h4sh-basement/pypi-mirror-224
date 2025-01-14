from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_measurement

from hestia_earth.models.site.organicCarbonPerKgSoil import MODEL, TERM_ID, run, _should_run

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


@patch(f"{class_path}.find_term_match")
def test_should_run(mock_find):
    # no measurement => no run
    mock_find.return_value = {}
    should_run, *args = _should_run({})
    assert not should_run

    # with measurement => run
    mock_find.return_value = {'value': [10]}
    should_run, *args = _should_run({})
    assert should_run is True


@patch(f"hestia_earth.models.{MODEL}.utils._new_measurement", side_effect=fake_new_measurement)
def test_run(*args):
    with open(f"{fixtures_folder}/site.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(site)
    assert value == expected
