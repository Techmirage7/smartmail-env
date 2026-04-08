def grade_action(action, task):
    score = 0.0

    # correct action type
    if action.action_type == task["expected_action"]:
        score += 0.4

    # correct label
    if action.label == task["expected_label"]:
        score += 0.35

    # difficulty bonus
    if task["difficulty"] == "easy":
        score += 0.15
    elif task["difficulty"] == "medium":
        score += 0.12
    elif task["difficulty"] == "hard":
        score += 0.10

    # STRICTLY keep score inside (0,1)
    if score <= 0.0:
        score = 0.05

    if score >= 1.0:
        score = 0.95

    return round(score, 2)