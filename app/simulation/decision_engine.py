def make_decision(persona, scenario, requirement):

    topic = requirement["topic"]
    knowledge = persona["security_knowledge"]

    if topic == "phishing":

        if requirement["id"] == "REQ-001":
            if knowledge == "High":
                return "Do not click and report the email."
            else:
                return "Click the link to check the email."

        if requirement["id"] == "REQ-002":
            if knowledge == "High":
                return "Report the suspicious email."
            else:
                return "Ignore the suspicious email."

    if topic == "passwords":
        return "Do not share the password."

    if topic == "generative_ai":
        if knowledge == "Low":
            return "Use the AI tool with the company information."
        else:
            return "Do not enter the confidential information."

    if topic == "usb_devices":
        if knowledge == "High":
            return "Do not connect the USB."
        else:
            return "Connect the USB to see what is on it."

    if topic == "lost_devices":
        return "Report the lost laptop to IT."

    return "I am not sure what to do."
