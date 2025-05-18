from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ModelDetail(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        api_key = self.runtime.credentials.get("civitai_api_key")
        if not api_key:
            yield self.create_text_message("Please input base_url")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        if not "model_id" in tool_parameters:
            yield self.create_text_message("Please input model_id")
            return
        model_id = tool_parameters["model_id"]
        response = requests.get(
            f"https://civitai.com/api/v1/models/{model_id}", headers=headers
        ).json()
        for val_name in ["name", "description", "type", "nsfw", "tags"]:
            yield self.create_variable_message(val_name, response[val_name])

        yield self.create_variable_message("nsfw_level", response["nsfwLevel"])
        yield self.create_variable_message(
            "download_count", response["stats"]["downloadCount"]
        )
        yield self.create_variable_message(
            "thumbs_up_count", response["stats"]["thumbsUpCount"]
        )
        yield self.create_variable_message(
            "thumbs_down_count", response["stats"]["thumbsDownCount"]
        )
        yield self.create_variable_message(
            "creator_name", response["creator"]["username"]
        )
        yield self.create_variable_message(
            "creator_icon_url", response["creator"]["image"]
        )
        version_ids = [v["id"] for v in response["modelVersions"]]
        yield self.create_variable_message("version_ids", version_ids)
