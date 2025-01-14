# SPDX-FileCopyrightText: 2022-present Artur Drogunow <artur.drogunow@zf.com>
#
# SPDX-License-Identifier: MIT

import ctypes
import typing
from typing import List

from .cnp_api import cnp_class, cnp_constants
from .config import RC

try:
    from .cnp_api import cnp_prototype
except FileNotFoundError:
    cnp_prototype = None  # type: ignore[assignment]


class Sample(typing.NamedTuple):
    timestamp: float
    value: float


class EcuTask:
    def __init__(
        self,
        asap3_handle: cnp_class.TAsap3Hdl,  # type: ignore[valid-type]
        module_handle: cnp_class.TModulHdl,
        task_info: cnp_class.TTaskInfo2,
    ) -> None:
        """The :class:`~pycanape.ecu_task.EcuTask` class is not meant to be instantiated
        by the user. :class:`~pycanape.ecu_task.EcuTask` instances are returned by
        :meth:`~pycanape.module.Module.get_ecu_tasks`.


        :param asap3_handle:
        :param module_handle:
        :param task_info:
        """
        if cnp_prototype is None:
            err_msg = (
                "CANape API not found. Add CANape API "
                "location to environment variable `PATH`."
            )
            raise FileNotFoundError(err_msg)

        self._asap3_handle = asap3_handle
        self._module_handle = module_handle
        self._task_info = task_info

    def __str__(self) -> str:
        return f"EcuTask {self.description}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def description(self) -> str:
        """Description text"""
        return self._task_info.description.decode(RC["ENCODING"])

    @property
    def task_id(self) -> int:
        """Identification number.

        The task Id is dynamically generated by CANape
        depending on internal definitions.
        """
        return self._task_info.taskId

    @property
    def task_cycle(self) -> int:
        """Cycle rate in msec.

        0 if not a cyclic task or unknown. In case of modes
        polling or cycle this parameter has no sense.
        """
        return self._task_info.taskCycle

    @property
    def event_channel(self) -> int:
        return self._task_info.eventChannel

    def daq_setup_channel(
        self, measurement_object_name: str, polling_rate: int, save_to_file: bool
    ) -> None:
        """Add a measurement object to the data acquisition channel list.

        :param measurement_object_name:
            Name of object to measure
        :param polling_rate:
            If accquisition mode is polling this specifies the polling rate.
            Reduce the original sample rate of ECU data. Example: If the sample
            rate of the ECU is 1 per 10msec, but the CANapeAPI client is set to
            receive data only every 50msec, the option 'downsampling' must be set to 5.
        :param save_to_file:
            Save this channel to measurement file. Therefore the currently
            selected Recorder will be used
        """
        cnp_prototype.Asap3SetupDataAcquisitionChnl(
            self._asap3_handle,
            self._module_handle,
            measurement_object_name.encode(RC["ENCODING"]),
            cnp_constants.TFormat.PHYSICAL_REPRESENTATION,
            self.task_id,
            polling_rate,
            save_to_file,
        )

    def daq_check_overrun(self, reset_overrun: bool = False) -> None:
        """Check if data have been lost due to FIFO overrun.

        Asap3CheckOverrun doesn't have any impact to the FIFO data. All data
        are available excluding the data record which caused the overrun.

        :param reset_overrun:
            If True reset the overrun flag in CANape
        """
        cnp_prototype.Asap3CheckOverrun(
            self._asap3_handle,
            self._module_handle,
            self.task_id,
            reset_overrun,
        )

    def daq_get_fifo_level(self) -> int:
        """Get number of samples in FIFO."""
        fifo_level = cnp_prototype.Asap3GetFifoLevel(
            self._asap3_handle,
            self._module_handle,
            self.task_id,
        )
        return fifo_level

    def daq_get_next_sample(self, channel_count: int) -> List[Sample]:
        c_time = cnp_class.TTime()
        value = ctypes.c_double()
        ptr = ctypes.pointer(ctypes.pointer(value))
        cnp_prototype.Asap3GetNextSample(
            self._asap3_handle,
            self._module_handle,
            self.task_id,
            ctypes.byref(c_time),
            ptr,
        )
        time_ms = c_time.value / 10
        return [
            Sample(time_ms, typing.cast(float, ptr.contents[i]))
            for i in range(channel_count)
        ]

    def daq_get_current_values(self, channel_count: int) -> List[Sample]:
        c_time = cnp_class.TTime()
        values = (ctypes.c_double * channel_count)()
        cnp_prototype.Asap3GetCurrentValues(
            self._asap3_handle,
            self._module_handle,
            self.task_id,
            ctypes.byref(c_time),
            values,
            channel_count,
        )
        time_ms = c_time.value / 10
        return [Sample(time_ms, values[i]) for i in range(channel_count)]
