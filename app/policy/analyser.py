def analyse_rule(text):
    text = text.strip()

    if "must not" in text.lower():
        rule_type = "PROHIBITED"
    elif "must" in text.lower():
        rule_type = "REQUIRED"
    elif "should" in text.lower():
        rule_type = "RECOMMENDED"
    else:
        rule_type = "UNCLEAR"

    return rule_type