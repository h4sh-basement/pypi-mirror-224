from typing import List, Iterator, Optional, Dict, Any

from pydantic import BaseModel, ConfigDict

from phi.llm.schemas import Message, Function


class LLM(BaseModel):
    model: str
    name: Optional[str] = None
    metrics: Dict[str, Any] = {}
    functions: Optional[List[Function]] = None
    function_call: Optional[str] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def response(self, messages: List[Message]) -> str:
        raise NotImplementedError

    def response_stream(self, messages: List[Message]) -> Iterator[str]:
        raise NotImplementedError
