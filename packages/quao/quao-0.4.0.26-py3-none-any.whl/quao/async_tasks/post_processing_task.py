"""
    QuaO Project post_processing_task.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from ..component.callback.update_job_metadata import update_job_metadata
from ..config.logging_config import logger
from ..data.promise.post_processing_promise import PostProcessingPromise
from ..data.response.job_response import JobResponse
from ..enum.media_type import MediaType
from ..enum.status.job_status import JobStatus
from ..enum.status.status_code import StatusCode
from ..util.json_parser_utils import JsonParserUtils


def post_processing_task(post_processing_fn, promise: PostProcessingPromise):
    """
    Execute post_processing and send to backend

    @param post_processing_fn: post_processing function
    @param promise: promise arg
    """

    job_response = JobResponse(
        authentication=promise.authentication,
        status_code=StatusCode.DONE)

    # Start post_processing
    update_job_metadata(job_response=job_response,
                        callback_url=promise.callback_url.on_start)

    try:
        job_response.content_type = MediaType.APPLICATION_JSON

        logger.info("Execute post_processing ...")
        job_result_post_processing = post_processing_fn(promise.job_result)
        logger.info("Execute post_processing finishing!")

        logger.debug("Parsing job result....")
        job_result_dictionary = JsonParserUtils.parse(job_result_post_processing)
        logger.debug("Parsing job result completed!")

        job_response.job_result = job_result_dictionary

        # Call backend to update job done
        update_job_metadata(job_response=job_response,
                            callback_url=promise.callback_url.on_done)

    except Exception as exception:
        job_response.job_result = {
            "error": "Error when execute post_processing(): ",
            "exception": str(exception),
        }
        job_response.status_code = JobStatus.ERROR

        # Call BE to update job error
        update_job_metadata(
            job_response=job_response,
            callback_url=promise.callback_url.on_error
        )
