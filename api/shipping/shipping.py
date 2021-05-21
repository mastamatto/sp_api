from sp_api.base import Client, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params


class Shipping(Client):

    @sp_endpoint('/shipping/v1/tracking/{}')
    def get_tracking_information(self, tracking_id, **kwargs) -> ApiResponse:
        """
        get_tracking_information(self, tracking_id, **kwargs) -> ApiResponse


        Args:
            tracking_id:
            **kwargs:

        Returns:

        """
        return self._request(fill_query_params(kwargs.pop('path'), tracking_id), params={**kwargs})
    
    