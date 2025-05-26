from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from .civitai_client import CivitAI


class GetModels(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        api_key = self.runtime.credentials.get("civitai_api_key")
        if not api_key:
            yield self.create_text_message("Please input api_key")
        cli = CivitAI(api_key)
        type = tool_parameters.get("type")
        types = None
        if type != "All":
            types = [type]
        allowCommercialUse = None
        if tool_parameters.get("allowCommercialUse") != "None":
            allowCommercialUse = [tool_parameters.get("allowCommercialUse")]
        json = cli.get_models(limit=tool_parameters.get("limit", 100),
                              page=tool_parameters.get("page"),
                              query=tool_parameters.get("query"),
                              tag=tool_parameters.get("tag"),
                              types=types,
                              sort=tool_parameters.get("sort"),
                              period=tool_parameters.get("period"),
                              favorites=tool_parameters.get("favorites"),
                              hidden=tool_parameters.get("hidden"),
                              primaryFileOnly=tool_parameters.get(
                                  "primaryFileOnly"),
                              allowNoCredit="true" if tool_parameters.get(
                                  "allowNoCredit") else "false",
                              allowDerivatives="true" if tool_parameters.get(
                                  "allowDerivatives") else "false",
                              allowDifferentLicenses="true" if tool_parameters.get(
                                  "allowDifferentLicenses") else "false",
                              allowCommercialUse=allowCommercialUse,
                              nsfw="true" if tool_parameters.get(
                                  "nsfw") else "false",
                              supportsGeneration="true" if tool_parameters.get("supportsGeneration") else "false")

        yield self.create_json_message(json)

        mapping = {"ids": [item["id"] for item in json["items"]],
                   "names": [item["name"] for item in json["items"]]
                   }
        for key in mapping:
            yield self.create_variable_message(
                key, mapping[key]
            )
