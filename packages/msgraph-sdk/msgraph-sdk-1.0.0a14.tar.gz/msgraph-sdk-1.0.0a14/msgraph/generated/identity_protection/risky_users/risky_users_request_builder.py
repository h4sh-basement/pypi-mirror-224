from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.risky_user import RiskyUser
    from ...models.risky_user_collection_response import RiskyUserCollectionResponse
    from .confirm_compromised.confirm_compromised_request_builder import ConfirmCompromisedRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .dismiss.dismiss_request_builder import DismissRequestBuilder
    from .item.risky_user_item_request_builder import RiskyUserItemRequestBuilder

class RiskyUsersRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the riskyUsers property of the microsoft.graph.identityProtectionRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RiskyUsersRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/identityProtection/riskyUsers{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_risky_user_id(self,risky_user_id: str) -> RiskyUserItemRequestBuilder:
        """
        Provides operations to manage the riskyUsers property of the microsoft.graph.identityProtectionRoot entity.
        Args:
            risky_user_id: Unique identifier of the item
        Returns: RiskyUserItemRequestBuilder
        """
        if not risky_user_id:
            raise TypeError("risky_user_id cannot be null.")
        from .item.risky_user_item_request_builder import RiskyUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["riskyUser%2Did"] = risky_user_id
        return RiskyUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RiskyUsersRequestBuilderGetRequestConfiguration] = None) -> Optional[RiskyUserCollectionResponse]:
        """
        Get a list of the riskyUser objects and their properties.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RiskyUserCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.risky_user_collection_response import RiskyUserCollectionResponse

        return await self.request_adapter.send_async(request_info, RiskyUserCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[RiskyUser] = None, request_configuration: Optional[RiskyUsersRequestBuilderPostRequestConfiguration] = None) -> Optional[RiskyUser]:
        """
        Create new navigation property to riskyUsers for identityProtection
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RiskyUser]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.risky_user import RiskyUser

        return await self.request_adapter.send_async(request_info, RiskyUser, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RiskyUsersRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a list of the riskyUser objects and their properties.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_post_request_information(self,body: Optional[RiskyUser] = None, request_configuration: Optional[RiskyUsersRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to riskyUsers for identityProtection
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def confirm_compromised(self) -> ConfirmCompromisedRequestBuilder:
        """
        Provides operations to call the confirmCompromised method.
        """
        from .confirm_compromised.confirm_compromised_request_builder import ConfirmCompromisedRequestBuilder

        return ConfirmCompromisedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dismiss(self) -> DismissRequestBuilder:
        """
        Provides operations to call the dismiss method.
        """
        from .dismiss.dismiss_request_builder import DismissRequestBuilder

        return DismissRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RiskyUsersRequestBuilderGetQueryParameters():
        """
        Get a list of the riskyUser objects and their properties.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RiskyUsersRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[RiskyUsersRequestBuilder.RiskyUsersRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RiskyUsersRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

