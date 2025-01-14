from typing import Any, Callable, Dict, Optional, Tuple

from ...api.api_substation import SubstationAPI
from ...configuration import config
from ...logging import log

substation = SubstationAPI(config)


def substation_injection() -> Callable[[Dict[str, Any]], Any]:
    def model(input: Dict[str, Any]) -> Any:
        return substation.predict(input["prompt"], input["max_output_length"])

    return model


class SubstationTask:
    def __init__(self, func: Callable[[Any], Any], id: str, model: Optional[str]) -> None:
        self.func = func
        self.args: Optional[Tuple[Any, ...]] = None
        self.kwargs: Optional[Dict[str, Any]] = None
        self.type = "inference"
        self.model = model
        self.id = id

    def process(self, *args: Any, **kwargs: Any) -> Any:
        self.args = args
        self.kwargs = kwargs

        if self.model == "mpt-30b":
            log.info("Processing MPT-30B Model...")
            self.args = self.args + (substation_injection(),)

            return self.func(*self.args, **self.kwargs)

    def print(self) -> None:
        log.info(f"id: {self.id}, type: {self.type}, model: {self.model}")
