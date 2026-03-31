from fastapi import FastAPI
from env.environment import SmartMailEnv
from env.models import Action

app = FastAPI()


@app.get("/")
def home():
    env = SmartMailEnv()
    observation = env.reset()

    action = Action(
        action_type="escalate",
        label="refund_issue"
    )

    observation, reward, done, info = env.step(action)

    return {
        "message": "SmartMail Space is running",
        "reward": reward,
        "done": done,
        "info": info
    }