def is_relevant(requirement, scenario):

    requirement_text = requirement["text"].lower()
    scenario_text = scenario["name"].lower()

    if "email" in requirement_text and "email" in scenario_text:
        return True

    if "password" in requirement_text and "password" in scenario_text:
        return True

    if "usb" in requirement_text and "usb" in scenario_text:
        return True

    if "incident" in requirement_text and "incident" in scenario_text:
        return True

    return False
