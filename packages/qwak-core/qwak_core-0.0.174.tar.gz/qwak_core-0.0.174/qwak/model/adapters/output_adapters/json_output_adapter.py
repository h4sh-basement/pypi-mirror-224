from typing import Any

from .base_output_adapter import BaseOutputAdapter


class JsonOutputAdapter(BaseOutputAdapter):
    @staticmethod
    def pack_user_func_return_value(return_result: Any) -> str:
        pass
