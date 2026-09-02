from app.personas.persona_engine import personas
from app.scenarios.scenario_engine import scenarios


def run_simulation():

    for persona in personas:

        print()
        print("PERSONA:", persona["name"])
        print("ROLE:", persona["role"])

        for scenario in scenarios:

            print()
            print("SCENARIO:", scenario["name"])
            print("SITUATION:", scenario["situation"])
            print("EXPECTED:", scenario["expected_action"])


run_simulation()
