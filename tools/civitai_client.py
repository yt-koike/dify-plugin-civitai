import requests


class CivitAI:
    # Base on https://developer.civitai.com/docs/api/public-rest
    def __init__(self, api_key=None):
        self._api_key = api_key

    def _call(self, url, params, with_key=False) -> dict:
        headers = {
            "Content-Type": "application/json",
        }
        if with_key:
            if self._api_key is None:
                raise Exception("api_key not found")
            headers["Authorization"] = f"Bearer {self._api_key}"
        response = requests.get(
            url, headers=headers, params=params
        )
        if response.status_code != 200:
            raise Exception("Failed fetching")
        return response.json()

    def get_creators(self, limit=20, page=None, query=None) -> dict:
        params = {"limit": limit}
        if page is not None:
            params["page"] = page
        if query is not None:
            params["query"] = query
        response_dict = self._call(
            "https://civitai.com/api/v1/creators", params, False)
        return response_dict

    def get_images(self, limit=20, postId=None, modelId=None, modelVersionId=None, username=None, nsfw=None, sort=None, period=None, page=None) -> dict:
        params = {"limit": limit}
        response_dict = self._call(
            "https://civitai.com/api/v1/images", params, False)
        return response_dict

    def get_models(self, limit=20, page=None, query=None, tag=None, username=None, types=None, sort=None, period=None, favorites=False, hidden=False, primaryFileOnly=None, allowNoCredit=None, allowDerivatives=None, allowDifferentLicenses=None, allowCommercialUse=None, nsfw=None, supportsGeneration=None) -> dict:
        params = {"limit": limit}
        response_dict = self._call(
            "https://civitai.com/api/v1/images", params, favorites or hidden)
        return response_dict

    def get_model_detail(self, modelId: str) -> dict:
        response_dict = self._call(
            "https://civitai.com/api/v1/models/"+modelId, {}, False)
        return response_dict

    def get_model_version(self, modelVersionId: str) -> dict:
        response_dict = self._call(
            "https://civitai.com/api/v1/model-versions/"+modelVersionId, {}, False)
        return response_dict

    def get_model_by_hash(self, hash: str) -> dict:
        response_dict = self._call(
            "https://civitai.com/api/v1/model-versions/by-hash/"+hash, {}, False)
        return response_dict

    def get_tags(self, limit=20, page=None, query=None) -> dict:
        params = {"limit": limit}
        if page is not None:
            params["page"] = page
        if query is not None:
            params["query"] = query
        response_dict = self._call(
            "https://civitai.com/api/v1/tags", params, False)
        return response_dict
