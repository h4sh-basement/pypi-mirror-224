from abc import ABC, abstractmethod

import torch


class TaskPrioritizerBase(ABC):
    """Abstract class for TaskPrioritizer whose responsibility is to evaluate task priority"""

    @abstractmethod
    def prioritize(self, *input: torch.Tensor, points: float = 0.0, **kwargs) -> float:
        """Evaluates task value by the amount of points given, task input and additional kwargs. Lower priority is better"""
        pass


class DummyTaskPrioritizer(TaskPrioritizerBase):
    def prioritize(self, *input: torch.Tensor, points: float = 0.0, **kwargs) -> float:
        # Inference steps (especially short ones) go first since they are more latency-sensitive
        if kwargs.get("type") == "short_inference":
            return 1.0
        if kwargs.get("type") == "inference":
            return 2.0
        return 3.0  # Forward, backward
