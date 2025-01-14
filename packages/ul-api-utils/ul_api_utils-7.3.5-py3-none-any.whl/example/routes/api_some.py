from datetime import datetime, timedelta
from time import sleep
from typing import List, Optional, Tuple

from ul_db_utils.modules.db import db
from flask import jsonify
from pydantic import BaseModel

from werkzeug import Response as BaseResponse
from ul_api_utils.api_resource.api_request import ApiRequestQuery
from ul_api_utils.api_resource.api_resource import ApiResource
from ul_api_utils.api_resource.api_resource_config import ApiResourceConfig
from ul_api_utils.api_resource.api_response import FileApiResponse, JsonApiResponsePayload, JsonApiResponse, AnyJsonApiResponse, ProxyJsonApiResponse, HtmlApiResponse
from ul_api_utils.errors import Server5XXInternalApiError, NoResultFoundApiError, Client4XXInternalApiError
from ul_api_utils.internal_api.internal_api import InternalApi
from ul_api_utils.utils.api_encoding import ApiEncoding
from ul_api_utils.resources.health_check.health_check import HealthCheckContext
from ul_api_utils.validators.custom_fields import QueryParamsSeparatedList
from example.conf import sdk
from example.permissions import SOME_PERMISSION

internal_api = InternalApi(
    entry_point='http://localhost:5000',
    default_auth_token='',
)

internal_api_another_service = InternalApi(
    entry_point='http://localhost:5000',
    default_auth_token='',
)

internal_api_gzip = InternalApi(
    entry_point='http://localhost:5000',
    default_auth_token='',
    force_encoding=ApiEncoding.GZIP,
)


class RespObject(JsonApiResponsePayload):
    now: datetime
    notes: str = ''


class SomeBody(BaseModel):
    seconds: float


class Some2Query(ApiRequestQuery):
    sleep: float = 0.4
    some: QueryParamsSeparatedList[str]


@sdk.rest_api('POST', '/example-resource-simple', access=sdk.ACCESS_PUBLIC)
def some5(api_resource: ApiResource, body: SomeBody) -> JsonApiResponse[List[RespObject]]:
    return api_resource.response_ok([
        RespObject(now=datetime.now() + timedelta(seconds=body.seconds)),
        RespObject(now=datetime.now() + timedelta(seconds=body.seconds * 2)),
    ], 2)


class Some7Query(ApiRequestQuery):
    need_redirect: int


@sdk.rest_api('POST', '/example-resource-simple-any', access=sdk.ACCESS_PUBLIC)
def some9(api_resource: ApiResource) -> AnyJsonApiResponse:
    return api_resource.response_ok([RespObject(now=datetime.now(), notes="some9")], 1)


@sdk.rest_api('POST', '/example-resource-simple-any-private', access=SOME_PERMISSION)
def some9private(api_resource: ApiResource) -> AnyJsonApiResponse:
    return api_resource.response_ok([RespObject(now=datetime.now(), notes="some9")], 1)


@sdk.rest_api('POST', '/example-resource-simple-proxy', access=sdk.ACCESS_PUBLIC)
def some8(api_resource: ApiResource) -> JsonApiResponse[List[RespObject]]:
    return api_resource.response_ok([RespObject(now=datetime.now(), notes="some8")], 1)


@sdk.rest_api('POST', '/example-resource-simple-redirect-or-json', access=sdk.ACCESS_PUBLIC)
def some7(api_resource: ApiResource, query: Some7Query) -> JsonApiResponse[List[RespObject]]:
    if query.need_redirect > 0:
        return api_resource.response_redirect(sdk.url_for('some8'))  # type: ignore
    return api_resource.response_ok([RespObject(now=datetime.now(), notes="some7")], 1)


@sdk.rest_api('GET', '/example-resource-simple-proxy', access=sdk.ACCESS_PUBLIC)
def some6(api_resource: ApiResource) -> ProxyJsonApiResponse[List[RespObject]]:  # type: ignore
    res = internal_api.request_post('/example-resource-simple', json={'seconds': 123}).typed(List[RespObject]).check()
    assert res.payload[0].now is not None

    return api_resource.response_proxy(res)


