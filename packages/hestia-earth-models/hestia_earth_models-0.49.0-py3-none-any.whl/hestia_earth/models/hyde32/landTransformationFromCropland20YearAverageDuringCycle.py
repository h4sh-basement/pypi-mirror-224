from hestia_earth.schema import SiteSiteType

from .utils import run_land_transformation

REQUIREMENTS = {
    "ImpactAssessment": {
        "or": {
            "country": {"@type": "Term", "termType": "region"},
            "site": {
                "@type": "Site",
                "region": {"@type": "Term", "termType": "region"}
            }
        },
        "endDate": "",
        "product": {"@type": "Term"},
        "cycle": {
            "@type": "Cycle",
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
LOOKUPS = {
    "@doc": "One of (depending on `site.siteType`)",
    "region-forest-landTransformation20years": "cropland",
    "region-permanent_pasture-landTransformation20years": "cropland",
    "region-other_natural_vegetation-landTransformation20years": "cropland"
}
RETURNS = {
    "Indicator": [{
        "value": ""
    }]
}
TERM_ID = 'landTransformationFromCropland20YearAverageDuringCycle'


def run(impact_assessment: dict): return run_land_transformation(impact_assessment, TERM_ID, SiteSiteType.CROPLAND)
