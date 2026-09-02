def create_requirement(rule_id, text, rule_type):
    return {
        "id": rule_id,
        "text": text,
        "type": rule_type
    }