@sdk.rest_api('GET', '/example-limiter', access=sdk.ACCESS_PUBLIC)
def some6limit(api_resource: ApiResource) -> JsonApiResponse[List[RespObject]]:
    return api_resource.response_ok([
        RespObject(now=datetime.now() + timedelta(seconds=4)),
        RespObject(now=datetime.now() + timedelta(seconds=5 * 2)),
    ], 2)


@sdk.rest_api('POST', '/example-resource-simple-list', access=sdk.ACCESS_PUBLIC)
def some4(api_resource: ApiResource, body: List[SomeBody]) -> JsonApiResponse[List[RespObject]]:
    return api_resource.response_ok([
        RespObject(now=datetime.now() + timedelta(seconds=body[0].seconds)),
        RespObject(now=datetime.now() + timedelta(seconds=body[0].seconds * 2)),
    ], 2)


@sdk.rest_api('POST', '/example-resource-simple-list-err', access=sdk.ACCESS_PUBLIC)
def some4err(api_resource: ApiResource, body: List[SomeBody]) -> JsonApiResponse[List[RespObject]]:
    raise ValueError('some error')


@sdk.rest_api('GET', '/example-resource-simple-not-found', access=sdk.ACCESS_PUBLIC)
def some5err(api_resource: ApiResource) -> JsonApiResponse[List[RespObject]]:
    raise NoResultFoundApiError()


@sdk.health_check()
def health_check(context: HealthCheckContext) -> None:
    def function_raises_error_example() -> None:
        raise TypeError('blabla')

    context.add_step("Function_raises_error_example", function_raises_error_example)
    context.check_database_connection_exists()
    context.check_internal_api_route(
        internal_api,
        "Check Example with 1 second sleep",
        '/example-resource-for-loong-sleep',
        q={'sleep': 1},
    )
    context.check_internal_api_route(
        internal_api,
        "Check another example",
        '/example-resource-empty',
    )
    context.check_internal_api_health(internal_api_another_service, "SELF_API")
    # context.check_message_queues_health(
    #     uni,
    #     override_limits = {
    #         "some_queue_name": HealthCheckMessageQueueRange(ok=2, warn=100),
    #     }
    # )


@sdk.rest_api('GET', '/example-resource', access=sdk.ACCESS_PUBLIC)
def some3(api_resource: ApiResource) -> JsonApiResponse[RespObject]:
    api_resource.logger.info('some 1')
    sleep(0.1)
    sess = db.session()
    sess.execute('SELECT * FROM information_schema.tables WHERE table_schema = \'pg_catalog\' LIMIT 4;')
    api_resource.logger.info('some 2')
    internal_api.request_get('/example-resource-for-loong-sleep', q={"sleep": 0.1}).check()
    api_resource.logger.info('some 3')
    internal_api.request_post('/example-resource-simple', q={"sleep": 0.1}, json={"seconds": 123}).check()
    api_resource.logger.info('some 4')
    internal_api.request_post('/example-resource-simple-list', q={"sleep": 0.1}, json=[{"seconds": 123}]).check()
    api_resource.logger.info('some 5')
    internal_api.request_post('/example-resource-simple-proxy', q={"sleep": 0.1}, json={"seconds": 123}).check()
    api_resource.logger.info('some 6')
    internal_api.request_post('/example-resource-simple-any', q={"sleep": 0.1}, json={"seconds": 123}).check()
    api_resource.logger.info('some 7')
    internal_api.request_post('/example-resource-simple-redirect-or-json', q={"need_redirect": 3}, json={"seconds": 123}).check()
    api_resource.logger.info('some 8')
    internal_api.request_post('/example-resource-simple-redirect-or-json', q={"need_redirect": -3}, json={"seconds": 123}).check()
    api_resource.logger.info('some 9')
    sess.execute('SELECT * FROM information_schema.tables LIMIT 4;')
    api_resource.logger.info('some 10')
    return api_resource.response_ok(RespObject(now=datetime.now()))


@sdk.html_view(('GET', 'OPTIONS'), '/example-resource-for-loong-sleep', access=sdk.ACCESS_PUBLIC)
def some2html(api_resource: ApiResource, query: Some2Query) -> HtmlApiResponse:
    raise NoResultFoundApiError()


