"""
Classes
~~~~~~~

Classes which may be used to handle or interact with the Asset API.

"""
from google.cloud import asset_v1


class Client:
    r"""This class can be used to call methods in this library using the same
    credentials object, cutting down on API authentication flows.
    """

    def __init__(self, gcp_org_id, credentials=None):
        self._client = asset_v1.AssetServiceClient(credentials=credentials)
        self.gcp_org_id = gcp_org_id

    def list_assets(self, parent, asset_types=None, content_type=None, page_size=1000):
        """https://cloud.google.com/asset-inventory/docs/reference/rest/v1/assets/list"""
        request = {
            "parent": parent,
            "read_time": None,
            "page_size": page_size,
        }
        if type(asset_types) is not list and asset_types is not None:
            asset_types = [asset_types]
        if asset_types is not None:
            request["asset_types"] = asset_types
        if content_type is not None:
            request["content_type"] = content_type

        return [asset for asset in self._client.list_assets(request=request)]

    def get_asset(self, scope, asset_name, asset_type=None):
        result = self.search_assets(
            scope, f'name="{asset_name}"', asset_types=asset_type, page_size=1
        )
        return result.results[0] if len(result.results) > 1 else None

    def search_assets(
        self, scope, query, asset_types=None, order_by=None, page_size=1000
    ):
        """https://cloud.google.com/asset-inventory/docs/query-syntax
        https://cloud.google.com/asset-inventory/docs/searching-resources#search_resources
        """
        if type(asset_types) is not list and asset_types is not None:
            asset_types = [asset_types]
        if asset_types is not None:
            request["asset_types"] = asset_types
        if order_by is not None:
            request["order_by"] = order_by
        return self._client.search_all_resources(
            request={
                "scope": scope,
                "query": query,
                "asset_types": asset_types,
                "page_size": page_size,
                "order_by": order_by,
            }
        )
