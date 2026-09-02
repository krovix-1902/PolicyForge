def create_requirement(rule_id, text, rule_type):
    return {
        "id": rule_id,
        "text": text,
        "type": rule_type
    }


def extract_requirements(policy):
    requirements = []
    number = 1

    for line in policy.splitlines():
        line = line.strip()

        if "must not" in line.lower():
            requirements.append(
                create_requirement(
                    f"REQ-{number:03}",
                    line,
                    "PROHIBITED"
                )
            )
            number += 1

        elif "must" in line.lower():
            requirements.append(
                create_requirement(
                    f"REQ-{number:03}",
                    line,
                    "REQUIRED"
                )
            )
            number += 1

        elif "should" in line.lower():
            requirements.append(
                create_requirement(
                    f"REQ-{number:03}",
                    line,
                    "RECOMMENDED"
                )
            )
            number += 1

    return requirements
