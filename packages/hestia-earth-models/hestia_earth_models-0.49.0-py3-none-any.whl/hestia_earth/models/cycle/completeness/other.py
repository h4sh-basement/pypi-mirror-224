"""
Completeness Other

This model checks if we have the requirements below and updates the
[Data Completeness](https://hestia.earth/schema/Completeness#other) value.
"""
from hestia_earth.schema import SiteSiteType
from hestia_earth.utils.model import find_term_match, find_primary_product

from hestia_earth.models.log import logRequirements
from hestia_earth.models.utils.crop import is_orchard
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "completeness.other": "False",
        "inputs": [
            {"@type": "Input", "value": "", "term.@id": ["seed", "saplings"]}
        ],
        "site": {
            "@type": "Site",
            "siteType": ["cropland", "glass or high accessible cover"]
        }
    }
}
RETURNS = {
    "Completeness": {
        "other": ""
    }
}
LOOKUPS = {
    "crop": "isOrchard"
}
MODEL_KEY = 'other'
ALLOWED_SITE_TYPES = [
    SiteSiteType.CROPLAND.value,
    SiteSiteType.GLASS_OR_HIGH_ACCESSIBLE_COVER.value
]


def run(cycle: dict):
    site_type = cycle.get('site', {}).get('siteType')
    site_type_allowed = site_type in ALLOWED_SITE_TYPES

    has_seed = find_term_match(cycle.get('inputs', []), 'seed', None)

    product = find_primary_product(cycle) or {}
    term_id = product.get('term', {}).get('@id')
    has_saplings = find_term_match(cycle.get('inputs', []), 'saplings', None) and is_orchard(MODEL, None, term_id)

    logRequirements(cycle, model=MODEL, term=None, key=MODEL_KEY,
                    site_type_allowed=site_type_allowed,
                    has_seed=has_seed,
                    has_saplings=has_saplings)

    return all([site_type_allowed, has_seed or has_saplings])
