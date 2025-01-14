"""
    QuaO Project update_job_metadata.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
import json

import requests

from ...data.response.job_response import JobResponse
from ...util.http_utils import HttpUtils
from ...util.response_utils import ResponseUtils
from ...config.logging_config import logger


def update_job_metadata(
        job_response: JobResponse,
        callback_url: str):
    """

    @param job_response: Job response
    @param callback_url: Callback url to Quao server
    """
    logger.info("Calling to backend update job metadata: {0}".format(callback_url))

    request_body = ResponseUtils.generate_response(job_response)

    try:
        response = requests.patch(
            url=callback_url,
            json=request_body,
            headers=HttpUtils.create_bearer_header(job_response.user_token),
        )

        logger.info("Calling to backend with status code: {0}".format(response.status_code))

    except Exception as exception:
        logger.error(
            "Error calling to backend with exception: {0}".format(str(exception))
        )

