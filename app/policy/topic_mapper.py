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
