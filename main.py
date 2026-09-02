from app.policy.analyser import analyse_rule


def load_policy(file):
    with open(file, "r") as f:
        return f.read()


policy = load_policy("data/policies/test_policy.txt")

print("=== POLICYFORGE ===")
print()
print("POLICY ANALYSIS")
print("----------------")

for line in policy.splitlines():

    line = line.strip()

    if not line:
        continue

    if line[0].isdigit() and "." in line:
        print()
        print(line)

    elif "must" in line.lower() or "should" in line.lower():
        result = analyse_rule(line)
        print("  ", result, ":", line)
