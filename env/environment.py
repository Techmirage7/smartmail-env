from env.models import Observation
from env.tasks import TASKS
from env.graders import grade_action


class SmartMailEnv:
    def __init__(self):
        self.current_task_index = 0
        self.current_task = None
        self.current_status = "new"
        self.step_count = 0

    def reset(self):
        self.current_task_index = (
            self.current_task_index + 1
        ) % len(TASKS)

        self.current_task = TASKS[self.current_task_index]
        self.current_status = "new"
        self.step_count = 0

        return Observation(
            email_subject=self.current_task["email_subject"],
            email_body=self.current_task["email_body"],
            current_status=self.current_status
        )

    def step(self, action):
        self.step_count += 1

        # progressive reward shaping
        if self.step_count == 1:
            score = grade_action(action, self.current_task)
            self.current_status = "under_review"
            done = False

        elif self.step_count == 2:
            score = 0.2
            self.current_status = "resolved"
            done = True

        else:
            score = 0.0
            done = True

        info = {
            "task_id": self.current_task["id"],
            "difficulty": self.current_task["difficulty"],
            "step_count": self.step_count
        }

        observation = Observation(
            email_subject=self.current_task["email_subject"],
            email_body=self.current_task["email_body"],
            current_status=self.current_status
        )

        return observation, score, done, info

    def state(self):
        return {
            "task": self.current_task,
            "status": self.current_status,
            "step_count": self.step_count
        }