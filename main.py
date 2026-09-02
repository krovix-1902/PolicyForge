from app.policy.requirements import extract_requirements
from app.policy.control_mapper import map_requirement
from app.policy.risk_mapper import map_risk
from app.personas.persona_engine import personas
from app.scenarios.scenario_engine import scenarios
from app.simulation.decision_engine import make_decision
from app.simulation.policy_tester import test_policy
from app.simulation.relevance import is_relevant
from app.findings.finding_engine import create_finding
from app.findings.coverage import check_coverage


with open("data/policies/test_policy.txt", "r") as f:
    policy = f.read()


requirements = extract_requirements(policy)

print()
print("================================")
print("        POLICYFORGE")
print("================================")


print()
print("POLICY COVERAGE")
print("----------------")

coverage = check_coverage(requirements, scenarios)

for item in coverage:

    print(
        item["requirement_id"],
        "|",
        item["topic"],
        "|",
        item["status"]
    )

    if item["status"] == "GAP":
        print("  No test scenario available")


print()
print("POLICY FINDINGS")
print("----------------")


for requirement in requirements:

    control = map_requirement(requirement)
    risk = map_risk(requirement)

    for persona in personas:

        for scenario in scenarios:

            if not is_relevant(requirement, scenario):
                continue

            decision = make_decision(
                persona,
                scenario,
                requirement
            )

            result = test_policy(
                requirement,
                scenario,
                decision
            )

            if result["result"] == "FAIL":

                finding = create_finding(
                    result,
                    control,
                    risk
                )

                print()
                print("FINDING")
                print("----------------")
                print("Persona:", persona["name"])
                print("Requirement:", requirement["id"])
                print("Scenario:", scenario["name"])
                print("Expected:", result["expected"])
                print("Actual:", result["actual"])
                print("Control:", control)
                print("Risk:", risk)
                print("Severity:", finding["severity"])
