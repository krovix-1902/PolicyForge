def create_requirement(rule_id, text, rule_type, topic):
    return {
        "id": rule_id,
        "text": text,
        "type": rule_type,
        "topic": topic,
        "ambiguity": "LOW",
        "testable": "YES"
    }


def check_ambiguity(text):
    words = [
        "as soon as possible",
        "appropriate",
        "reasonable",
        "regularly",
        "quickly",
        "suspicious",
        "sensitive"
    ]

    for word in words:
        if word in text.lower():
            return "HIGH"

    return "LOW"


def get_topic(text):
    text = text.lower()

    if "public ai" in text:
        return "generative_ai"

    if "phishing" in text or "suspicious email" in text:
        return "phishing"

    if "password" in text:
        return "passwords"

    if "confidential company information" in text:
        return "confidential_data"

    if "usb" in text:
        return "usb_devices"

    if "approved devices" in text or "remotely" in text:
        return "remote_working"

    if "lost" in text and "device" in text:
        return "lost_devices"

    if "security incident" in text:
        return "security_incidents"

    if "public wi-fi" in text:
        return "public_wifi"

    if "unauthorised software" in text:
        return "software"

    return "unknown"


def get_expected_action(topic, text):
    text = text.lower()

    if topic == "phishing":
        if "report suspicious emails" in text:
            return "REPORT_EMAIL"
        return "DO_NOT_CLICK"

    actions = {
        "passwords": "DO_NOT_SHARE",
        "confidential_data": "DO_NOT_SHARE",
        "generative_ai": "DO_NOT_ENTER",
        "usb_devices": "DO_NOT_CONNECT",
        "remote_working": "USE_APPROVED_DEVICE",
        "lost_devices": "REPORT_LOST_DEVICE",
        "security_incidents": "REPORT_INCIDENT",
        "public_wifi": "USE_SECURITY_PROTECTION",
        "software": "DO_NOT_INSTALL"
    }

    return actions.get(topic, "UNKNOWN")


def extract_requirements(policy):
    requirements = []
    number = 1

    for line in policy.splitlines():
        line = line.strip()

        if "must not" in line.lower():
            rule_type = "PROHIBITED"

        elif "must" in line.lower():
            rule_type = "REQUIRED"

        elif "should" in line.lower():
            rule_type = "RECOMMENDED"

        else:
            continue

        topic = get_topic(line)

        requirement = create_requirement(
            f"REQ-{number:03}",
            line,
            rule_type,
            topic
        )

        requirement["expected_action"] = get_expected_action(
            topic,
            line
        )

        requirement["ambiguity"] = check_ambiguity(line)

        requirements.append(requirement)
        number += 1

    return requirements
