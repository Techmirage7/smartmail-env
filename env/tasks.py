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
        "difficulty": "easy",
        "email_subject": "Package delayed",
        "email_body": "My package was supposed to arrive yesterday but has still not been delivered.",
        "expected_action": "escalate",
        "expected_label": "delivery_issue",
        "priority": "medium"
    },
    {
        "id": 3,
        "difficulty": "medium",
        "email_subject": "Payment failed twice",
        "email_body": "My payment keeps failing while checking out after retrying twice.",
        "expected_action": "classify",
        "expected_label": "billing_issue",
        "priority": "high"
    },
    {
        "id": 4,
        "difficulty": "medium",
        "email_subject": "Suspicious login email",
        "email_body": "I received an email asking for my password and OTP details.",
        "expected_action": "flag",
        "expected_label": "security_issue",
        "priority": "critical"
    },
    {
        "id": 5,
        "difficulty": "hard",
        "email_subject": "Urgent premium client complaint",
        "email_body": "I am a premium customer and this issue has been unresolved for 10 days.",
        "expected_action": "escalate",
        "expected_label": "priority_issue",
        "priority": "critical"
    },
    {
        "id": 6,
        "difficulty": "hard",
        "email_subject": "Urgent client complaint mixed with spam risk",
        "email_body": "A customer reports repeated login failures while suspicious promotional links are also attached.",
        "expected_action": "escalate",
        "expected_label": "security_issue",
        "priority": "critical"
    }
]