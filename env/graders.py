def grade_action(action, task):
    score = 0.0

    # correct action type
    if action.action_type == task["expected_action"]:
        score += 0.4

    # correct label
    if action.label == task["expected_label"]:
        score += 0.4

    # difficulty-based bonus
    if task["difficulty"] == "easy":
        score += 0.2
    elif task["difficulty"] == "medium":
        score += 0.15
    elif task["difficulty"] == "hard":
        score += 0.1

    return round(min(score, 1.0), 2)