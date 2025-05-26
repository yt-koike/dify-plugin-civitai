from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from .civitai_client import CivitAI


class ModelVersionDetail(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        api_key = self.runtime.credentials.get("civitai_api_key")
        if not api_key:
            yield self.create_text_message("Please input api_key")
        cli = CivitAI(api_key)
        if tool_parameters.get("model_version_id") is None:
            yield self.create_text_message("Please input model_version_id")
        json = cli.get_tags(tool_parameters.get("limit", 20))
        yield self.create_json_message(json)

        mapping = {"name": [item["name"] for item in json["items"]],
                   "link": [item["link"] for item in json["items"]]}
        for key in mapping:
            yield self.create_variable_message(key, mapping[key])
