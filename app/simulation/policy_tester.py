def get_behaviour(text):

    text = text.lower()

    if "click" in text and "do not" in text:
        return "DO_NOT_CLICK"

    if "click" in text:
        return "CLICK"

    if "share" in text and "do not" in text:
        return "DO_NOT_SHARE"

    if "share" in text:
        return "SHARE"

    if "report" in text:
        return "REPORT"

    if "connect" in text and "do not" in text:
        return "DO_NOT_CONNECT"

    if "connect" in text:
        return "CONNECT"

    return "UNKNOWN"


def test_policy(requirement, scenario, decision):

    expected = get_behaviour(scenario["expected_action"])
    actual = get_behaviour(decision)

    if expected == actual:
        result = "PASS"
    else:
        result = "FAIL"

    return {
        "requirement_id": requirement["id"],
        "scenario": scenario["name"],
        "expected": expected,
        "actual": actual,
        "result": result
    }
