from .utils import run_inputs_production

REQUIREMENTS = {
    "ImpactAssessment": {
        "product": {"@type": "Term"},
        "cycle": {
            "@type": "Cycle",
            "products": [{
                "@type": "Product",
                "primary": "True",
                "value": "> 0",
                "economicValueShare": "> 0"
            }],
            "inputs": [{
                "@type": "Input",
                "impactAssessment": {
                    "@type": "ImpactAssessment",
                    "emissionsResourceUse": [{
                        "@type": "Indicator",
                        "term.@id": "landTransformationFromCropland20YearAverageDuringCycle",
                        "value": "> 0"
                    }]
                }
            }]
        }
    }
}
RETURNS = {
    "Indicator": [{
        "value": ""
    }]
}
TERM_ID = 'landTransformationFromCropland20YearAverageInputsProduction'


def run(impact_assessment: dict): return run_inputs_production(impact_assessment, TERM_ID)
