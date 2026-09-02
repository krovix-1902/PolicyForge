from app.policy.control_mapper import map_requirement
from app.policy.risk_mapper import map_risk


def create_test_case(requirement):

    return {
        "id": "TEST-" + requirement["id"].replace("REQ-", ""),
        "requirement": requirement,
        "control": map_requirement(requirement),
        "risk": map_risk(requirement)
    }


def build_test_cases(requirements):

    test_cases = []

    for requirement in requirements:
        test_cases.append(
            create_test_case(requirement)
        )

    return test_cases
