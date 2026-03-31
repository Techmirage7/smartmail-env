from fastapi import FastAPI
from env.environment import SmartMailEnv
from env.models import Action

app = FastAPI()


@app.get("/")
def home():
    return {"message": "SmartMail Space is running"}


@app.post("/reset")
def reset_env():
    env = SmartMailEnv()
    observation = env.reset()

    return observation.model_dump()


@app.post("/step")
def step_env():
    env = SmartMailEnv()
    env.reset()

    action = Action(
        action_type="escalate",
        label="refund_issue"
    )

    observation, reward, done, info = env.step(action)

    return {
        "observation": observation.model_dump(),
        "reward": reward,
        "done": done,
        "info": info
    }