def test_policy(requirement, scenario, decision):

    expected = requirement["expected_action"]

    decision_actions = {
        "Click the link to check the email.": "CLICK",
        "Do not click and report the email.": "DO_NOT_CLICK",
        "Report the suspicious email.": "REPORT_EMAIL",
        "Ignore the suspicious email.": "IGNORE_EMAIL",
        "Do not share the password.": "DO_NOT_SHARE",
        "Use the AI tool with the company information.": "DO_NOT_ENTER",
        "Do not enter the confidential information.": "DO_NOT_ENTER",
        "Connect the USB to see what is on it.": "CONNECT",
        "Do not connect the USB.": "DO_NOT_CONNECT",
        "Report the lost laptop to IT.": "REPORT_LOST_DEVICE"
    }

    actual = decision_actions.get(decision, "UNKNOWN")

    if actual == expected:
        result = "PASS"
    else:
        result = "FAIL"

    return {
        "result": result,
        "requirement_id": requirement["id"],
        "scenario": scenario["name"],
        "expected": expected,
        "actual": actual
    }
