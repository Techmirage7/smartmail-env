import os
from env.environment import SmartMailEnv
from env.models import Action


API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")


def run_baseline():
    env = SmartMailEnv()

    print("[START] task=SmartMail rollout", flush=True)

    obs = env.reset()
    print(
        f"[STEP] step=0 state={obs.current_status} "
        f"subject='{obs.email_subject}'",
        flush=True
    )

    action1 = Action(
        action_type="classify",
        label="delivery_issue"
    )

    obs, reward1, done, info = env.step(action1)

    print(
        f"[STEP] step=1 reward={reward1} "
        f"done={done} "
        f"state={obs.current_status}",
        flush=True
    )

    total_reward = reward1
    steps = 1

    if not done:
        action2 = Action(
            action_type="resolve",
            label="delivery_team"
        )

        obs, reward2, done, info = env.step(action2)

        total_reward += reward2
        steps += 1

        print(
            f"[STEP] step=2 reward={reward2} "
            f"done={done} "
            f"state={obs.current_status}",
            flush=True
        )

    print(
        f"[END] task=SmartMail score={total_reward} steps={steps}",
        flush=True
    )


if __name__ == "__main__":
    run_baseline()