from pydantic import BaseModel


class Observation(BaseModel):
    email_subject: str
    email_body: str
    current_status: str


class Action(BaseModel):
    action_type: str
    label: str