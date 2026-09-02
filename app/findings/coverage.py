def check_coverage(requirements, scenarios):

    results = []

    for requirement in requirements:

        matched_scenarios = []

        for scenario in scenarios:

            if requirement["topic"] == scenario["topic"]:
                matched_scenarios.append(scenario["name"])

        if matched_scenarios:
            status = "COVERED"
        else:
            status = "GAP"

        results.append({
            "requirement_id": requirement["id"],
            "text": requirement["text"],
            "topic": requirement["topic"],
            "status": status,
            "scenarios": matched_scenarios
        })

    return results