@sdk.rest_api('GET', '/example-resource-for-loong-sleep', access=sdk.ACCESS_PUBLIC)
def some2(api_resource: ApiResource, query: Some2Query) -> JsonApiResponse[RespObject]:
    sess = db.session()
    sess.execute('SELECT * FROM information_schema.tables LIMIT 3;')
    sleep(query.sleep)
    sess.execute('SELECT * FROM information_schema.tables LIMIT 3;')
    return api_resource.response_ok(RespObject(now=datetime.now()))


@sdk.rest_api('GET', '/example-resource-empty', access=sdk.ACCESS_PUBLIC)
def some1(api_resource: ApiResource) -> JsonApiResponse[RespObject]:
    return api_resource.response_ok(RespObject(now=datetime.now()))


def test_override(res: Tuple[BaseResponse, int]) -> Tuple[BaseResponse, int]:
    return jsonify({'this is test': 'test'}), 500


@sdk.rest_api('GET', '/example-resource-override', access=sdk.ACCESS_PUBLIC, config=ApiResourceConfig(override_flask_response=test_override))
def override(api_resource: ApiResource) -> JsonApiResponse[RespObject]:
    return api_resource.response_ok(RespObject(now=datetime.now()))


@sdk.rest_api('POST', '/example-resource-empty-gzip', access=sdk.ACCESS_PUBLIC)
def some12(api_resource: ApiResource, body: List[SomeBody]) -> JsonApiResponse[RespObject]:
    sess = db.session()
    sess.execute('SELECT * FROM information_schema.tables LIMIT 3;')
    sleep(body[0].seconds)
    return api_resource.response_ok(RespObject(now=datetime.now()))


@sdk.html_view(('GET', 'POST'), '/', access=sdk.ACCESS_PUBLIC)
def view_home(api_resource: ApiResource, body: Optional[List[SomeBody]]) -> HtmlApiResponse:
    sleep(0.02)
    sess = db.session()

    resp = internal_api.request_get('/example-resource-simple-not-found')
    try:
        resp.check()
    except Client4XXInternalApiError:
        pass

    sess.execute('SELECT * FROM information_schema.tables LIMIT 100;')
    res = internal_api.request_get('/example-resource-empty').check()
    res2 = internal_api_gzip.request_post('/example-resource-empty-gzip', json=[{"seconds": 0.7} for i in range(1000)]).check()

    assert isinstance(res.payload_raw, dict)
    assert isinstance(res2.payload_raw, dict)
    assert res.payload_raw['now'] is not None
    sess.execute('SELECT * FROM information_schema.tables LIMIT 100;')
    sleep(0.3)

    try:
        internal_api.request_get('/example-resource').check()
    except Server5XXInternalApiError:
        pass

    try:
        internal_api.request_get('/example-resource-override').check()
    except Server5XXInternalApiError:
        pass

    resp = internal_api.request_get('/example-resource-for-405')
    try:
        resp.check()
    except Server5XXInternalApiError:
        pass

    sess.execute('SELECT * FROM information_schema.tables LIMIT 100;')
    try:
        internal_api.request_get('/example-resource-for-loong-sleep', q={"sleep": 0.4, "some": "1,2,3"}).check()
    except Server5XXInternalApiError:
        pass
    sess.execute('SELECT * FROM information_schema.tables LIMIT 100;')
    internal_api.request_get('/example-resource-for-loong-sleep', q={"sleep": 0.2, "some": "1,2,3"}).check()
    try:
        internal_api.request_post('/example-resource-simple-list-err', q={"sleep": 0.1}, json=[{"seconds": 123}]).check()
    except Server5XXInternalApiError:
        pass
    sleep(0.02)
    return api_resource.response_template('home.html.jinja2')


@sdk.file_download('GET', '/example-send-temp-file', access=sdk.ACCESS_PUBLIC)
def somefile(api_resource: ApiResource) -> FileApiResponse:
    fn = api_resource.mk_tmp_file()

    with open(fn, 'wt') as f:
        for i in range(1000_000):
            f.write(f'test {i}\n')

    return api_resource.response_file_ok(
        path_or_file=fn,
        mimetype='text/plain',
        as_attachment=True,
        attachment_filename='import_devices_log.txt',
    )
