import io
from datetime import datetime
from types import NoneType
from typing import TypeVar, Generic, List, Optional, Dict, Any, Callable, Union, BinaryIO, Tuple, Type
import msgpack
from flask import jsonify, send_file, redirect, Response, request
from pydantic import Extra
from pydantic.main import BaseModel
from werkzeug import Response as BaseResponse

from ul_api_utils.api_resource.db_types import TPayloadInputUnion
from ul_api_utils.const import RESPONSE_PROP_OK, RESPONSE_PROP_PAYLOAD, RESPONSE_PROP_COUNT, RESPONSE_PROP_TOTAL, RESPONSE_PROP_ERRORS, MIME__JSON, MIME__MSGPCK, \
    REQUEST_HEADER__ACCEPT
from ul_api_utils.debug.debugger import Debugger
from ul_api_utils.utils.json_encoder import CustomJSONEncoder


def msgpackify(response: Any) -> Response:
    flask_response = jsonify()
    enc = CustomJSONEncoder()
    flask_response.data = msgpack.packb(response, default=enc.default)
    flask_response.content_type = MIME__MSGPCK
    return flask_response


class ApiResponse(BaseModel):
    ok: bool
    status_code: int
    headers: Dict[str, str] = {}

    class Config:
        extra = Extra.forbid
        arbitrary_types_allowed = True

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        raise NotImplementedError()

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        raise NotImplementedError()


class RedirectApiResponse(ApiResponse):
    location: str
    status_code: int = 302

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        resp = redirect(
            self.location,
            code=self.status_code,
        )

        resp.headers.update(self.headers)

        return resp


class HtmlApiResponse(ApiResponse):
    content: str
    error: Optional[Exception] = None

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseNoneType(BaseModel):
            __root__: NoneType  # type: ignore
        return _ResponseNoneType

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        content = self.content
        debugger_content = debugger.render_html(self.status_code) if debugger is not None else ''

        if debugger_content:
            prev_len = len(content)
            content = content.replace('</body>', f'{debugger_content}</body>', 1)
            if len(content) == prev_len:
                content += debugger_content

        resp = Response(
            content,
            status=self.status_code,
        )

        resp.headers.update(self.headers)

        return resp


class FileApiResponse(ApiResponse):
    file_path: Union[str, BinaryIO, io.BytesIO]
    mimetype: Optional[str]  # it will be auto-detected by extension if mimetype==None
    as_attachment: bool = False
    download_name: Optional[str] = None
    attachment_filename: Optional[str] = None
    conditional: bool = True
    etag: Union[bool, str] = True
    add_etags: Optional[bool] = None
    last_modified: Optional[Union[datetime, int, float]] = None
    max_age: Optional[Union[int, Callable[[Optional[str]], Optional[int]]]] = None
    cache_timeout: Optional[int] = None

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseNoneType(BaseModel):
            __root__: NoneType  # type: ignore
        return _ResponseNoneType

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        resp = send_file(
            path_or_file=self.file_path,
            mimetype=self.mimetype,
            as_attachment=self.as_attachment,
            download_name=self.download_name,
            attachment_filename=self.attachment_filename,
            conditional=self.conditional,
            etag=self.etag,
            add_etags=self.add_etags,
            last_modified=self.last_modified,
            max_age=self.max_age,
            cache_timeout=self.cache_timeout,
        )

        resp.headers.update(self.headers)

        return resp


class EmptyJsonApiResponse(ApiResponse):

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseNoneType(BaseModel):
            __root__: NoneType  # type: ignore
        return _ResponseNoneType

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        resp = Response(response=None, status=self.status_code, mimetype=MIME__JSON)
        resp.headers.update(self.headers)
        return resp


class JsonApiResponsePayload(BaseModel):
    class Config:
        extra = Extra.ignore


TResultPayloadUnion = Union[None, Dict[str, Any], JsonApiResponsePayload, List[JsonApiResponsePayload], List[Dict[str, Any]]]
TPayloadTotalUnion = Union[
    Tuple[None, None],
    Tuple[Dict[str, Any], None],
    Tuple[JsonApiResponsePayload, None],
    Tuple[List[JsonApiResponsePayload], int],
    Tuple[List[Dict[str, Any]], int],
]


