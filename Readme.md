============================
# SmartMail Environment
============================
SmartMail is a real-world OpenEnv environment designed for training and evaluating AI agents on **email triage and customer support workflows**.

The environment simulates realistic inbox tasks such as:
- refund complaints
- payment failures
- security / spam risk emails

This project is built for the Meta × Hugging Face OpenEnv Hackathon.

---
=====================
## 🎯 Objective
=====================
The AI agent must analyze incoming emails and take the correct action.

Supported actions include:
- `classify`
- `escalate`
- `mark_spam`

The goal is to maximize task completion reward.

---
========================
## Observation Space
=========================
Each observation contains:

- `email_subject`
- `email_body`
- `current_status`
=========
Example:
=========
```python
{
    "email_subject": "Refund not received",
    "email_body": "I requested a refund 5 days ago...",
    "current_status": "new"
}
***************
Action Space
***************
Each action contains:

action_type
label
============
Example:
============
Action(
    action_type="escalate",
    label="refund_issue"
)
=======
## Tasks
=======
🟢 Easy

Refund issue triage

🟡 Medium

Payment failure classification

🔴 Hard

Security / suspicious email escalation
====================
##  Reward Logic
====================

correct action → 0.4
correct label → 0.4
completion bonus → 0.2

Maximum reward = 1.0

==============
## Run locally
==============
python inference.py
==============
##  Docker
==============
docker build -t smartmail-env .
docker run --rm smartmail-env

==================
##   Validation
==================
openenv validate

Status:
Ready for multi-mode deployment


