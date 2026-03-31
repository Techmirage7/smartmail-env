TASKS = [
    {
        "id": 1,
        "difficulty": "easy",
        "email_subject": "Refund not received",
        "email_body": "I requested a refund 5 days ago but still haven't received it.",
        "expected_action": "escalate",
        "expected_label": "refund_issue",
        "priority": "high"
    },
    {
        "id": 2,
        "difficulty": "medium",
        "email_subject": "Payment failed twice",
        "email_body": "My payment keeps failing while checking out after retrying twice.",
        "expected_action": "classify",
        "expected_label": "billing_issue",
        "priority": "high"
    },
    {
        "id": 3,
        "difficulty": "hard",
        "email_subject": "Urgent client complaint mixed with spam risk",
        "email_body": "A customer reports repeated login failures while suspicious promotional links are also attached.",
        "expected_action": "escalate",
        "expected_label": "security_issue",
        "priority": "critical"
    }
]