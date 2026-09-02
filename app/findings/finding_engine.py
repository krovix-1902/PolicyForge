def create_finding(test_result, control, risk):

    if test_result["result"] == "FAIL":
        severity = "HIGH"
    else:
        severity = "NONE"

    return {
        "id": "FINDING-001",
        "status": test_result["result"],
        "requirement_id": test_result["requirement_id"],
        "scenario": test_result["scenario"],
        "expected": test_result["expected"],
        "actual": test_result["actual"],
        "control": control,
        "risk": risk,
        "severity": severity
    }
