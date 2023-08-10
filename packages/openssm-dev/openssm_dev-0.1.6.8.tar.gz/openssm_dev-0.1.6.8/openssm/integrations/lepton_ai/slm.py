import os
from typing import Optional
from openssm.integrations.openai.slm import ChatCompletionSLM as OpenAIChatCompletionSLM
from openssm.core.adapter.abstract_adapter import AbstractAdapter
from openssm.utils.config import Config


Config.LEPTONAI_API_KEY: Optional[str] = os.environ.get('LEPTONAI_API_KEY') or None
Config.LEPTONAI_API_URL: Optional[str] = os.environ.get('LEPTONAI_API_URL') or None


class SLM(OpenAIChatCompletionSLM):
    def __init__(self,
                 api_key: str = Config.LEPTONAI_API_KEY,
                 api_base: str = Config.LEPTONAI_API_URL,
                 model: str = "gpt-3.5-turbo",
                 adapter: AbstractAdapter = None):
        super().__init__(api_key, api_base, model, adapter)
