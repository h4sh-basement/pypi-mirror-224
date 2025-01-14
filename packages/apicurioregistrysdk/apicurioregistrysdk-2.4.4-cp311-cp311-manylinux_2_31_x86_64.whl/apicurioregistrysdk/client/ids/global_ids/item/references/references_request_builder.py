from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.artifact_reference import ArtifactReference

class ReferencesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /ids/globalIds/{globalId}/references
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReferencesRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/ids/globalIds/{globalId}/references{?refType*}", path_parameters)
    
    async def get(self,request_configuration: Optional[ReferencesRequestBuilderGetRequestConfiguration] = None) -> Optional[List[ArtifactReference]]:
        """
        Returns a list containing all the artifact references using the artifact global ID.This operation may fail for one of the following reasons:* A server error occurred (HTTP error `500`)
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[List[ArtifactReference]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.artifact_reference import ArtifactReference

        return await self.request_adapter.send_collection_async(request_info, ArtifactReference, None)
    
    def to_get_request_information(self,request_configuration: Optional[ReferencesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list containing all the artifact references using the artifact global ID.This operation may fail for one of the following reasons:* A server error occurred (HTTP error `500`)
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
    
    @dataclass
    class ReferencesRequestBuilderGetQueryParameters():
        """
        Returns a list containing all the artifact references using the artifact global ID.This operation may fail for one of the following reasons:* A server error occurred (HTTP error `500`)
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
            if original_name == "ref_type":
                return "refType"
            return original_name
        
        # Determines the type of reference to return, either INBOUND or OUTBOUND.  Defaults to OUTBOUND.
        ref_type: Optional[str] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReferencesRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ReferencesRequestBuilder.ReferencesRequestBuilderGetQueryParameters] = None

    

