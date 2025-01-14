"""
    QuaO Project circuit_running_option.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from ...enum.processing_unit import ProcessingUnit


class CircuitRunningOption:
    def __init__(self,
                 shots: int = 1024,
                 processing_unit: ProcessingUnit = ProcessingUnit.CPU):
        self.shots = shots
        self.processing_unit = processing_unit
