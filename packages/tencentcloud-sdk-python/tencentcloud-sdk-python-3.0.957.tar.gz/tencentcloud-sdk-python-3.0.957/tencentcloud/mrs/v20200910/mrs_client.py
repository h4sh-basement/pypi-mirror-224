# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.mrs.v20200910 import models


class MrsClient(AbstractClient):
    _apiVersion = '2020-09-10'
    _endpoint = 'mrs.tencentcloudapi.com'
    _service = 'mrs'


    def ImageToClass(self, request):
        """图片分类

        :param request: Request instance for ImageToClass.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageToClassRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageToClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageToClass", params, headers=headers)
            response = json.loads(body)
            model = models.ImageToClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageToObject(self, request):
        """图片转结构化对象

        :param request: Request instance for ImageToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageToObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageToObject", params, headers=headers)
            response = json.loads(body)
            model = models.ImageToObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToClass(self, request):
        """文本分类

        :param request: Request instance for TextToClass.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TextToClassRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TextToClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToClass", params, headers=headers)
            response = json.loads(body)
            model = models.TextToClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToObject(self, request):
        """文本转结构化对象。

        适用场景：经过腾讯医疗专用 OCR 从图片识别之后的文本，可以调用此接口。通过其它 OCR 识别的文本可能不适配。医院的 XML 格式文本也不适配，XML 文件需要经过特殊转换才能直接调用此接口。单次调用传入的文本不宜超过 2000 字。

        :param request: Request instance for TextToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TextToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TextToObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToObject", params, headers=headers)
            response = json.loads(body)
            model = models.TextToObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))