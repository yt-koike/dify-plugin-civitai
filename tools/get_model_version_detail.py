from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ModelVersionDetail(Tool):
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
        if not "version_id" in tool_parameters:
            yield self.create_text_message("Please input version_id")
            return
        version_id = tool_parameters["version_id"]
        response = requests.get(
            f"https://civitai.com/api/v1/models/{model_id}", headers=headers
        ).json()
        version = None
        for v in response["modelVersions"]:
            if v["id"] == version_id:
                version = v
                break
        if version is None:
            yield self.create_text_message(f"Version {version_id} not found")
            return
        yield self.create_variable_message("created_at", version["createdAt"])
        yield self.create_variable_message("published_at", version["publishedAt"])
        yield self.create_variable_message("url", version["downloadUrl"])
        yield self.create_variable_message(
            "download_count", version["stats"]["downloadCount"]
        )
        file_names = [f["name"] for f in version["files"]]
        yield self.create_variable_message("file_names", file_names)
        file_urls = [f["downloadUrl"] for f in version["files"]]
        yield self.create_variable_message("file_urls", file_urls)
        image_urls = [img["url"] for img in version["images"]]
        yield self.create_variable_message("image_urls", image_urls)
        image_nsfw = [img["nsfwLevel"] for img in version["images"]]
        yield self.create_variable_message("image_nsfw", image_nsfw)
