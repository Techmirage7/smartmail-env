def grade_action(action, task):
    score = 0.05   # base minimum reward

    # correct action type
    if action.action_type == task["expected_action"]:
        score += 0.40
    else:
        score -= 0.05

    
    if action.label == task["expected_label"]:
        score += 0.30
    else:
        score -= 0.03

    # difficulty bonus
    if task["difficulty"] == "easy":
        score += 0.10
    elif task["difficulty"] == "medium":
        score += 0.12
    elif task["difficulty"] == "hard":
        score += 0.15

    # priority-sensitive escalation reward
    if task["priority"] == "critical":
        if action.action_type == "escalate":
            score += 0.10
        else:
            score -= 0.08

    elif task["priority"] == "high":
        if action.action_type in ["escalate", "classify"]:
            score += 0.05

    # Enterprise logic for VIP / fraud tasks
    if "vip" in task["expected_label"] or "fraud" in task["expected_label"]:
        if action.action_type == "escalate":
            score += 0.05

    # keep strictly inside (0,1)
    score = max(0.05, min(score, 0.95))

    return round(score, 2)