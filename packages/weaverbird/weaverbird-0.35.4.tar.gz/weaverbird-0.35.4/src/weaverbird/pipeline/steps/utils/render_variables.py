from collections.abc import Callable
from typing import Any

from .base import BaseStep


class StepWithVariablesMixin:
    def render(self, variables: dict[str, Any], renderer: Callable[[Any, Any], Any]) -> BaseStep:
        RenderedClass = self.__class__.__bases__[0]
        step_as_dict = self.dict()  # type: ignore
        rendered_dict = renderer(step_as_dict, variables)
        return RenderedClass(**rendered_dict)
