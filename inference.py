from env.environment import SmartMailEnv
from env.models import Action


def run_baseline():
    env = SmartMailEnv()

    observation = env.reset()

    print("Initial Observation:")
    print(observation)

    action = Action(
        action_type="escalate",
        label="refund_issue"
    )

    observation, reward, done, info = env.step(action)

    print("\nAfter Step:")
    print("Observation:", observation)
    print("Reward:", reward)
    print("Done:", done)
    print("Info:", info)


if __name__ == "__main__":
    run_baseline()