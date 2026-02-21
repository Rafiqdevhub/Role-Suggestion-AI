from __future__ import annotations

from typing import Any, Optional

try:
    from google import genai as genai_module
    GENAI_AVAILABLE = True
except ImportError:
    genai_module = None
    GENAI_AVAILABLE = False


def _is_legacy_genai() -> bool:
    return bool(genai_module) and hasattr(genai_module, "configure") and hasattr(genai_module, "GenerativeModel")


def _build_generation_config(json_mode: bool) -> Optional[Any]:
    if not json_mode or not genai_module or not hasattr(genai_module, "types"):
        return None
    types = genai_module.types
    if hasattr(types, "GenerateContentConfig"):
        return types.GenerateContentConfig(response_mime_type="application/json")
    if hasattr(types, "GenerationConfig"):
        return types.GenerationConfig(response_mime_type="application/json")
    return None


class GenAIAdapter:
    def __init__(self, api_key: str):
        if not GENAI_AVAILABLE or not genai_module:
            raise ImportError("google-genai package is not available")
        self._api_key = api_key
        self._client: Optional[Any] = None
        self._legacy = _is_legacy_genai()
        self._init_client()

    def _init_client(self) -> None:
        if self._legacy:
            genai_module.configure(api_key=self._api_key)
            return

        if hasattr(genai_module, "aio") and hasattr(genai_module.aio, "Client"):
            self._client = genai_module.aio.Client(api_key=self._api_key)
        else:
            self._client = genai_module.Client(api_key=self._api_key)

    def create_model(self, model_name: str, *, json_mode: bool = False) -> Any:
        generation_config = _build_generation_config(json_mode)
        if self._legacy:
            if generation_config is not None:
                return genai_module.GenerativeModel(model_name, generation_config=generation_config)
            return genai_module.GenerativeModel(model_name)

        if self._client is None:
            raise RuntimeError("GenAI client is not initialized")
        return _GenAIModelShim(self._client, model_name, generation_config)


class _GenAIModelShim:
    def __init__(self, client: Any, model_name: str, generation_config: Optional[Any]):
        self._client = client
        self._model_name = model_name
        self._generation_config = generation_config

    async def generate_content_async(self, prompt: str) -> Any:
        if hasattr(self._client.models, "generate_content_async"):
            return await self._client.models.generate_content_async(
                model=self._model_name,
                contents=prompt,
                config=self._generation_config,
            )
        return self._client.models.generate_content(
            model=self._model_name,
            contents=prompt,
            config=self._generation_config,
        )

    def generate_content(self, prompt: str) -> Any:
        return self._client.models.generate_content(
            model=self._model_name,
            contents=prompt,
            config=self._generation_config,
        )
