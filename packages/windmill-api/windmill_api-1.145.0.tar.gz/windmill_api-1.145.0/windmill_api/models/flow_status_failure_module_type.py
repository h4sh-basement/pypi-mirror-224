from enum import Enum


class FlowStatusFailureModuleType(str, Enum):
    WAITINGFORPRIORSTEPS = "WaitingForPriorSteps"
    WAITINGFOREVENTS = "WaitingForEvents"
    WAITINGFOREXECUTOR = "WaitingForExecutor"
    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    FAILURE = "Failure"

    def __str__(self) -> str:
        return str(self.value)
