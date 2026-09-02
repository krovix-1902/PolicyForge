def make_decision(persona, scenario):

    if scenario["name"] == "Suspicious Email":
        if persona["security_knowledge"] == "High":
            return "Do not click and report the email."
        else:
            return "Click the link to check the email."

    if scenario["name"] == "Password Request":
        return "Do not share the password."

    if scenario["name"] == "Confidential AI Request":
        if persona["security_knowledge"] == "Low":
            return "Use the AI tool with the company information."
        else:
            return "Do not enter the confidential information."

    if scenario["name"] == "Unknown USB":
        if persona["security_knowledge"] == "High":
            return "Do not connect the USB."
        else:
            return "Connect the USB to see what is on it."

    if scenario["name"] == "Lost Laptop":
        return "Report the lost laptop to IT."

    return "I am not sure what to do."
