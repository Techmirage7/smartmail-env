import os
from openai import OpenAI
from env.environment import SmartMailEnv
from env.models import Action


API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")


API_KEY = (
    os.getenv("HF_TOKEN")
    or os.getenv("API_KEY")
    or os.getenv("OPENAI_API_KEY")
)

TASK_NAME = "smartmail_triage"
BENCHMARK = "smartmail_env"


def log_start():
    print(
        f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}",
        flush=True
    )


def log_step(step, action, reward, done, error=None):
    error_val = error if error else "null"
    print(
        f"[STEP] step={step} action={action} "
        f"reward={reward:.2f} done={str(done).lower()} "
        f"error={error_val}",
        flush=True
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} "
        f"steps={steps} score={score:.2f} "
        f"rewards={rewards_str}",
        flush=True
    )


def get_llm_action(client, obs):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an email triage agent. "
                    "Choose one action only from: "
                    "classify, escalate, resolve, mark_spam."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Email Subject: {obs.email_subject}\n"
                    f"Email Body: {obs.email_body}"
                )
            }
        ]
    )

    output = (response.choices[0].message.content or "").lower()

    if "resolve" in output:
        return "resolve"
    elif "escalate" in output:
        return "escalate"
    elif "spam" in output:
        return "mark_spam"
    else:
        return "classify"


def run_baseline():
    rewards = []
    steps_taken = 0
    success = False
    score = 0.0

    log_start()

    try:
        env = SmartMailEnv()
        obs = env.reset()

        
        if not API_KEY:
            action_type = "classify"
        else:
            client = OpenAI(
                base_url=API_BASE_URL,
                api_key=API_KEY
            )
            action_type = get_llm_action(client, obs)

        action = Action(
            action_type=action_type,
            label="delivery_issue"
        )

        obs, reward, done, info = env.step(action)

        rewards.append(reward)
        steps_taken = 1

        log_step(
            step=1,
            action=action_type,
            reward=reward,
            done=done
        )

        if not done:
            action2 = Action(
                action_type="resolve",
                label="delivery_issue"
            )

            obs, reward2, done, info = env.step(action2)

            rewards.append(reward2)
            steps_taken = 2

            log_step(
                step=2,
                action="resolve",
                reward=reward2,
                done=done
            )

        score = min(max(sum(rewards), 0.0), 1.0)
        success = score >= 0.5

    except Exception as e:
        log_step(
            step=max(steps_taken, 1),
            action="error",
            reward=0.0,
            done=True,
            error=str(e)
        )

    finally:
        log_end(
            success=success,
            steps=steps_taken,
            score=score,
            rewards=rewards
        )


if __name__ == "__main__":
    run_baseline()