class DictJsonApiResponsePayload(JsonApiResponsePayload):
    __root__: Dict[str, Any]


TProxyPayload = TypeVar('TProxyPayload', bound=Union[JsonApiResponsePayload, List[JsonApiResponsePayload], None])


class ProxyJsonApiResponse(Generic[TProxyPayload], EmptyJsonApiResponse):
    response: Dict[str, Any]

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseStd(BaseModel):
            ok: bool
            payload: inner_type  # type: ignore
            errors: List[Dict[str, Any]]
            total_count: Optional[int] = None
            count: Optional[int] = None
        return _ResponseStd

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        resp = jsonify(self.response)
        resp.status_code = self.status_code
        resp.headers.update(self.headers)
        return resp


TJsonObjApiResponsePayload = TypeVar('TJsonObjApiResponsePayload')


class RootJsonApiResponse(Generic[TJsonObjApiResponsePayload], EmptyJsonApiResponse):
    root: TJsonObjApiResponsePayload

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseStd(BaseModel):
            __root__: inner_type  # type: ignore
        return _ResponseStd

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        resp = jsonify(self.root)
        resp.status_code = self.status_code
        resp.headers.update(self.headers)
        return resp


class AnyJsonApiResponse(ApiResponse):
    payload: TPayloadInputUnion
    total_count: Optional[int] = None
    errors: List[Dict[str, Any]] = []

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseStd(BaseModel):
            ok: bool
            payload: Any
            errors: List[Dict[str, Any]]
            total_count: Optional[int] = None
            count: Optional[int] = None
        return _ResponseStd

    def to_flask_response(self, debugger: Optional[Debugger] = None) -> BaseResponse:
        list_props: Dict[str, Any] = {}
        if self.total_count is not None and isinstance(self.payload, (tuple, list)):
            list_props = {
                RESPONSE_PROP_COUNT: len(self.payload),
                RESPONSE_PROP_TOTAL: self.total_count,
            }

        data = {
            RESPONSE_PROP_OK: self.ok,
            RESPONSE_PROP_PAYLOAD: self.payload,
            RESPONSE_PROP_ERRORS: self.errors,
            **list_props,
            **(debugger.render_dict(self.status_code) if debugger is not None else {}),
        }

        if self.ok and len(self.errors) == 0 and MIME__MSGPCK in request.headers.get(REQUEST_HEADER__ACCEPT, MIME__JSON):
            resp = msgpackify(data)
        else:
            resp = jsonify(data)

        resp.status_code = self.status_code

        resp.headers.update(self.headers)

        return resp

    @staticmethod
    def _internal_use_response_error(many: bool, status_code: int, errors: List[Dict[str, str]]) -> 'JsonApiResponse[TJsonObjApiResponsePayload]':
        # TODO
        # exc -> 0 -> error_location
        #     str type expected (type=type_error.str)

        # pydantic.error_wrappers.ValidationError: 8 validation exc for JsonApiResponse
        #
        # ul_api_utils.exc.api_list_error.ApiValidationListError:
        # validation exc: [
        # {'error_type': 'body-validation-error', 'error_message': 'field required', 'error_location': ('id',), 'error_kind': 'value_error.missing'},
        # {'error_type': 'body-validation-error', 'error_message': 'field required', 'error_location': ('date_created',), 'error_kind': 'value_error.missing'}

        # exc can by Dict[str, str | Tuple[str]]

        if many:
            return JsonApiResponse(ok=False, total_count=0, payload=[], status_code=status_code, errors=errors)
        return JsonApiResponse(ok=False, total_count=0, payload=[], status_code=status_code, errors=errors)


class JsonApiResponse(Generic[TJsonObjApiResponsePayload], AnyJsonApiResponse):

    @classmethod
    def _internal_use__mk_schema(cls, inner_type: Optional[Type[BaseModel]]) -> Type[BaseModel]:
        class _ResponseStd(BaseModel):
            ok: bool
            payload: inner_type  # type: ignore
            errors: List[Dict[str, Any]]
            total_count: Optional[int] = None
            count: Optional[int] = None
        return _ResponseStd
