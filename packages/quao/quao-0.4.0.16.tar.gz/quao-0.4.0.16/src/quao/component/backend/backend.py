"""
    QuaO Project backend.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from braket.circuits import Circuit
from qiskit import QuantumCircuit

from ..callback.update_job_metadata import update_job_metadata
from ...async_tasks.export_circuit_task import export_circuit_task
from ...component.device.device_selection import DeviceSelection
from ...config.logging_config import logger
from ...config.thread_config import circuit_exporting_pool
from ...data.device.circuit_running_option import CircuitRunningOption
from ...data.request.invocation_request import InvocationRequest
from ...data.response.authentication import Authentication
from ...data.response.job_response import JobResponse
from ...enum.invocation_step import InvocationStep
from ...enum.status.job_status import JobStatus
from ...factory.device_factory import DeviceFactory
from ...factory.provider_factory import ProviderFactory
from ...util.circuit_utils import CircuitUtils


class Backend:
    def __init__(self, request_data: InvocationRequest):
        self.sdk = request_data.sdk
        self.input = request_data.input
        self.device_id = request_data.device_id
        self.backend_information = None
        self.options = CircuitRunningOption(shots=request_data.shots,
                                            processing_unit=request_data.processing_unit)
        self.authentication = Authentication(user_token=request_data.user_token,
                                             user_identity=request_data.user_identity)
        self.server_url = request_data.device_selection_url
        self.circuit_export_url = request_data.circuit_export_url
        self.callback_dict = {
            InvocationStep.PREPARATION: request_data.preparation,
            InvocationStep.EXECUTION: request_data.execution,
            InvocationStep.ANALYSIS: request_data.analysis,
            InvocationStep.FINALIZATION: request_data.finalization
        }

    def submit_job(self, circuit_preparation_fn, post_processing_fn):
        """

        @param post_processing_fn: Post-processing function
        @param circuit_preparation_fn: Circuit-preparation function
        @return: Job result
        """

        circuit = self.__pre_execute(circuit_preparation_fn)

        self.__execute(circuit, post_processing_fn)

    def __pre_execute(self, circuit_preparation_fn):
        """

        @param circuit_preparation_fn: Circuit preparation function
        """
        circuit = self.__prepare_circuit(circuit_preparation_fn)

        self.__prepare_backend_data(circuit)

        self.__export_circuit(circuit)

        return circuit

    def __execute(self, circuit, post_processing_fn):
        """

        @param circuit: Circuit was run
        @param post_processing_fn: Post-processing function
        @return: Job response
        """

        logger.debug('Execute job!')

        try:
            if self.backend_information is None:
                raise Exception("Backend is not found")

            device_name = self.backend_information.device_name
            provider_tag = self.backend_information.provider_tag
            backend_authentication = self.backend_information.authentication

            logger.debug('Execute job with provider tag: {0}'.format(provider_tag))
            provider = ProviderFactory().create_provider(provider_tag, backend_authentication)

            logger.debug('Execute job with device name: {0}'.format(device_name))
            device = DeviceFactory().create_device(provider,
                                                   device_name,
                                                   backend_authentication,
                                                   self.sdk,
                                                   self.options.processing_unit)

        except Exception as exception:
            job_response = JobResponse(job_status=JobStatus.ERROR.value,
                                       authentication=self.authentication,
                                       job_result={"error": str(exception)})
            update_job_metadata(
                job_response=job_response,
                callback_url=self.callback_dict.get(InvocationStep.EXECUTION).on_error)

            return

        device.run_circuit(circuit=circuit,
                           post_processing_fn=post_processing_fn,
                           options=self.options,
                           callback_dict=self.callback_dict,
                           authentication=self.authentication)

    def __prepare_circuit(self, circuit_preparation_fn):
        """

        @param circuit_preparation_fn: Circuit preparation function
        @return: circuit
        """
        circuit = None

        job_response = JobResponse(invocation_step=InvocationStep.PREPARATION,
                                   authentication=self.authentication)
        update_job_metadata(
            job_response=job_response,
            callback_url=self.callback_dict.get(InvocationStep.PREPARATION).on_start)

        try:
            circuit = circuit_preparation_fn(self.input)

            if circuit is None or not isinstance(circuit, (QuantumCircuit, Circuit)):
                raise Exception("Invalid circuit")

            job_response.reset_job_status(JobStatus.DONE.value)
            update_job_metadata(
                job_response=job_response,
                callback_url=self.callback_dict.get(InvocationStep.PREPARATION).on_done)

        except Exception as exception:
            job_response.reset_job_status(JobStatus.ERROR.value)
            job_response.job_result = {"error": str(exception)}

            update_job_metadata(
                job_response=job_response,
                callback_url=self.callback_dict.get(InvocationStep.PREPARATION).on_error)

        return circuit

    def __prepare_backend_data(self, circuit):
        """

        @param circuit: Circuit was run
        """

        required_qubit_amount = CircuitUtils.get_qubit_amount(circuit)

        device_selection = DeviceSelection(required_qubit_amount,
                                           self.device_id,
                                           self.authentication.user_token,
                                           self.server_url)

        self.backend_information = device_selection.select()

    def __export_circuit(self, circuit):
        """

        @param circuit: Circuit was exported
        """

        logger.debug("Preparing configuration for circuit export")

        circuit_config_map = {
            'circuit': circuit,
            'circuit_export_url': self.circuit_export_url
        }

        backend_config_map = {
            'provider_tag': self.backend_information.provider_tag,
            'device_name': self.backend_information.device_name,
            'token': self.authentication.user_token
        }

        logger.debug("Configuration of circuit export has been already prepared")

        export_circuit_task(circuit_config_map=circuit_config_map,
                            backend_config_map=backend_config_map,
                            user_token=self.authentication.user_token)

