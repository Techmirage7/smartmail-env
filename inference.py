from env.environment import SmartMailEnv
from env.models import Action


def run_baseline():
    env = SmartMailEnv()

    observation = env.reset()

    print("Initial Observation:")
    print(observation)

    total_reward = 0.0

    # Step 1: classify / escalate
    action1 = Action(
        action_type="escalate",
        label="refund_issue"
    )

    observation, reward1, done, info = env.step(action1)
    total_reward += reward1

    print("\nAfter Step 1:")
    print("Observation:", observation)
    print("Reward:", reward1)
    print("Done:", done)
    print("Info:", info)

    # Step 2: resolve if not done
    if not done:
        action2 = Action(
            action_type="resolve",
            label="billing_team"
        )

        observation, reward2, done, info = env.step(action2)
        total_reward += reward2

        print("\nAfter Step 2:")
        print("Observation:", observation)
        print("Reward:", reward2)
        print("Done:", done)
        print("Info:", info)

    print("\nTotal Reward:", total_reward)


if __name__ == "__main__":
    run_baseline()