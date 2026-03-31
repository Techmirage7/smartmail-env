def grade_action(action, task):
    score = 0.0

    if action.action_type == task["expected_action"]:
        score += 0.4

    if action.label == task["expected_label"]:
        score += 0.4

    if task["difficulty"] == "hard":
        score += 0.2
    else:
        score += 0.2

    return min(score, 1.0)