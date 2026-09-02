personas = [
    {
        "name": "Alex",
        "role": "Marketing Employee",
        "security_knowledge": "Low"
    },
    {
        "name": "Sam",
        "role": "Software Developer",
        "security_knowledge": "High"
    },
    {
        "name": "Jordan",
        "role": "New Employee",
        "security_knowledge": "Low"
    },
    {
        "name": "Taylor",
        "role": "Finance Employee",
        "security_knowledge": "Medium"
    },
    {
        "name": "Morgan",
        "role": "Remote Employee",
        "security_knowledge": "Medium"
    }
]


def show_personas():
    for persona in personas:
        print(
            persona["name"],
            "-",
            persona["role"],
            "- Security knowledge:",
            persona["security_knowledge"]
        )
