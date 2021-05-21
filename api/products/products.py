import urllib.parse
from sp_api.base import Client, Marketplaces, sp_endpoint, ApiResponse


class Products(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/product-pricing-api/productPricingV0.md
    """

    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_product_pricing_for_skus(self, seller_sku_list: [str], item_condition=None, **kwargs) -> ApiResponse:
        """
        get_product_pricing_for_skus(self, seller_sku_list: [str], item_condition: str = None, **kwargs) -> ApiResponse
        Returns pricing information for a seller's offer listings based on SKU.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============

        Args:

            seller_sku_list: [str]
            item_condition: str ("New", "Used", "Collectible", "Refurbished", "Club")
            **kwargs:

        Returns:
            ApiResponse:
        """
        if item_condition is not None:
            kwargs['ItemCondition'] = item_condition

        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_product_pricing_for_asins(self, asin_list: [str], item_condition=None, **kwargs) -> ApiResponse:
        """
        get_product_pricing_for_asins(self, asin_list: [str], item_condition=None, **kwargs) -> ApiResponse
        Returns pricing information for a seller's offer listings based on ASIN.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param asin_list: [str]
        :param item_condition: str ("New", "Used", "Collectible", "Refurbished", "Club")
           Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
           Available values : New, Used, Collectible, Refurbished, Club
        :param kwargs:
        :return: ApiResponse
        """
        if item_condition is not None:
            kwargs['ItemCondition'] = item_condition

        return self._create_get_pricing_request(asin_list, 'Asin', **kwargs)

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing_for_skus(self, seller_sku_list: [str], **kwargs) -> ApiResponse:
        """
        get_competitive_pricing_for_skus(self, seller_sku_list, **kwargs) -> ApiResponse
        Returns competitive pricing information for a seller's offer listings based on Seller Sku

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param seller_sku_list: [str]
        :param kwargs:
        :return: ApiResponse
        """
        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing_for_asins(self, asin_list: [str], **kwargs) -> ApiResponse:
        """
        get_competitive_pricing_for_asins(self, asin_list, **kwargs) -> ApiResponse
        Returns competitive pricing information for a seller's offer listings based on ASIN

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param asin_list: [str]
        :param kwargs:
        :return:

        """
        return self._create_get_pricing_request(asin_list, 'Asin', **kwargs)

    def _create_get_pricing_request(self, item_list, item_type, **kwargs):
        return self._request(kwargs.pop('path'),
                             params={**{f"{item_type}s": ','.join(
                                 [urllib.parse.quote_plus(s) for s in item_list])},
                                     'ItemType': item_type,
                                     **({'ItemCondition': kwargs.pop(
                                         'ItemCondition')} if 'ItemCondition' in kwargs else {}),
                                     'MarketplaceId': kwargs.get('MarketplaceId', self.marketplace_id)})
