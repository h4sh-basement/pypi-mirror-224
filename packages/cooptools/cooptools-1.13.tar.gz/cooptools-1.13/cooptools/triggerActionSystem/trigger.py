from typing import Any, Callable, List
import cooptools.coopProtocols as cprot

trigger_callable = Callable[[Any], str]

class TriggerHub:
    def __init__(self, trigger: trigger_callable):
        pass

    def register_triggers(self, ):