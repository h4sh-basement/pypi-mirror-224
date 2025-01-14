"""
Live Animal

This model calculates the amount of live animal produced during a Cycle, based on the amount of animal product.
"""
from hestia_earth.schema import TermTermType, ProductStatsDefinition, SiteSiteType
from hestia_earth.utils.model import find_primary_product, find_term_match
from hestia_earth.utils.tools import list_sum, safe_parse_float

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.product import _new_product
from hestia_earth.models.utils.term import get_lookup_value
from hestia_earth.models.utils.site import valid_site_type
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{
            "@type": "Product",
            "primary": "True",
            "value": "",
            "term.termType": "animalProduct",
            "properties": [{
                "@type": "Property",
                "value": "",
                "term.@id": [
                    "coldCarcassWeightPerHead",
                    "coldDressedCarcassWeightPerHead",
                    "liveweightPerHead",
                    "readyToCookWeightPerHead"
                ]
            }]
        }],
        "site": {
            "@type": "Site",
            "siteType": ["animal housing", "permanent pasture"]
        }
    }
}
RETURNS = {
    "Product": [{
        "term.termType": "liveAnimal",
        "value": "",
        "statsDefinition": "modelled"
    }]
}
MODEL_KEY = 'liveAnimal'
VALID_SITE_TYPES = [SiteSiteType.ANIMAL_HOUSING.value, SiteSiteType.PERMANENT_PASTURE.value]


def _product(term: str, value: float):
    product = _new_product(term, value)
    product['statsDefinition'] = ProductStatsDefinition.MODELLED.value
    return product


def _run(term_id: str, product_value: dict, propertyPerHead: float):
    value = product_value / propertyPerHead
    return [_product(term_id, value)] if value else []


def _get_liveAnimal_term_id(product: dict):
    return get_lookup_value(product.get('term', {}), MODEL_KEY, model=MODEL, model_key=MODEL_KEY)


def _should_run(cycle: dict):
    site_type_valid = valid_site_type(cycle.get('site'), site_types=VALID_SITE_TYPES)
    product = find_primary_product(cycle) or {}
    product_value = list_sum(product.get('value', []))
    is_animalProduct = product.get('term', {}).get('termType') == TermTermType.ANIMALPRODUCT.value
    units = f"{product.get('term', {}).get('units')} / head"
    property = next(
        (p for p in product.get('properties', []) if p.get('term', {}).get('units') == units), {}
    ) or next(
        (p for p in product.get('properties', []) if p.get('term', {}).get('@id').endswith('PerHead')), {}
    )
    propertyPerHead = safe_parse_float(property.get('value'), 0)

    # make sure the `liveAnimal` Term is not already present as a product
    term_id = _get_liveAnimal_term_id(product)
    has_liveAnimal_product = find_term_match(cycle.get('products', []), term_id, None) is not None

    logRequirements(cycle, model=MODEL, term=term_id, model_key=MODEL_KEY,
                    site_type_valid=site_type_valid,
                    is_animalProduct=is_animalProduct,
                    has_liveAnimal_product=has_liveAnimal_product,
                    product_value=product_value,
                    propertyPerHead=propertyPerHead)

    should_run = all([
        site_type_valid,
        term_id, is_animalProduct, not has_liveAnimal_product,
        product_value, propertyPerHead
    ])
    logShouldRun(cycle, MODEL, term_id, should_run, model_key=MODEL_KEY)
    return should_run, term_id, product_value, propertyPerHead


def run(cycle: dict):
    should_run, term_id, product_value, propertyPerHead = _should_run(cycle)
    return _run(term_id, product_value, propertyPerHead) if should_run else []
