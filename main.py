def load_policy(file):
    with open(file, "r") as f:
        return f.read()


def analyse_policy(policy):
    for line in policy.splitlines():
        line = line.strip()

        if not line:
            continue

        if "must not" in line.lower():
            print("🚫 PROHIBITED:", line)

        elif "must" in line.lower():
            print("✅ REQUIRED:", line)

        elif "should" in line.lower():
            print("⚠️ RECOMMENDED:", line)


policy = load_policy("data/policies/test_policy.txt")

print("=== POLICYFORGE ===")
print()
print("Analysing policy instructions...")
print()

analyse_policy(policy)
