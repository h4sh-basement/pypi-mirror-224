# ----------------------------------------------------------------------------
# Description    : S4g SPI module QCoDeS interface
# Git repository : https://gitlab.com/qblox/packages/software/qblox_instruments.git
# Copyright (C) Qblox BV (2021)
# ----------------------------------------------------------------------------

from qcodes.instrument.channel import InstrumentChannel
from qcodes import validators

from functools import partial
from typing import List, Optional

from qblox_instruments.native.spi_rack_modules import S4gModule as S4gModuleNative
from qblox_instruments.native.spi_rack_modules import S4gDacChannel as S4gDacChannelNative


class S4gModule(S4gModuleNative, InstrumentChannel):
    """
    `QCoDeS <https://qcodes.github.io/Qcodes/>`_ style instrument channel
    driver for the S4g SPI module.
    """

    NUMBER_OF_DACS = 4  # Set by hardware constraints

    def __init__(
        self,
        parent,
        name: str,
        address: int,
        reset_currents: bool = False,
        dac_names: Optional[List[str]] = None,
        is_dummy: bool = False,
    ):
        """
        Instantiates the driver object. This is the object that should be
        instantiated by the :func:`~qblox_instruments.SpiRack.add_spi_module`
        function.

        Parameters
        ----------
        parent
            Reference to the :class:`~qblox_instruments.SpiRack` parent
            object. This is handled by the
            :func:`~qblox_instruments.SpiRack.add_spi_module` function.
        name : str
            Name given to the InstrumentChannel.
        address : int
            Module number set on the hardware.
        reset_currents : bool
            If True, then reset all currents to zero and change the span to
            `range_max_bi`.
        dac_names : Optional[List[str]]
            List of all the names to use for the dac channels. If no list is
            given or is None, the default name "dac{i}" is used for the i-th dac channel.
        is_dummy : bool
            If true, do not connect to physical hardware, but use a dummy module.

        Returns
        ----------

        Raises
        ----------
        ValueError
            Length of the dac names list does not match the number of dacs.
        """
        super().__init__(parent,
                         name,
                         address,
                         reset_currents,
                         dac_names,
                         is_dummy)
        InstrumentChannel.__init__(self, parent, name)

        for dac, old_channel in enumerate(self._channels):
            new_channel = S4gDacChannel(self, old_channel._chan_name, dac)
            self._channels[dac] = new_channel
            self.add_submodule(old_channel._chan_name, new_channel)

    def set_dacs_zero(self) -> None:
        """
        Sets all currents of all outputs to 0.

        Returns
        ----------
        """
        for ch in self._channels:
            ch.current(0)


class S4gDacChannel(S4gDacChannelNative, InstrumentChannel):
    """
    `QCoDeS <https://qcodes.github.io/Qcodes/>`_ style instrument channel
    driver for the dac channels of the S4g module. This class is used by
    the :class:`~qblox_instruments.qcodes_drivers.spi_rack_modules.S4gModule`
    to define the individual dac channels and should not be used directly.
    """

    def __init__(self, parent: S4gModule, name: str, dac: int):
        """
        Constructor for the dac channel instrument channel.

        Parameters
        ----------
        parent : S4gModule
            Reference to the parent
            :class:`~qblox_instruments.qcodes_drivers.spi_rack_modules.S4gModule`
        name : str
            Name for the instrument channel
        dac : int
            Number of the dac that this channel corresponds to

        Returns
        ----------

        Raises
        ----------
        """
        super().__init__(parent, name)
        InstrumentChannel.__init__(self, parent, name)

        self.add_parameter(
            "current",
            get_cmd=partial(self._get_current, dac),
            set_cmd=partial(self._set_current, dac),
            unit="A",
            vals=validators.Numbers(min_value=-40e-3, max_value=40e-3),
            docstring="Sets the output current of the dac channel. Depending "
            "on the value of ramping_enabled, the output value is either "
            "achieved through slowly ramping, or instantaneously set.",
        )
        self.add_parameter(
            "span",
            val_mapping={
                "range_max_uni": 0,
                "range_max_bi": 2,
                "range_min_bi": 4
            },
            get_cmd=partial(self._get_span, dac),
            set_cmd=partial(self._set_span, dac),
            docstring="Sets the max range of the DACs. Possible values:"
            "\t'range_max_uni':\t0 - 40 mA,"
            "\t'range_max_bi':\t-40 - 40 mA,"
            "\t'range_min_bi':\t-20 - 20 mA.",
        )

        self.add_parameter(
            "ramp_rate",
            get_cmd=partial(getattr, self, "_ramp_rate"),
            set_cmd=partial(setattr, self, "_ramp_rate"),
            unit="A/s",
            initial_value=1e-3,  # 1 mA/s
            docstring="Limits the rate at which currents can be changed. The "
            "size of of steps is still limited by `ramp_max_step`.",
        )
        self.add_parameter(
            "ramp_max_step",
            get_cmd=partial(getattr, self, "_ramp_max_step"),
            set_cmd=partial(setattr, self, "_ramp_max_step"),
            unit="A",
            initial_value=0.5e-3,
            docstring="Sets the maximum step size for current ramping. The "
            "rate at which it ramps is set by `ramp_rate`.",
        )
        self.add_parameter(
            "ramping_enabled",
            get_cmd=partial(getattr, self, "_ramping_enabled"),
            set_cmd=partial(setattr, self, "_ramping_enabled"),
            initial_value=False,
            vals=validators.Bool(),
            docstring="Turns ramping on or off. Toggling `ramping_enabled` "
            "changed the behavior of the setter for the `current` parameter. "
            "If enabled, ramping is done at a rate set by `ramp_rate` and "
            "in steps specified by `ramp_max_step`.",
        )
        self.add_parameter(
            "is_ramping",
            get_cmd=partial(getattr, self, "_is_ramping"),
            set_cmd=False,
            docstring="Returns whether the dac is currently in the process "
            "of ramping.",
        )
        self.add_parameter(
            "stepsize",
            unit="A",
            set_cmd=False,
            get_cmd=partial(self._api.get_stepsize, dac),
            docstring="Returns the smallest current step allowed by the dac "
            "for the current settings.",
        )
        self.add_parameter(
            "dac_channel",
            set_cmd=False,
            get_cmd=lambda: dac,
            docstring="Returns the dac number of this channel.",
        )
