import inspect
import logging
import re
from typing import Any, Dict
from urllib.parse import urlparse

from pydantic_client.clients.abstract_client import AbstractClient
from pydantic_client.schema.http_request import HttpRequest
from pydantic_client.schema.method_info import MethodInfo

logger = logging.getLogger(__name__)


class Proxy:
    querystring_pattern = re.compile(r"\{(.*?)\}")

    def __init__(self, instance: AbstractClient, method_info: MethodInfo):
        self.instance = instance
        self.method_info = method_info

    def _apply_args(self, *args, **kwargs) -> Dict[str, Any]:
        f = inspect.getcallargs(
            self.method_info.func, self.instance, *args, **kwargs,
        )
        f.pop("self", None)
        return f

    def _get_url(self, args) -> str:
        keys = self.querystring_pattern.findall(self.method_info.url)
        query_args = {arg: val for arg, val in args.items() if arg in keys and val}
        url = self.method_info.url.format(**query_args)

        url_result = urlparse(url)
        if "{" in url_result.path:
            logger.warning(f"Not formatted args in url path: {url}")

        querystring = "&".join(
            f"{k}={v}" for k, v in url_result.query if "{" not in v
        )
        return url_result.path + "?" + querystring if querystring else url_result.path

    def get_request(self, *args, **kwargs):
        func_args: Dict[str, Any] = self._apply_args(*args, **kwargs)

        url: str = self._get_url(func_args)
        if self.method_info.form_body:
            data, json = func_args, {}
        else:
            data, json = {}, func_args

        return HttpRequest(
            url=url,
            data=data,
            json_body=json,
            method=self.method_info.http_method
        )


class ClientProxy(Proxy):

    def __call__(self, *args, **kwargs):
        request = self.get_request(*args, **kwargs)
        raw_response = self.instance.do_request(request)
        if self.method_info.response_type:
            return self.method_info.response_type(**raw_response)
        return raw_response


class AsyncClientProxy(Proxy):

    async def __call__(self, *args, **kwargs):
        request = self.get_request(*args, **kwargs)
        raw_response = await self.instance.do_request(request)
        if self.method_info.response_type:
            return self.method_info.response_type(**raw_response)
        return raw_response
