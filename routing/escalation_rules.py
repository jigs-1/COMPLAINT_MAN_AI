def get_escalation_time(priority):

    rules = {
        "High": "12 Hours",
        "Medium": "24 Hours",
        "Low": "48 Hours"
    }

    return rules.get(priority, "24 Hours")