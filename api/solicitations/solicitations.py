import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Solicitations(Client):

    @sp_endpoint('/solicitations/v1/orders/{}')
    def get_solicitation_actions_for_order(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_solicitation_actions_for_order(self, order_id: str, **kwargs) -> ApiResponse

        Args:
            order_id:
            key marketplaceIds: str
            **kwargs:

        Returns:
            ApiResponse:
        """
        kwargs.update({'marketplaceIds': kwargs.get('marketplaceIds', None) or self.marketplace_id})
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params=kwargs)
    
    @sp_endpoint('/solicitations/v1/orders/{}/productReviewAndSellerFeedback','POST')
    def create_product_review_and_seller_feedback_solicitation(self,order_id: str, **kwargs) -> ApiResponse:
        """
        create_product_review_and_seller_feedback_solicitation(self, order_id: str, **kwargs) -> ApiResponse

        Args:
            order_id:
            key marketplaceIds: str
            **kwargs:

        Returns:
            ApiResponse:
        """
        kwargs.update({'marketplaceIds': kwargs.get('marketplaceIds', None) or self.marketplace_id})
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params=kwargs)