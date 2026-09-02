def create_requirement(rule_id, text, rule_type):
    return {
        "id": rule_id,
        "text": text,
        "type": rule_type,
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

        requirement = create_requirement(
            f"REQ-{number:03}",
            line,
            rule_type
        )

        requirement["ambiguity"] = check_ambiguity(line)

        requirements.append(requirement)
        number += 1

    return requirements
