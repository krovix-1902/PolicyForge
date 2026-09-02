def map_requirement(requirement):

    text = requirement["text"].lower()

    if "phishing" in text or "email" in text:
        return "CTRL-002"

    if "password" in text or "credential" in text:
        return "CTRL-003"

    if "confidential" in text or "company information" in text:
        return "CTRL-004"

    if "usb" in text or "software" in text or "device" in text:
        return "CTRL-005"

    if "incident" in text or "report" in text:
        return "CTRL-006"

    return "CTRL-001"
