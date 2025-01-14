import json
from copy import deepcopy
from pathlib import Path

import pytest

from definition_tooling.validator import errors as err
from definition_tooling.validator.core import DefinitionValidator

# Note: It's easier to get some 100% valid spec and corrupt it
# instead of having multiple incorrect specs in the repo

SPECS_ROOT_DIR = Path(__file__).absolute().parent / "data"
COMPANY_BASIC_INFO: dict = json.loads(
    (SPECS_ROOT_DIR / "CompanyBasicInfo.json").read_text(encoding="utf8")
)


def check_validation_error(tmp_path, spec: dict, exception):
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(spec))
    with pytest.raises(exception):
        DefinitionValidator(spec_path).validate()


@pytest.mark.parametrize("method", ["get", "put", "delete"])
def test_standards_has_non_post_method(method, tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    spec["paths"]["/draft/Company/BasicInfo"][method] = {
        "description": "Method which should not exist"
    }
    check_validation_error(tmp_path, spec, err.OnlyPostMethodAllowed)


def test_post_method_is_missing(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    del spec["paths"]["/draft/Company/BasicInfo"]["post"]
    check_validation_error(tmp_path, spec, err.PostMethodIsMissing)


def test_many_endpoints(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    spec["paths"]["/pets"] = {"post": {"description": "Pet store, why not?"}}
    check_validation_error(tmp_path, spec, err.OnlyOneEndpointAllowed)


def test_no_endpoints(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    del spec["paths"]
    check_validation_error(tmp_path, spec, err.NoEndpointsDefined)


def test_missing_field_body_is_fine(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    del spec["paths"]["/draft/Company/BasicInfo"]["post"]["requestBody"]
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(spec))
    DefinitionValidator(spec_path).validate()


def test_missing_200_response(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    del spec["paths"]["/draft/Company/BasicInfo"]["post"]["responses"]["200"]
    check_validation_error(tmp_path, spec, err.ResponseBodyMissing)


def test_wrong_content_type_of_request_body(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    request_body = spec["paths"]["/draft/Company/BasicInfo"]["post"]["requestBody"]
    schema = deepcopy(request_body["content"]["application/json"])
    request_body["content"]["text/plan"] = schema
    del request_body["content"]["application/json"]
    check_validation_error(tmp_path, spec, err.WrongContentType)


def test_wrong_content_type_of_response(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    response = spec["paths"]["/draft/Company/BasicInfo"]["post"]["responses"]["200"]
    schema = deepcopy(response["content"]["application/json"])
    response["content"]["text/plan"] = schema
    del response["content"]["application/json"]
    check_validation_error(tmp_path, spec, err.WrongContentType)


def test_component_schema_is_missing(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    del spec["components"]["schemas"]
    check_validation_error(tmp_path, spec, err.SchemaMissing)


@pytest.mark.parametrize(
    "model_name", ["BasicCompanyInfoRequest", "BasicCompanyInfoResponse"]
)
def test_component_is_missing(model_name, tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    del spec["components"]["schemas"][model_name]
    check_validation_error(tmp_path, spec, err.SchemaMissing)


def test_non_existing_component_defined_in_body(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    body = spec["paths"]["/draft/Company/BasicInfo"]["post"]["requestBody"]
    body["content"]["application/json"]["schema"]["$ref"] += "blah"
    check_validation_error(tmp_path, spec, err.SchemaMissing)


def test_non_existing_component_defined_in_response(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    resp_200 = spec["paths"]["/draft/Company/BasicInfo"]["post"]["responses"]["200"]
    resp_200["content"]["application/json"]["schema"]["$ref"] += "blah"
    check_validation_error(tmp_path, spec, err.SchemaMissing)


def test_auth_header_is_missing(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    x_app_provider_header = {
        "schema": {"type": "string"},
        "in": "header",
        "name": "X-Authorization-Provider",
        "description": "Provider domain",
    }
    spec["paths"]["/draft/Company/BasicInfo"]["post"]["parameters"] = [
        x_app_provider_header
    ]
    check_validation_error(tmp_path, spec, err.AuthorizationHeaderMissing)


def test_auth_provider_header_is_missing(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    auth_header = {
        "schema": {"type": "string"},
        "in": "header",
        "name": "Authorization",
        "description": "User bearer token",
    }
    spec["paths"]["/draft/Company/BasicInfo"]["post"]["parameters"] = [auth_header]
    check_validation_error(tmp_path, spec, err.AuthProviderHeaderMissing)


def test_servers_are_defined(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    spec["servers"] = [{"url": "http://example.com"}]
    check_validation_error(tmp_path, spec, err.ServersShouldNotBeDefined)


def test_security_is_defined(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    spec["paths"]["/draft/Company/BasicInfo"]["post"]["security"] = {}
    check_validation_error(tmp_path, spec, err.SecurityShouldNotBeDefined)


def test_loading_non_json_file(tmp_path):
    spec_path = tmp_path / "spec.json"
    spec_path.write_text("weirdo content")
    with pytest.raises(err.InvalidJSON):
        DefinitionValidator(spec_path).validate()


def test_loading_unsupported_version(tmp_path):
    spec = deepcopy(COMPANY_BASIC_INFO)
    spec["openapi"] = "999.999.999"
    check_validation_error(tmp_path, spec, err.UnsupportedVersion)


@pytest.mark.parametrize("code", [401, 403, 404, 422, 444, 502, 503, 504, 550])
def test_http_errors_defined(tmp_path, code):
    spec = deepcopy(COMPANY_BASIC_INFO)
    spec["paths"]["/draft/Company/BasicInfo"]["post"]["responses"].pop(str(code), None)
    check_validation_error(tmp_path, spec, err.HTTPResponseIsMissing)
