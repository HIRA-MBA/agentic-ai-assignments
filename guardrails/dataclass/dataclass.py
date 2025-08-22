from pydantic import BaseModel

class Input_Guardrail(BaseModel):
        is_question_realted_to_Maths:bool
        reason:str

class Output_Guardrail(BaseModel):
    is_question_realted_to_politics:bool
    reason:str