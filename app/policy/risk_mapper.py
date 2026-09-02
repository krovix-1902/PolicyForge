def map_risk(requirement):

    text = requirement["text"].lower()

    if "phishing" in text or "email" in text:
        return "RISK-001"

    if "password" in text or "credential" in text:
        return "RISK-002"

    if "confidential" in text or "company information" in text:
        return "RISK-003"

    if "usb" in text or "software" in text:
        return "RISK-004"

    if "incident" in text or "report" in text:
        return "RISK-005"

    return "RISK-005"
