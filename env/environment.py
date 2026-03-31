from env.models import Observation
from env.tasks import TASKS
from env.graders import grade_action


class SmartMailEnv:
    def __init__(self):
        self.current_task_index = 0
        self.current_task = None

    def reset(self):
        self.current_task_index = 0
        self.current_task = TASKS[self.current_task_index]

        return Observation(
            email_subject=self.current_task["email_subject"],
            email_body=self.current_task["email_body"],
            current_status="new"
        )

    def step(self, action):
        score = grade_action(action, self.current_task)

        done = True
        info = {
            "task_id": self.current_task["id"],
            "difficulty": self.current_task["difficulty"]
        }

        observation = Observation(
            email_subject=self.current_task["email_subject"],
            email_body=self.current_task["email_body"],
            current_status="processed"
        )

        return observation, score, done, info

    def state(self):
        return self.current_task