scenarios = [
    {
        "name": "Suspicious Email",
        "situation": "You receive an email asking you to click a link to verify your company account.",
        "expected_action": "Do not click the link and report the email."
    },
    {
        "name": "Password Request",
        "situation": "A colleague asks you to send them your password because they need to access your account.",
        "expected_action": "Do not share your password."
    },
    {
        "name": "Confidential AI Request",
        "situation": "You want to paste confidential company information into a public AI chatbot to help with your work.",
        "expected_action": "Do not enter the confidential information."
    },
    {
        "name": "Unknown USB",
        "situation": "You find an unknown USB drive and want to connect it to your work computer.",
        "expected_action": "Do not connect the USB device."
    },
    {
        "name": "Lost Laptop",
        "situation": "You realise that your company laptop has been lost while travelling.",
        "expected_action": "Report the lost device to the IT team."
    }
]


def show_scenarios():
    for scenario in scenarios:
        print()
        print(scenario["name"])
        print("Situation:", scenario["situation"])
        print("Expected:", scenario["expected_action"])
