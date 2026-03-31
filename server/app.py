from env.environment import SmartMailEnv
from env.models import Action


def main():
    env = SmartMailEnv()
    observation = env.reset()

    action = Action(
        action_type="escalate",
        label="refund_issue"
    )

    observation, reward, done, info = env.step(action)

    print("Server running successfully")
    print(observation)
    print(reward)


if __name__ == "__main__":
    main()