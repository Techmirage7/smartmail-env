---
title: SmartMail Env
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# 📧 SmartMail Environment

## SmartMail RL Architecture
![SmartMail Architecture](Architecture_diagram.png)

SmartMail is a real-world **OpenEnv RL environment** designed for training and evaluating AI agents on **email triage and customer support workflows**.

Built for the **Meta × Hugging Face OpenEnv Hackathon**.

---

## Overview

The environment simulates realistic customer-support email tasks such as:

- refund complaints
- payment failures
- delayed deliveries
- suspicious / phishing emails
- escalation workflows

It follows the standard OpenEnv interface:

```python
reset()
step(action)
state()

    RL Workflow

The environment supports a true RL-style loop:


Agent → Action → Environment → Reward → Next State

Example state trajectory:

new → under_review → resolved


    Observation Space

Each observation contains:

{
    "email_subject": str,
    "email_body": str,
    "current_status": str
}

Example:

{
    "email_subject": "Package delayed",
    "email_body": "My package was supposed to arrive yesterday...",
    "current_status": "new"
}
    Action Space

Each action contains:

Action(
    action_type="classify",
    label="delivery_issue"
)

    Supported actions:

classify
escalate
mark_spam
resolve


    Tasks

The environment currently supports multiple tasks with increasing complexity:

🟢 Easy
refund issue
delivery delay
🟡 Medium
payment failure
account login issue
🔴 Hard
phishing / security escalation
spam + urgent customer complaint mix

    Reward Logic

Progressive reward shaping:

correct action → 0.4
correct label → 0.2
correct trajectory step → 0.2
completion bonus → 0.2

Maximum reward:

1.0

     Multi-Step Example

Example rollout:

Step 1:
new → under_review
reward = 0.6

Step 2:
under_review → resolved
reward = 0.2

Total reward = 0.8
    
    Run Locally
python inference.py
    
    Docker
docker build -t smartmail-env .
docker run --rm smartmail-env

    Validation
openenv validate

Status:

Ready for multi-mode deployment

     Hugging Face Space

Live deployment:

https://duniyakapapa007-smartmail-env.hf.space

    Built With
OpenEnv
FastAPI
Docker
Hugging Face Spaces
Python 3.12