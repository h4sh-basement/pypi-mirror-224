# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicemesh20200111 import models as servicemesh_20200111_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('servicemesh', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cluster_into_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_namespace_check):
            body['IgnoreNamespaceCheck'] = request.ignore_namespace_check
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cluster_into_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_namespace_check):
            body['IgnoreNamespaceCheck'] = request.ignore_namespace_check
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cluster_into_service_mesh(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_into_service_mesh_with_options(request, runtime)

    async def add_cluster_into_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_into_service_mesh_with_options_async(request, runtime)

    def add_vminto_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated
        
        @param request: AddVMIntoServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVMIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVMIntoServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vminto_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated
        
        @param request: AddVMIntoServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVMIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVMIntoServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vminto_service_mesh(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated
        
        @param request: AddVMIntoServiceMeshRequest
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vminto_service_mesh_with_options(request, runtime)

    async def add_vminto_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated
        
        @param request: AddVMIntoServiceMeshRequest
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_vminto_service_mesh_with_options_async(request, runtime)

    def create_asmgateway_with_options(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateASMGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_asmgateway_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateASMGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_asmgateway(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_asmgateway_with_options(request, runtime)

    async def create_asmgateway_async(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_asmgateway_with_options_async(request, runtime)

    def create_gateway_secret_with_options(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert):
            body['Cert'] = request.cert
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateGatewaySecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_secret_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert):
            body['Cert'] = request.cert
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateGatewaySecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_secret(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_secret_with_options(request, runtime)

    async def create_gateway_secret_async(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_secret_with_options_async(request, runtime)

    def create_istio_gateway_domains_with_options(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.credential):
            body['Credential'] = request.credential
        if not UtilClient.is_unset(request.force_https):
            body['ForceHttps'] = request.force_https
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_istio_gateway_domains_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.credential):
            body['Credential'] = request.credential
        if not UtilClient.is_unset(request.force_https):
            body['ForceHttps'] = request.force_https
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_istio_gateway_domains(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_istio_gateway_domains_with_options(request, runtime)

    async def create_istio_gateway_domains_async(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_istio_gateway_domains_with_options_async(request, runtime)

    def create_istio_gateway_routes_with_options(
        self,
        tmp_req: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.CreateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_istio_gateway_routes_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.CreateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_istio_gateway_routes(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_istio_gateway_routes_with_options(request, runtime)

    async def create_istio_gateway_routes_async(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_istio_gateway_routes_with_options_async(request, runtime)

    def create_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.api_server_load_balancer_spec):
            body['ApiServerLoadBalancerSpec'] = request.api_server_load_balancer_spec
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.edition):
            body['Edition'] = request.edition
        if not UtilClient.is_unset(request.enable_ambient):
            body['EnableAmbient'] = request.enable_ambient
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.existing_ca_cert):
            body['ExistingCaCert'] = request.existing_ca_cert
        if not UtilClient.is_unset(request.existing_ca_key):
            body['ExistingCaKey'] = request.existing_ca_key
        if not UtilClient.is_unset(request.existing_ca_type):
            body['ExistingCaType'] = request.existing_ca_type
        if not UtilClient.is_unset(request.existing_root_ca_cert):
            body['ExistingRootCaCert'] = request.existing_root_ca_cert
        if not UtilClient.is_unset(request.existing_root_ca_key):
            body['ExistingRootCaKey'] = request.existing_root_ca_key
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.pilot_load_balancer_spec):
            body['PilotLoadBalancerSpec'] = request.pilot_load_balancer_spec
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.use_existing_ca):
            body['UseExistingCA'] = request.use_existing_ca
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.api_server_load_balancer_spec):
            body['ApiServerLoadBalancerSpec'] = request.api_server_load_balancer_spec
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.edition):
            body['Edition'] = request.edition
        if not UtilClient.is_unset(request.enable_ambient):
            body['EnableAmbient'] = request.enable_ambient
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.existing_ca_cert):
            body['ExistingCaCert'] = request.existing_ca_cert
        if not UtilClient.is_unset(request.existing_ca_key):
            body['ExistingCaKey'] = request.existing_ca_key
        if not UtilClient.is_unset(request.existing_ca_type):
            body['ExistingCaType'] = request.existing_ca_type
        if not UtilClient.is_unset(request.existing_root_ca_cert):
            body['ExistingRootCaCert'] = request.existing_root_ca_cert
        if not UtilClient.is_unset(request.existing_root_ca_key):
            body['ExistingRootCaKey'] = request.existing_root_ca_key
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.pilot_load_balancer_spec):
            body['PilotLoadBalancerSpec'] = request.pilot_load_balancer_spec
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.use_existing_ca):
            body['UseExistingCA'] = request.use_existing_ca
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_mesh(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_mesh_with_options(request, runtime)

    async def create_service_mesh_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_mesh_with_options_async(request, runtime)

    def create_swim_lane_with_options(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_swim_lane_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_swim_lane(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_swim_lane_with_options(request, runtime)

    async def create_swim_lane_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_swim_lane_with_options_async(request, runtime)

    def create_swim_lane_group_with_options(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ingress_gateway_name):
            body['IngressGatewayName'] = request.ingress_gateway_name
        if not UtilClient.is_unset(request.ingress_type):
            body['IngressType'] = request.ingress_type
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_swim_lane_group_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ingress_gateway_name):
            body['IngressGatewayName'] = request.ingress_gateway_name
        if not UtilClient.is_unset(request.ingress_type):
            body['IngressType'] = request.ingress_type
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_swim_lane_group(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_swim_lane_group_with_options(request, runtime)

    async def create_swim_lane_group_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_swim_lane_group_with_options_async(request, runtime)

    def delete_gateway_route_with_options(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_route_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_route(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_route_with_options(request, runtime)

    async def delete_gateway_route_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_route_with_options_async(request, runtime)

    def delete_gateway_secret_with_options(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewaySecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_secret_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewaySecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_secret(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_secret_with_options(request, runtime)

    async def delete_gateway_secret_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_secret_with_options_async(request, runtime)

    def delete_istio_gateway_domains_with_options(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_istio_gateway_domains_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_istio_gateway_domains(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_istio_gateway_domains_with_options(request, runtime)

    async def delete_istio_gateway_domains_async(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_istio_gateway_domains_with_options_async(request, runtime)

    def delete_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources):
            body['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources):
            body['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_mesh(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_mesh_with_options(request, runtime)

    async def delete_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_mesh_with_options_async(request, runtime)

    def delete_swim_lane_with_options(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swim_lane_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swim_lane(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_swim_lane_with_options(request, runtime)

    async def delete_swim_lane_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_swim_lane_with_options_async(request, runtime)

    def delete_swim_lane_group_with_options(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swim_lane_group_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swim_lane_group(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_swim_lane_group_with_options(request, runtime)

    async def delete_swim_lane_group_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_swim_lane_group_with_options_async(request, runtime)

    def describe_asmgateway_imported_services_with_options(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asmgateway_imported_services_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asmgateway_imported_services(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_asmgateway_imported_services_with_options(request, runtime)

    async def describe_asmgateway_imported_services_async(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_asmgateway_imported_services_with_options_async(request, runtime)

    def describe_ccmversion_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCCMVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCCMVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ccmversion_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCCMVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCCMVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ccmversion(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ccmversion_with_options(request, runtime)

    async def describe_ccmversion_async(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ccmversion_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cens(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_cluster_grafana_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterGrafana',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_grafana_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterGrafana',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_grafana(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_grafana_with_options(request, runtime)

    async def describe_cluster_grafana_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_grafana_with_options_async(request, runtime)

    def describe_cluster_prometheus_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.k_8s_cluster_region_id):
            query['K8sClusterRegionId'] = request.k_8s_cluster_region_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterPrometheus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_prometheus_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.k_8s_cluster_region_id):
            query['K8sClusterRegionId'] = request.k_8s_cluster_region_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterPrometheus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_prometheus(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_prometheus_with_options(request, runtime)

    async def describe_cluster_prometheus_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_prometheus_with_options_async(request, runtime)

    def describe_clusters_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_in_service_mesh_with_options(request, runtime)

    async def describe_clusters_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_in_service_mesh_with_options_async(request, runtime)

    def describe_cr_templates_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCrTemplates',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCrTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cr_templates_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCrTemplates',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCrTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cr_templates(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cr_templates_with_options(request, runtime)

    async def describe_cr_templates_async(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cr_templates_with_options_async(request, runtime)

    def describe_eip_resources_with_options(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEipResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeEipResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eip_resources_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEipResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeEipResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eip_resources(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_resources_with_options(request, runtime)

    async def describe_eip_resources_async(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_resources_with_options_async(request, runtime)

    def describe_gateway_secret_details_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGatewaySecretDetails',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_secret_details_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGatewaySecretDetails',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_secret_details(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_secret_details_with_options(request, runtime)

    async def describe_gateway_secret_details_async(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_secret_details_with_options_async(request, runtime)

    def describe_guest_cluster_access_log_dashboards_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterAccessLogDashboards',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_access_log_dashboards_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterAccessLogDashboards',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_access_log_dashboards(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_access_log_dashboards_with_options(request, runtime)

    async def describe_guest_cluster_access_log_dashboards_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_access_log_dashboards_with_options_async(request, runtime)

    def describe_guest_cluster_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.show_ns_labels):
            body['ShowNsLabels'] = request.show_ns_labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.show_ns_labels):
            body['ShowNsLabels'] = request.show_ns_labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_namespaces(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_namespaces_with_options(request, runtime)

    async def describe_guest_cluster_namespaces_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_namespaces_with_options_async(request, runtime)

    def describe_guest_cluster_pods_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterPods',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterPodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_pods_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterPods',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterPodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_pods(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_pods_with_options(request, runtime)

    async def describe_guest_cluster_pods_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_pods_with_options_async(request, runtime)

    def describe_imported_services_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImportedServicesDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeImportedServicesDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imported_services_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImportedServicesDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeImportedServicesDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imported_services_detail(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_imported_services_detail_with_options(request, runtime)

    async def describe_imported_services_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_imported_services_detail_with_options_async(request, runtime)

    def describe_istio_gateway_domains_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_istio_gateway_domains_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_istio_gateway_domains(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_istio_gateway_domains_with_options(request, runtime)

    async def describe_istio_gateway_domains_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_istio_gateway_domains_with_options_async(request, runtime)

    def describe_istio_gateway_route_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRouteDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_istio_gateway_route_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRouteDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_istio_gateway_route_detail(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_istio_gateway_route_detail_with_options(request, runtime)

    async def describe_istio_gateway_route_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_istio_gateway_route_detail_with_options_async(request, runtime)

    def describe_istio_gateway_routes_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_istio_gateway_routes_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_istio_gateway_routes(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_istio_gateway_routes_with_options(request, runtime)

    async def describe_istio_gateway_routes_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_istio_gateway_routes_with_options_async(request, runtime)

    def describe_metadata_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeMetadataResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMetadata',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metadata_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeMetadataResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMetadata',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metadata(self) -> servicemesh_20200111_models.DescribeMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metadata_with_options(runtime)

    async def describe_metadata_async(self) -> servicemesh_20200111_models.DescribeMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metadata_with_options_async(runtime)

    def describe_namespace_scope_sidecar_config_with_options(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_scope_sidecar_config_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_scope_sidecar_config(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_namespace_scope_sidecar_config_with_options(request, runtime)

    async def describe_namespace_scope_sidecar_config_async(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_namespace_scope_sidecar_config_with_options_async(request, runtime)

    def describe_nodes_instance_type_with_options(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodesInstanceType',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNodesInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nodes_instance_type_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodesInstanceType',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNodesInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nodes_instance_type(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nodes_instance_type_with_options(request, runtime)

    async def describe_nodes_instance_type_async(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nodes_instance_type_with_options_async(request, runtime)

    def describe_reusable_slb_with_options(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReusableSlb',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeReusableSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reusable_slb_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReusableSlb',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeReusableSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reusable_slb(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reusable_slb_with_options(request, runtime)

    async def describe_reusable_slb_async(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reusable_slb_with_options_async(request, runtime)

    def describe_service_mesh_additional_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_mode):
            body['CheckMode'] = request.check_mode
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_additional_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_mode):
            body['CheckMode'] = request.check_mode
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_additional_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_additional_status_with_options(request, runtime)

    async def describe_service_mesh_additional_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_additional_status_with_options_async(request, runtime)

    def describe_service_mesh_clusters_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshClusters',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_clusters_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshClusters',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_clusters(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_clusters_with_options(request, runtime)

    async def describe_service_mesh_clusters_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_clusters_with_options_async(request, runtime)

    def describe_service_mesh_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_detail(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_detail_with_options(request, runtime)

    async def describe_service_mesh_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_detail_with_options_async(request, runtime)

    def describe_service_mesh_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_kubeconfig(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_kubeconfig_with_options(request, runtime)

    async def describe_service_mesh_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_kubeconfig_with_options_async(request, runtime)

    def describe_service_mesh_logs_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshLogs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_logs_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshLogs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_logs(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_logs_with_options(request, runtime)

    async def describe_service_mesh_logs_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_logs_with_options_async(request, runtime)

    def describe_service_mesh_proxy_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshProxyStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_proxy_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshProxyStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_proxy_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_proxy_status_with_options(request, runtime)

    async def describe_service_mesh_proxy_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_proxy_status_with_options_async(request, runtime)

    def describe_service_mesh_upgrade_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.all_istio_gateway_full_names):
            body['AllIstioGatewayFullNames'] = request.all_istio_gateway_full_names
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshUpgradeStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_upgrade_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.all_istio_gateway_full_names):
            body['AllIstioGatewayFullNames'] = request.all_istio_gateway_full_names
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshUpgradeStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_upgrade_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_upgrade_status_with_options(request, runtime)

    async def describe_service_mesh_upgrade_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_upgrade_status_with_options_async(request, runtime)

    def describe_service_mesh_vms_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated
        
        @param request: DescribeServiceMeshVMsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshVMs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshVMsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_vms_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated
        
        @param request: DescribeServiceMeshVMsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshVMs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshVMsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_vms(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated
        
        @param request: DescribeServiceMeshVMsRequest
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_vms_with_options(request, runtime)

    async def describe_service_mesh_vms_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated
        
        @param request: DescribeServiceMeshVMsRequest
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_vms_with_options_async(request, runtime)

    def describe_service_meshes_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeServiceMeshes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_meshes_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeServiceMeshes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_meshes(self) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_meshes_with_options(runtime)

    async def describe_service_meshes_async(self) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_meshes_with_options_async(runtime)

    def describe_upgrade_version_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upgrade_version_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_upgrade_version(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_version_with_options(request, runtime)

    async def describe_upgrade_version_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upgrade_version_with_options_async(request, runtime)

    def describe_user_permissions_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_permissions_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_permissions(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_permissions_with_options(request, runtime)

    async def describe_user_permissions_async(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_permissions_with_options_async(request, runtime)

    def describe_users_with_permissions_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsersWithPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUsersWithPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_with_permissions_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsersWithPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUsersWithPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users_with_permissions(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_permissions_with_options(request, runtime)

    async def describe_users_with_permissions_async(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_with_permissions_with_options_async(request, runtime)

    def describe_vms_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated
        
        @param request: DescribeVMsInServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVMsInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVMsInServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vms_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated
        
        @param request: DescribeVMsInServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVMsInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVMsInServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vms_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated
        
        @param request: DescribeVMsInServiceMeshRequest
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vms_in_service_mesh_with_options(request, runtime)

    async def describe_vms_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated
        
        @param request: DescribeVMsInServiceMeshRequest
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vms_in_service_mesh_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_versions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVersionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVersions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_versions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVersionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVersions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_versions(self) -> servicemesh_20200111_models.DescribeVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_versions_with_options(runtime)

    async def describe_versions_async(self) -> servicemesh_20200111_models.DescribeVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_versions_with_options_async(runtime)

    def describe_vpcs_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def get_ca_cert_with_options(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCaCert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ca_cert_with_options_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCaCert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ca_cert(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ca_cert_with_options(request, runtime)

    async def get_ca_cert_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ca_cert_with_options_async(request, runtime)

    def get_deployment_by_selector_with_options(
        self,
        tmp_req: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GetDeploymentBySelectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'LabelSelector', 'json')
        body = {}
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.label_selector_shrink):
            body['LabelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.mark):
            body['Mark'] = request.mark
        if not UtilClient.is_unset(request.name_space):
            body['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeploymentBySelector',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDeploymentBySelectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_by_selector_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GetDeploymentBySelectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'LabelSelector', 'json')
        body = {}
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.label_selector_shrink):
            body['LabelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.mark):
            body['Mark'] = request.mark
        if not UtilClient.is_unset(request.name_space):
            body['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeploymentBySelector',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDeploymentBySelectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_by_selector(
        self,
        request: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_by_selector_with_options(request, runtime)

    async def get_deployment_by_selector_async(
        self,
        request: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_deployment_by_selector_with_options_async(request, runtime)

    def get_grafana_dashboard_url_with_options(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGrafanaDashboardUrl',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetGrafanaDashboardUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_grafana_dashboard_url_with_options_async(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGrafanaDashboardUrl',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetGrafanaDashboardUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_grafana_dashboard_url(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_grafana_dashboard_url_with_options(request, runtime)

    async def get_grafana_dashboard_url_async(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_grafana_dashboard_url_with_options_async(request, runtime)

    def get_registered_service_endpoints_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceEndpoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_service_endpoints_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceEndpoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_service_endpoints(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_endpoints_with_options(request, runtime)

    async def get_registered_service_endpoints_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_endpoints_with_options_async(request, runtime)

    def get_registered_service_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_service_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_service_namespaces(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_namespaces_with_options(request, runtime)

    async def get_registered_service_namespaces_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_namespaces_with_options_async(request, runtime)

    def get_swim_lane_detail_with_options(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_swim_lane_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_swim_lane_detail(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_swim_lane_detail_with_options(request, runtime)

    async def get_swim_lane_detail_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_swim_lane_detail_with_options_async(request, runtime)

    def get_swim_lane_group_list_with_options(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneGroupList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_swim_lane_group_list_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneGroupList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_swim_lane_group_list(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_swim_lane_group_list_with_options(request, runtime)

    async def get_swim_lane_group_list_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_swim_lane_group_list_with_options_async(request, runtime)

    def get_swim_lane_list_with_options(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_swim_lane_list_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_swim_lane_list(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_swim_lane_list_with_options(request, runtime)

    async def get_swim_lane_list_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_swim_lane_list_with_options_async(request, runtime)

    def get_vm_app_mesh_info_with_options(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated
        
        @param request: GetVmAppMeshInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmAppMeshInfo',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vm_app_mesh_info_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated
        
        @param request: GetVmAppMeshInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmAppMeshInfo',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vm_app_mesh_info(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated
        
        @param request: GetVmAppMeshInfoRequest
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vm_app_mesh_info_with_options(request, runtime)

    async def get_vm_app_mesh_info_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated
        
        @param request: GetVmAppMeshInfoRequest
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_app_mesh_info_with_options_async(request, runtime)

    def get_vm_meta_with_options(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated
        
        @param request: GetVmMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmMetaResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmMeta',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vm_meta_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated
        
        @param request: GetVmMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmMetaResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmMeta',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vm_meta(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated
        
        @param request: GetVmMetaRequest
        @return: GetVmMetaResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vm_meta_with_options(request, runtime)

    async def get_vm_meta_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated
        
        @param request: GetVmMetaRequest
        @return: GetVmMetaResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_meta_with_options_async(request, runtime)

    def grant_user_permissions_with_options(
        self,
        tmp_req: servicemesh_20200111_models.GrantUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GrantUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_account_user_ids):
            request.sub_account_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_account_user_ids, 'SubAccountUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        if not UtilClient.is_unset(request.sub_account_user_ids_shrink):
            body['SubAccountUserIds'] = request.sub_account_user_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GrantUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_user_permissions_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.GrantUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GrantUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_account_user_ids):
            request.sub_account_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_account_user_ids, 'SubAccountUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        if not UtilClient.is_unset(request.sub_account_user_ids_shrink):
            body['SubAccountUserIds'] = request.sub_account_user_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GrantUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_user_permissions(
        self,
        request: servicemesh_20200111_models.GrantUserPermissionsRequest,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_user_permissions_with_options(request, runtime)

    async def grant_user_permissions_async(
        self,
        request: servicemesh_20200111_models.GrantUserPermissionsRequest,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_user_permissions_with_options_async(request, runtime)

    def modify_api_server_eip_resource_with_options(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['ApiServerEipId'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApiServerEipResource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyApiServerEipResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_server_eip_resource_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['ApiServerEipId'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApiServerEipResource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyApiServerEipResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_server_eip_resource(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_server_eip_resource_with_options(request, runtime)

    async def modify_api_server_eip_resource_async(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_server_eip_resource_with_options_async(request, runtime)

    def modify_service_mesh_name_with_options(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceMeshName',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyServiceMeshNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_mesh_name_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceMeshName',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyServiceMeshNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_mesh_name(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_service_mesh_name_with_options(request, runtime)

    async def modify_service_mesh_name_async(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_mesh_name_with_options_async(request, runtime)

    def re_activate_audit_with_options(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        Before you call this operation, make sure that you understand the billing methods of Log Service. For more information, visit the [pricing page](https://www.aliyun.com/price/product?spm=5176.10695662.1119587.4.194c6a67rcPWQH#/sls/detail).
        
        @param request: ReActivateAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReActivateAuditResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReActivateAudit',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ReActivateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_activate_audit_with_options_async(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        Before you call this operation, make sure that you understand the billing methods of Log Service. For more information, visit the [pricing page](https://www.aliyun.com/price/product?spm=5176.10695662.1119587.4.194c6a67rcPWQH#/sls/detail).
        
        @param request: ReActivateAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReActivateAuditResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReActivateAudit',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ReActivateAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_activate_audit(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        Before you call this operation, make sure that you understand the billing methods of Log Service. For more information, visit the [pricing page](https://www.aliyun.com/price/product?spm=5176.10695662.1119587.4.194c6a67rcPWQH#/sls/detail).
        
        @param request: ReActivateAuditRequest
        @return: ReActivateAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.re_activate_audit_with_options(request, runtime)

    async def re_activate_audit_async(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        Before you call this operation, make sure that you understand the billing methods of Log Service. For more information, visit the [pricing page](https://www.aliyun.com/price/product?spm=5176.10695662.1119587.4.194c6a67rcPWQH#/sls/detail).
        
        @param request: ReActivateAuditRequest
        @return: ReActivateAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.re_activate_audit_with_options_async(request, runtime)

    def remove_cluster_from_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.reserve_namespace):
            body['ReserveNamespace'] = request.reserve_namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_from_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.reserve_namespace):
            body['ReserveNamespace'] = request.reserve_namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster_from_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_from_service_mesh_with_options(request, runtime)

    async def remove_cluster_from_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cluster_from_service_mesh_with_options_async(request, runtime)

    def remove_vmfrom_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated
        
        @param request: RemoveVMFromServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVMFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVMFromServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vmfrom_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated
        
        @param request: RemoveVMFromServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVMFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVMFromServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vmfrom_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated
        
        @param request: RemoveVMFromServiceMeshRequest
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_vmfrom_service_mesh_with_options(request, runtime)

    async def remove_vmfrom_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated
        
        @param request: RemoveVMFromServiceMeshRequest
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_vmfrom_service_mesh_with_options_async(request, runtime)

    def revoke_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RevokeKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RevokeKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_kubeconfig(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_kubeconfig_with_options(request, runtime)

    async def revoke_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_kubeconfig_with_options_async(request, runtime)

    def update_asmgateway_with_options(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asmgateway_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asmgateway(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_asmgateway_with_options(request, runtime)

    async def update_asmgateway_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_asmgateway_with_options_async(request, runtime)

    def update_asmgateway_imported_services_with_options(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_names):
            body['ServiceNames'] = request.service_names
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asmgateway_imported_services_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_names):
            body['ServiceNames'] = request.service_names
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asmgateway_imported_services(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_asmgateway_imported_services_with_options(request, runtime)

    async def update_asmgateway_imported_services_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_asmgateway_imported_services_with_options_async(request, runtime)

    def update_asmnamespace_from_guest_cluster_with_options(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMNamespaceFromGuestCluster',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asmnamespace_from_guest_cluster_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMNamespaceFromGuestCluster',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asmnamespace_from_guest_cluster(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_asmnamespace_from_guest_cluster_with_options(request, runtime)

    async def update_asmnamespace_from_guest_cluster_async(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_asmnamespace_from_guest_cluster_with_options_async(request, runtime)

    def update_istio_gateway_routes_with_options(
        self,
        tmp_req: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_gateway_routes_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_gateway_routes(
        self,
        request: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_istio_gateway_routes_with_options(request, runtime)

    async def update_istio_gateway_routes_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_gateway_routes_with_options_async(request, runtime)

    def update_istio_injection_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_plane_mode):
            body['DataPlaneMode'] = request.data_plane_mode
        if not UtilClient.is_unset(request.enable_istio_injection):
            body['EnableIstioInjection'] = request.enable_istio_injection
        if not UtilClient.is_unset(request.enable_sidecar_set_injection):
            body['EnableSidecarSetInjection'] = request.enable_sidecar_set_injection
        if not UtilClient.is_unset(request.istio_rev):
            body['IstioRev'] = request.istio_rev
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioInjectionConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_injection_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_plane_mode):
            body['DataPlaneMode'] = request.data_plane_mode
        if not UtilClient.is_unset(request.enable_istio_injection):
            body['EnableIstioInjection'] = request.enable_istio_injection
        if not UtilClient.is_unset(request.enable_sidecar_set_injection):
            body['EnableSidecarSetInjection'] = request.enable_sidecar_set_injection
        if not UtilClient.is_unset(request.istio_rev):
            body['IstioRev'] = request.istio_rev
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioInjectionConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_injection_config(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_istio_injection_config_with_options(request, runtime)

    async def update_istio_injection_config_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_injection_config_with_options_async(request, runtime)

    def update_istio_route_additional_status_with_options(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_name):
            query['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioRouteAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_route_additional_status_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_name):
            query['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioRouteAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_route_additional_status(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_istio_route_additional_status_with_options(request, runtime)

    async def update_istio_route_additional_status_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_route_additional_status_with_options_async(request, runtime)

    def update_mesh_craggregation_with_options(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpulimit):
            body['CPULimit'] = request.cpulimit
        if not UtilClient.is_unset(request.cpurequirement):
            body['CPURequirement'] = request.cpurequirement
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.memory_limit):
            body['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_requirement):
            body['MemoryRequirement'] = request.memory_requirement
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.use_public_api_server):
            body['UsePublicApiServer'] = request.use_public_api_server
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshCRAggregation',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshCRAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mesh_craggregation_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpulimit):
            body['CPULimit'] = request.cpulimit
        if not UtilClient.is_unset(request.cpurequirement):
            body['CPURequirement'] = request.cpurequirement
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.memory_limit):
            body['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_requirement):
            body['MemoryRequirement'] = request.memory_requirement
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.use_public_api_server):
            body['UsePublicApiServer'] = request.use_public_api_server
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshCRAggregation',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshCRAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mesh_craggregation(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_craggregation_with_options(request, runtime)

    async def update_mesh_craggregation_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_craggregation_with_options_async(request, runtime)

    def update_mesh_feature_with_options(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_gateway_lifecycle):
            body['AccessLogGatewayLifecycle'] = request.access_log_gateway_lifecycle
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.access_log_sidecar_lifecycle):
            body['AccessLogSidecarLifecycle'] = request.access_log_sidecar_lifecycle
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_injection_policy_enabled):
            body['AutoInjectionPolicyEnabled'] = request.auto_injection_policy_enabled
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cni_enabled):
            body['CniEnabled'] = request.cni_enabled
        if not UtilClient.is_unset(request.cni_exclude_namespaces):
            body['CniExcludeNamespaces'] = request.cni_exclude_namespaces
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.default_components_schedule_config):
            body['DefaultComponentsScheduleConfig'] = request.default_components_schedule_config
        if not UtilClient.is_unset(request.discovery_selectors):
            body['DiscoverySelectors'] = request.discovery_selectors
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_auto_diagnosis):
            body['EnableAutoDiagnosis'] = request.enable_auto_diagnosis
        if not UtilClient.is_unset(request.enable_bootstrap_xds_agent):
            body['EnableBootstrapXdsAgent'] = request.enable_bootstrap_xds_agent
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_namespaces_by_default):
            body['EnableNamespacesByDefault'] = request.enable_namespaces_by_default
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.http_10enabled):
            body['Http10Enabled'] = request.http_10enabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.integrate_kiali):
            body['IntegrateKiali'] = request.integrate_kiali
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.kiali_arms_auth_tokens):
            body['KialiArmsAuthTokens'] = request.kiali_arms_auth_tokens
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.kiali_service_annotations):
            body['KialiServiceAnnotations'] = request.kiali_service_annotations
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.nfdenabled):
            body['NFDEnabled'] = request.nfdenabled
        if not UtilClient.is_unset(request.nfdlabel_pruned):
            body['NFDLabelPruned'] = request.nfdlabel_pruned
        if not UtilClient.is_unset(request.opainjector_cpulimit):
            body['OPAInjectorCPULimit'] = request.opainjector_cpulimit
        if not UtilClient.is_unset(request.opainjector_cpurequirement):
            body['OPAInjectorCPURequirement'] = request.opainjector_cpurequirement
        if not UtilClient.is_unset(request.opainjector_memory_limit):
            body['OPAInjectorMemoryLimit'] = request.opainjector_memory_limit
        if not UtilClient.is_unset(request.opainjector_memory_requirement):
            body['OPAInjectorMemoryRequirement'] = request.opainjector_memory_requirement
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opascope_injected):
            body['OPAScopeInjected'] = request.opascope_injected
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.outbound_traffic_policy):
            body['OutboundTrafficPolicy'] = request.outbound_traffic_policy
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_injector_limit_cpu):
            body['SidecarInjectorLimitCPU'] = request.sidecar_injector_limit_cpu
        if not UtilClient.is_unset(request.sidecar_injector_limit_memory):
            body['SidecarInjectorLimitMemory'] = request.sidecar_injector_limit_memory
        if not UtilClient.is_unset(request.sidecar_injector_request_cpu):
            body['SidecarInjectorRequestCPU'] = request.sidecar_injector_request_cpu
        if not UtilClient.is_unset(request.sidecar_injector_request_memory):
            body['SidecarInjectorRequestMemory'] = request.sidecar_injector_request_memory
        if not UtilClient.is_unset(request.sidecar_injector_webhook_as_yaml):
            body['SidecarInjectorWebhookAsYaml'] = request.sidecar_injector_webhook_as_yaml
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_custom_tags):
            body['TraceCustomTags'] = request.trace_custom_tags
        if not UtilClient.is_unset(request.trace_max_path_tag_length):
            body['TraceMaxPathTagLength'] = request.trace_max_path_tag_length
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_cpu):
            body['TracingOnExtZipkinLimitCPU'] = request.tracing_on_ext_zipkin_limit_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_memory):
            body['TracingOnExtZipkinLimitMemory'] = request.tracing_on_ext_zipkin_limit_memory
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_cpu):
            body['TracingOnExtZipkinRequestCPU'] = request.tracing_on_ext_zipkin_request_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_memory):
            body['TracingOnExtZipkinRequestMemory'] = request.tracing_on_ext_zipkin_request_memory
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshFeature',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mesh_feature_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_gateway_lifecycle):
            body['AccessLogGatewayLifecycle'] = request.access_log_gateway_lifecycle
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.access_log_sidecar_lifecycle):
            body['AccessLogSidecarLifecycle'] = request.access_log_sidecar_lifecycle
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_injection_policy_enabled):
            body['AutoInjectionPolicyEnabled'] = request.auto_injection_policy_enabled
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cni_enabled):
            body['CniEnabled'] = request.cni_enabled
        if not UtilClient.is_unset(request.cni_exclude_namespaces):
            body['CniExcludeNamespaces'] = request.cni_exclude_namespaces
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.default_components_schedule_config):
            body['DefaultComponentsScheduleConfig'] = request.default_components_schedule_config
        if not UtilClient.is_unset(request.discovery_selectors):
            body['DiscoverySelectors'] = request.discovery_selectors
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_auto_diagnosis):
            body['EnableAutoDiagnosis'] = request.enable_auto_diagnosis
        if not UtilClient.is_unset(request.enable_bootstrap_xds_agent):
            body['EnableBootstrapXdsAgent'] = request.enable_bootstrap_xds_agent
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_namespaces_by_default):
            body['EnableNamespacesByDefault'] = request.enable_namespaces_by_default
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.http_10enabled):
            body['Http10Enabled'] = request.http_10enabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.integrate_kiali):
            body['IntegrateKiali'] = request.integrate_kiali
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.kiali_arms_auth_tokens):
            body['KialiArmsAuthTokens'] = request.kiali_arms_auth_tokens
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.kiali_service_annotations):
            body['KialiServiceAnnotations'] = request.kiali_service_annotations
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.nfdenabled):
            body['NFDEnabled'] = request.nfdenabled
        if not UtilClient.is_unset(request.nfdlabel_pruned):
            body['NFDLabelPruned'] = request.nfdlabel_pruned
        if not UtilClient.is_unset(request.opainjector_cpulimit):
            body['OPAInjectorCPULimit'] = request.opainjector_cpulimit
        if not UtilClient.is_unset(request.opainjector_cpurequirement):
            body['OPAInjectorCPURequirement'] = request.opainjector_cpurequirement
        if not UtilClient.is_unset(request.opainjector_memory_limit):
            body['OPAInjectorMemoryLimit'] = request.opainjector_memory_limit
        if not UtilClient.is_unset(request.opainjector_memory_requirement):
            body['OPAInjectorMemoryRequirement'] = request.opainjector_memory_requirement
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opascope_injected):
            body['OPAScopeInjected'] = request.opascope_injected
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.outbound_traffic_policy):
            body['OutboundTrafficPolicy'] = request.outbound_traffic_policy
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_injector_limit_cpu):
            body['SidecarInjectorLimitCPU'] = request.sidecar_injector_limit_cpu
        if not UtilClient.is_unset(request.sidecar_injector_limit_memory):
            body['SidecarInjectorLimitMemory'] = request.sidecar_injector_limit_memory
        if not UtilClient.is_unset(request.sidecar_injector_request_cpu):
            body['SidecarInjectorRequestCPU'] = request.sidecar_injector_request_cpu
        if not UtilClient.is_unset(request.sidecar_injector_request_memory):
            body['SidecarInjectorRequestMemory'] = request.sidecar_injector_request_memory
        if not UtilClient.is_unset(request.sidecar_injector_webhook_as_yaml):
            body['SidecarInjectorWebhookAsYaml'] = request.sidecar_injector_webhook_as_yaml
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_custom_tags):
            body['TraceCustomTags'] = request.trace_custom_tags
        if not UtilClient.is_unset(request.trace_max_path_tag_length):
            body['TraceMaxPathTagLength'] = request.trace_max_path_tag_length
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_cpu):
            body['TracingOnExtZipkinLimitCPU'] = request.tracing_on_ext_zipkin_limit_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_memory):
            body['TracingOnExtZipkinLimitMemory'] = request.tracing_on_ext_zipkin_limit_memory
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_cpu):
            body['TracingOnExtZipkinRequestCPU'] = request.tracing_on_ext_zipkin_request_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_memory):
            body['TracingOnExtZipkinRequestMemory'] = request.tracing_on_ext_zipkin_request_memory
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshFeature',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mesh_feature(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_feature_with_options(request, runtime)

    async def update_mesh_feature_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_feature_with_options_async(request, runtime)

    def update_namespace_scope_sidecar_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.istio_dnsproxy_enabled):
            body['IstioDNSProxyEnabled'] = request.istio_dnsproxy_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.post_start):
            body['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            body['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_limit):
            body['ProxyInitAckSloCPUResourceLimit'] = request.proxy_init_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_request):
            body['ProxyInitAckSloCPUResourceRequest'] = request.proxy_init_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_limit):
            body['ProxyInitAckSloMemoryResourceLimit'] = request.proxy_init_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_request):
            body['ProxyInitAckSloMemoryResourceRequest'] = request.proxy_init_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_metadata):
            body['ProxyMetadata'] = request.proxy_metadata
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_limit):
            body['SidecarProxyAckSloCPUResourceLimit'] = request.sidecar_proxy_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_request):
            body['SidecarProxyAckSloCPUResourceRequest'] = request.sidecar_proxy_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_limit):
            body['SidecarProxyAckSloMemoryResourceLimit'] = request.sidecar_proxy_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_request):
            body['SidecarProxyAckSloMemoryResourceRequest'] = request.sidecar_proxy_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_limit):
            body['SidecarProxyCPUResourceLimit'] = request.sidecar_proxy_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_request):
            body['SidecarProxyCPUResourceRequest'] = request.sidecar_proxy_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_limit):
            body['SidecarProxyMemoryResourceLimit'] = request.sidecar_proxy_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_request):
            body['SidecarProxyMemoryResourceRequest'] = request.sidecar_proxy_memory_resource_request
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_scope_sidecar_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.istio_dnsproxy_enabled):
            body['IstioDNSProxyEnabled'] = request.istio_dnsproxy_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.post_start):
            body['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            body['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_limit):
            body['ProxyInitAckSloCPUResourceLimit'] = request.proxy_init_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_request):
            body['ProxyInitAckSloCPUResourceRequest'] = request.proxy_init_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_limit):
            body['ProxyInitAckSloMemoryResourceLimit'] = request.proxy_init_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_request):
            body['ProxyInitAckSloMemoryResourceRequest'] = request.proxy_init_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_metadata):
            body['ProxyMetadata'] = request.proxy_metadata
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_limit):
            body['SidecarProxyAckSloCPUResourceLimit'] = request.sidecar_proxy_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_request):
            body['SidecarProxyAckSloCPUResourceRequest'] = request.sidecar_proxy_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_limit):
            body['SidecarProxyAckSloMemoryResourceLimit'] = request.sidecar_proxy_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_request):
            body['SidecarProxyAckSloMemoryResourceRequest'] = request.sidecar_proxy_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_limit):
            body['SidecarProxyCPUResourceLimit'] = request.sidecar_proxy_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_request):
            body['SidecarProxyCPUResourceRequest'] = request.sidecar_proxy_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_limit):
            body['SidecarProxyMemoryResourceLimit'] = request.sidecar_proxy_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_request):
            body['SidecarProxyMemoryResourceRequest'] = request.sidecar_proxy_memory_resource_request
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_scope_sidecar_config(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_scope_sidecar_config_with_options(request, runtime)

    async def update_namespace_scope_sidecar_config_async(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_namespace_scope_sidecar_config_with_options_async(request, runtime)

    def update_swim_lane_with_options(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swim_lane_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swim_lane(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_swim_lane_with_options(request, runtime)

    async def update_swim_lane_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_swim_lane_with_options_async(request, runtime)

    def update_swim_lane_group_with_options(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swim_lane_group_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swim_lane_group(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_swim_lane_group_with_options(request, runtime)

    async def update_swim_lane_group_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_swim_lane_group_with_options_async(request, runtime)

    def upgrade_mesh_edition_partially_with_options(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_continue):
            body['ASMGatewayContinue'] = request.asmgateway_continue
        if not UtilClient.is_unset(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not UtilClient.is_unset(request.pre_check):
            body['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.switch_to_pro):
            body['SwitchToPro'] = request.switch_to_pro
        if not UtilClient.is_unset(request.upgrade_gateway_records):
            body['UpgradeGatewayRecords'] = request.upgrade_gateway_records
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeMeshEditionPartially',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_mesh_edition_partially_with_options_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_continue):
            body['ASMGatewayContinue'] = request.asmgateway_continue
        if not UtilClient.is_unset(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not UtilClient.is_unset(request.pre_check):
            body['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.switch_to_pro):
            body['SwitchToPro'] = request.switch_to_pro
        if not UtilClient.is_unset(request.upgrade_gateway_records):
            body['UpgradeGatewayRecords'] = request.upgrade_gateway_records
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeMeshEditionPartially',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_mesh_edition_partially(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_edition_partially_with_options(request, runtime)

    async def upgrade_mesh_edition_partially_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_mesh_edition_partially_with_options_async(request, runtime)

    def upgrade_mesh_version_with_options(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_check):
            query['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMeshVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_mesh_version_with_options_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_check):
            query['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMeshVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_mesh_version(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_version_with_options(request, runtime)

    async def upgrade_mesh_version_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_mesh_version_with_options_async(request, runtime)
