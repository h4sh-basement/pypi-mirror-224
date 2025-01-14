""" Qblox Cluster QCM driver."""

import json

from qblox_instruments.qcodes_drivers.cluster import Cluster as QbloxCluster
from qblox_instruments.qcodes_drivers.qcm_qrm import QcmQrm as QbloxQrmQcm
from qibo.config import log

from qibolab.instruments.abstract import Instrument
from qibolab.instruments.qblox.port import (
    ClusterBB_OutputPort,
    ClusterBB_OutputPort_Settings,
)
from qibolab.instruments.qblox.q1asm import (
    Block,
    Register,
    convert_phase,
    loop_block,
    wait_block,
)
from qibolab.instruments.qblox.sequencer import Sequencer, WaveformsBuffer
from qibolab.instruments.qblox.sweeper import QbloxSweeper, QbloxSweeperType
from qibolab.pulses import Pulse, PulseSequence, PulseType
from qibolab.sweeper import Parameter, Sweeper, SweeperType


class ClusterQCM_BB_Settings:
    def __init__(self, ports=None):
        if not ports:
            ports: dict = {
                "o1": ClusterBB_OutputPort_Settings(),
                "o2": ClusterBB_OutputPort_Settings(),
                "o3": ClusterBB_OutputPort_Settings(),
                "o4": ClusterBB_OutputPort_Settings(),
            }
        self.ports = ports


class ClusterQCM_BB(Instrument):
    """Qblox Cluster Qubit Control Module Baseband driver.

    Qubit Control Module (QCM) is an arbitratry wave generator with two DACs connected to
    four output ports. It can sinthesise either four independent real signals or two
    complex signals, using ports 0 and 2 to output the i(in-phase) component and
    ports 1 and 3 the q(quadrature) component. The sampling rate of its DAC is 1 GSPS.
    https://www.qblox.com/cluster

    The class aims to simplify the configuration of the instrument, exposing only
    those parameters most frequencly used and hiding other more complex components.

    A reference to the underlying `qblox_instruments.qcodes_drivers.qcm_qrm.QRM_QCM`
    object is provided via the attribute `device`, allowing the advanced user to gain
    access to the features that are not exposed directly by the class.

    In order to accelerate the execution, the instrument settings are cached, so that
    the communication with the instrument only happens when the parameters change.
    This caching is done with the method `_set_device_parameter(target, *parameters, value)`.

    .. code-block:: text

            ports:
                o1:
                    channel                      : L4-1
                    gain                         : 0.2 # -1.0<=v<=1.0
                    offset                       : 0   # -2.5<=v<=2.5
                o2:
                    channel                      : L4-2
                    gain                         : 0.2 # -1.0<=v<=1.0
                    offset                       : 0   # -2.5<=v<=2.5
                o3:
                    channel                      : L4-3
                    gain                         : 0.2 # -1.0<=v<=1.0
                    offset                       : 0   # -2.5<=v<=2.5
                o4:
                    channel                      : L4-4
                    gain                         : 0.2 # -1.0<=v<=1.0
                    offset                       : 0   # -2.5<=v<=2.5

    Attributes:
        name (str): A unique name given to the instrument.
        address (str): IP_address:module_number (the IP address of the cluster and
            the module number)
        device (QbloxQrmQcm): A reference to the underlying
            `qblox_instruments.qcodes_drivers.qcm_qrm.QcmQrm` object. It can be used to access other
            features not directly exposed by this wrapper.
            https://qblox-qblox-instruments.readthedocs-hosted.com/en/master/api_reference/qcm_qrm.html
        ports = A dictionary giving access to the output ports objects.

            - ports['o1']
            - ports['o2']
            - ports['o3']
            - ports['o4']

            - ports['oX'].channel (int | str): the id of the refrigerator channel the port is connected to.
            - ports['oX'].gain (float): (mapped to qrm.sequencers[0].gain_awg_path0 and qrm.sequencers[0].gain_awg_path1)
                Sets the gain on both paths of the output port.
            - ports['oX'].offset (float): (mapped to qrm.outX_offset)
                Sets the offset on the output port.
            - ports['oX'].hardware_mod_en (bool): (mapped to qrm.sequencers[0].mod_en_awg) Enables pulse
                modulation in hardware. When set to False, pulse modulation is done at the host computer
                and a modulated pulse waveform should be uploaded to the instrument. When set to True,
                the envelope of the pulse should be uploaded to the instrument and it modulates it in
                real time by its FPGA using the sequencer nco (numerically controlled oscillator).
            - ports['oX'].nco_freq (int): (mapped to qrm.sequencers[0].nco_freq)        # TODO mapped, but not configurable from the runcard
            - ports['oX'].nco_phase_offs = (mapped to qrm.sequencers[0].nco_phase_offs) # TODO mapped, but not configurable from the runcard

                - Sequencer 0 is always the first sequencer used to synthesise pulses on port o1.
                - Sequencer 1 is always the first sequencer used to synthesise pulses on port o2.
                - Sequencer 2 is always the first sequencer used to synthesise pulses on port o3.
                - Sequencer 3 is always the first sequencer used to synthesise pulses on port o4.
                - Sequencer 4 to 6 are used as needed to sinthesise simultaneous pulses on the same channel
                  or when the memory of the default sequencers rans out.
    """

    DEFAULT_SEQUENCERS = {"o1": 0, "o2": 1, "o3": 2, "o4": 3}
    SAMPLING_RATE: int = 1e9  # 1 GSPS
    FREQUENCY_LIMIT = 500e6

    property_wrapper = lambda parent, *parameter: property(
        lambda self: parent.device.get(parameter[0]),
        lambda self, x: parent._set_device_parameter(parent.device, *parameter, value=x),
    )
    sequencer_property_wrapper = lambda parent, sequencer, *parameter: property(
        lambda self: parent.device.sequencers[sequencer].get(parameter[0]),
        lambda self, x: parent._set_device_parameter(parent.device.sequencers[sequencer], *parameter, value=x),
    )

    def __init__(self, name: str, address: str, settings: dict):
        """Initialises the instance.

        All class attributes are defined and initialised.
        """
        super().__init__(name, address)
        self.settings: ClusterQCM_BB_Settings = settings
        self.device: QbloxQrmQcm = None
        self.ports: dict = {}
        for n in range(4):
            port = "o" + str(n + 1)
            self.ports[port] = ClusterBB_OutputPort(
                module=self, sequencer_number=self.DEFAULT_SEQUENCERS[port], number=n + 1
            )
        self.channels: list = []

        self._debug_folder: str = ""
        self._cluster: QbloxCluster = None
        self._output_ports_keys = ["o1", "o2", "o3", "o4"]
        self._sequencers: dict[Sequencer] = {"o1": [], "o2": [], "o3": [], "o4": []}
        self._port_channel_map: dict = {}
        self._channel_port_map: dict = {}
        self._device_parameters = {}
        self._device_num_output_ports = 2
        self._device_num_sequencers: int
        self._free_sequencers_numbers: list[int] = []
        self._used_sequencers_numbers: list[int] = []
        self._unused_sequencers_numbers: list[int] = []

    def connect(self, cluster: QbloxCluster):
        """Connects to the instrument using the instrument settings in the runcard.

        Once connected, it creates port classes with properties mapped to various instrument
        parameters, and initialises the the underlying device parameters.
        """
        if not self.is_connected:
            if cluster:
                # save a reference to the underlying object
                self.device = cluster.modules[int(self.address.split(":")[1]) - 1]
                # TODO: test connection with the module before continuing

                # save reference to cluster
                self._cluster = cluster
                self.is_connected = True

                # once connected, initialise the parameters of the device to the default values
                self._set_device_parameter(self.device, "out0_offset", value=0)  # Default after reboot = 0
                self._set_device_parameter(self.device, "out1_offset", value=0)  # Default after reboot = 0
                self._set_device_parameter(self.device, "out2_offset", value=0)  # Default after reboot = 0
                self._set_device_parameter(self.device, "out3_offset", value=0)  # Default after reboot = 0

                # initialise the parameters of the default sequencers to the default values,
                # the rest of the sequencers are not configured here, but will be configured
                # with the same parameters as the default in process_pulse_sequence()
                for target in [
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o1"]],
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o2"]],
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o3"]],
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o4"]],
                ]:
                    self._set_device_parameter(
                        target, "cont_mode_en_awg_path0", "cont_mode_en_awg_path1", value=False
                    )  # Default after reboot = False
                    self._set_device_parameter(
                        target, "cont_mode_waveform_idx_awg_path0", "cont_mode_waveform_idx_awg_path1", value=0
                    )  # Default after reboot = 0
                    self._set_device_parameter(target, "marker_ovr_en", value=True)  # Default after reboot = False
                    self._set_device_parameter(target, "marker_ovr_value", value=15)  # Default after reboot = 0
                    self._set_device_parameter(target, "mixer_corr_gain_ratio", value=1)
                    self._set_device_parameter(target, "mixer_corr_phase_offset_degree", value=0)
                    self._set_device_parameter(target, "offset_awg_path0", value=0)
                    self._set_device_parameter(target, "offset_awg_path1", value=0)
                    self._set_device_parameter(target, "sync_en", value=False)  # Default after reboot = False
                    self._set_device_parameter(target, "upsample_rate_awg_path0", "upsample_rate_awg_path1", value=0)

                for target in [
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o1"]],
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o2"]],
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o3"]],
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o4"]],
                ]:
                    self._set_device_parameter(
                        target, "channel_map_path0_out0_en", value=False
                    )  # Default after reboot = True
                    self._set_device_parameter(
                        target, "channel_map_path1_out1_en", value=False
                    )  # Default after reboot = True
                    self._set_device_parameter(
                        target, "channel_map_path0_out2_en", value=False
                    )  # Default after reboot = True
                    self._set_device_parameter(
                        target, "channel_map_path1_out3_en", value=False
                    )  # Default after reboot = True

                self._set_device_parameter(
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o1"]],
                    "channel_map_path0_out0_en",
                    value=True,
                )
                self._set_device_parameter(
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o2"]],
                    "channel_map_path1_out1_en",
                    value=True,
                )
                self._set_device_parameter(
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o3"]],
                    "channel_map_path0_out2_en",
                    value=True,
                )
                self._set_device_parameter(
                    self.device.sequencers[self.DEFAULT_SEQUENCERS["o4"]],
                    "channel_map_path1_out3_en",
                    value=True,
                )

                # on initialisation, disconnect all other sequencers from the ports
                self._device_num_sequencers = len(self.device.sequencers)
                for sequencer in range(4, self._device_num_sequencers):
                    target = self.device.sequencers[sequencer]
                    self._set_device_parameter(target, "channel_map_path0_out0_en", value=False)
                    self._set_device_parameter(target, "channel_map_path1_out1_en", value=False)
                    self._set_device_parameter(target, "channel_map_path0_out2_en", value=False)
                    self._set_device_parameter(target, "channel_map_path1_out3_en", value=False)

    def _set_device_parameter(self, target, *parameters, value):
        """Sets a parameter of the instrument, if it changed from the last stored in the cache.

        Args:
            target = an instance of qblox_instruments.qcodes_drivers.qcm_qrm.QcmQrm or
                                    qblox_instruments.qcodes_drivers.sequencer.Sequencer
            *parameters (list): A list of parameters to be cached and set.
            value = The value to set the paramters.
        Raises:
            Exception = If attempting to set a parameter without a connection to the instrument.
        """
        if self.is_connected:
            key = target.name + "." + parameters[0]
            if not key in self._device_parameters:
                for parameter in parameters:
                    if not hasattr(target, parameter):
                        raise Exception(f"The instrument {self.name} does not have parameters {parameter}")
                    target.set(parameter, value)
                self._device_parameters[key] = value
            elif self._device_parameters[key] != value:
                for parameter in parameters:
                    target.set(parameter, value)
                self._device_parameters[key] = value
        else:
            raise Exception("There is no connection to the instrument {self.name}")

    def _erase_device_parameters_cache(self):
        """Erases the cache of instrument parameters."""
        self._device_parameters = {}

    def setup(self):
        """Configures the instrument with the settings of the runcard.

        A connection to the instrument needs to be established beforehand.
        Args:
            **kwargs: dict = A dictionary of settings loaded from the runcard:

                - oX: ['o1', 'o2', 'o3', 'o4']
                - kwargs['ports']['oX']['channel'] (int | str): the id of the refrigerator channel the port is connected to.
                - kwargs['ports'][oX]['gain'] (float): [0.0 - 1.0 unitless] gain applied prior to up-conversion. Qblox recommends to keep
                  `pulse_amplitude * gain` below 0.3 to ensure the mixers are working in their linear regime, if necessary, lowering the attenuation
                  applied at the output.
                - kwargs['ports'][oX]['offset'] (float): [-2.5 - 2.5 V] offset in volts applied to the output port.
                - kwargs['ports'][oX]['hardware_mod_en'] (bool): enables Hardware Modulation. In this mode, pulses are modulated to the intermediate frequency
                  using the numerically controlled oscillator within the fpga. It only requires the upload of the pulse envelope waveform.

        Raises:
            Exception = If attempting to set a parameter without a connection to the instrument.
        """
        settings: ClusterQCM_BB_Settings = self.settings
        if self.is_connected:
            # Load settings
            for port in ["o1", "o2", "o3", "o4"]:
                if port in settings.ports:
                    port_settings: ClusterBB_OutputPort_Settings = settings.ports[port]
                    self.ports[port].channel = port_settings.channel
                    self._port_channel_map[port] = self.ports[port].channel
                    self.ports[port].gain = port_settings.gain
                    self.ports[port].offset = port_settings.offset
                    self.ports[port].hardware_mod_en = port_settings.hardware_mod_en
                    self.ports[port].qubit = port_settings.qubit
                    self.ports[port].nco_freq = 0
                    self.ports[port].nco_phase_offs = 0
                else:
                    if port in self.ports:
                        self.ports[port].channel = None
                        self.ports[port].gain = 0
                        self.ports[port].offset = 0
                        self.ports[port].hardware_mod_en = False
                        self.ports[port].qubit = None
                        self.ports[port].nco_freq = 0
                        self.ports[port].nco_phase_offs = 0
                        self.ports.pop(port)
                        self._output_ports_keys.remove(port)
                        self._sequencers.pop(port)

            self._channel_port_map = {v: k for k, v in self._port_channel_map.items()}
            self.channels = list(self._channel_port_map.keys())
        else:
            raise Exception("The instrument cannot be set up, there is no connection")

    def _get_next_sequencer(self, port, frequency, qubits: dict, qubit: None):
        """Retrieves and configures the next avaliable sequencer.

        The parameters of the new sequencer are copied from those of the default sequencer, except for the
        intermediate frequency and classification parameters.
        Args:
            port (str):
            frequency ():
            qubit ():
        Raises:
            Exception = If attempting to set a parameter without a connection to the instrument.
        """

        # select a new sequencer and configure it as required
        next_sequencer_number = self._free_sequencers_numbers.pop(0)
        if next_sequencer_number != self.DEFAULT_SEQUENCERS[port]:
            for parameter in self.device.sequencers[self.DEFAULT_SEQUENCERS[port]].parameters:
                # exclude read-only parameter `sequence`
                if not parameter in ["sequence"]:
                    value = self.device.sequencers[self.DEFAULT_SEQUENCERS[port]].get(param_name=parameter)
                    if value:
                        target = self.device.sequencers[next_sequencer_number]
                        self._set_device_parameter(target, parameter, value=value)

        # if hardware modulation is enabled configure nco_frequency
        if self.ports[port].hardware_mod_en:
            self._set_device_parameter(
                self.device.sequencers[next_sequencer_number],
                "nco_freq",
                value=frequency,  # Assumes all pulses in non_overlapping_pulses set
                # have the same frequency. Non-overlapping pulses of different frequencies on the same
                # qubit channel with hardware_demod_en would lead to wrong results.
                # TODO: Throw error in that event or implement for non_overlapping_same_frequency_pulses
                #       Even better, set the frequency before each pulse is played (would work with hardware modulation only)
            )

            # set sequencer port offset to the runcard value
            # self._set_device_parameter(
            #     self.device.sequencers[next_sequencer_number],
            #     "out0_offset", #How to select device parameter offset??
            #     value=qubits[qubit].sweetspot,
            # )

            self.ports[port].offset = qubits[qubit].sweetspot

        # create sequencer wrapper
        sequencer = Sequencer(next_sequencer_number)
        sequencer.qubit = qubit
        return sequencer

    def get_if(self, pulse):
        """Returns the intermediate frequency needed to synthesise a pulse based on the port lo frequency."""

        _rf = pulse.frequency
        _lo = 0  # QCMs do not have local oscillator
        _if = _rf - _lo
        if abs(_if) > self.FREQUENCY_LIMIT:
            raise RuntimeError(
                f"""
            Pulse frequency {_rf:_} cannot be synthesised, it exceeds the maximum frequency of {self.FREQUENCY_LIMIT:_}"""
            )
        return _if

    def process_pulse_sequence(
        self,
        qubits: dict,
        instrument_pulses: PulseSequence,
        navgs: int,
        nshots: int,
        repetition_duration: int,
        sweepers=None,
    ):
        """Processes a list of pulses, generating the waveforms and sequence program required by
        the instrument to synthesise them.

        The output of the process is a list of sequencers used for each port, configured with the information
        required to play the sequence.
        The following features are supported:

        - overlapping pulses
        - hardware modulation
        - software modulation, with support for arbitrary pulses
        - real-time sweepers of

            - pulse frequency (requires hardware modulation)
            - pulse relative phase (requires hardware modulation)
            - pulse amplitude
            - pulse start
            - pulse duration
            - port gain
            - port offset

        - sequencer memory optimisation (waveforms cache)
        - extended waveform memory with the use of multiple sequencers
        - pulses of up to 8192 pairs of i, q samples
        - intrument parameters cache

        Args:
            instrument_pulses (PulseSequence): A collection of Pulse objects to be played by the instrument.
            navgs (int): The number of times the sequence of pulses should be executed averaging the results.
            nshots (int): The number of times the sequence of pulses should be executed without averaging.
            repetition_duration (int): The total duration of the pulse sequence execution plus the reset/relaxation time.
            sweepers (list(Sweeper)): A list of Sweeper objects to be implemented.
        """
        if sweepers is None:
            sweepers = []
        sequencer: Sequencer
        sweeper: Sweeper

        self._free_sequencers_numbers = list(range(len(self.ports), 6))

        # process the pulses for every port
        for port in self.ports:
            # split the collection of instruments pulses by ports
            port_pulses: PulseSequence = instrument_pulses.get_channel_pulses(self._port_channel_map[port])

            # initialise the list of sequencers required by the port
            self._sequencers[port] = []

            # initialise the list of free sequencer numbers to include the default for each port {'o1': 0, 'o2': 1, 'o3': 2, 'o4': 3}
            self._free_sequencers_numbers = [self.DEFAULT_SEQUENCERS[port]] + self._free_sequencers_numbers

            if not port_pulses.is_empty:
                # split the collection of port pulses in non overlapping pulses
                non_overlapping_pulses: PulseSequence
                for non_overlapping_pulses in port_pulses.separate_overlapping_pulses():
                    # TODO: for non_overlapping_same_frequency_pulses in non_overlapping_pulses.separate_different_frequency_pulses():

                    # each set of not overlapping pulses will be played by a separate sequencer
                    # check sequencer availability
                    if len(self._free_sequencers_numbers) == 0:
                        raise Exception(
                            f"The number of sequencers requried to play the sequence exceeds the number available {self._device_num_sequencers}."
                        )
                    # get next sequencer
                    sequencer = self._get_next_sequencer(
                        port=port,
                        frequency=self.get_if(non_overlapping_pulses[0]),
                        qubits=qubits,
                        qubit=non_overlapping_pulses[0].qubit,
                    )
                    # add the sequencer to the list of sequencers required by the port
                    self._sequencers[port].append(sequencer)

                    # make a temporary copy of the pulses to be processed
                    pulses_to_be_processed = non_overlapping_pulses.shallow_copy()
                    while not pulses_to_be_processed.is_empty:
                        pulse: Pulse = pulses_to_be_processed[0]
                        # attempt to save the waveforms to the sequencer waveforms buffer
                        try:
                            sequencer.waveforms_buffer.add_waveforms(pulse, self.ports[port].hardware_mod_en, sweepers)
                            sequencer.pulses.add(pulse)
                            pulses_to_be_processed.remove(pulse)

                        # if there is not enough memory in the current sequencer, use another one
                        except WaveformsBuffer.NotEnoughMemory:
                            if len(pulse.waveform_i) + len(pulse.waveform_q) > WaveformsBuffer.SIZE:
                                raise NotImplementedError(
                                    f"Pulses with waveforms longer than the memory of a sequencer ({WaveformsBuffer.SIZE // 2}) are not supported."
                                )
                            if len(self._free_sequencers_numbers) == 0:
                                raise Exception(
                                    f"The number of sequencers requried to play the sequence exceeds the number available {self._device_num_sequencers}."
                                )
                            # get next sequencer
                            sequencer = self._get_next_sequencer(
                                port=port,
                                frequency=self.get_if(non_overlapping_pulses[0]),
                                qubits=qubits,
                                qubit=non_overlapping_pulses[0].qubit,
                            )
                            # add the sequencer to the list of sequencers required by the port
                            self._sequencers[port].append(sequencer)
            else:
                sequencer = self._get_next_sequencer(
                    port=port, frequency=0, qubits=qubits, qubit=self.ports[port].qubit
                )
                # add the sequencer to the list of sequencers required by the port
                self._sequencers[port].append(sequencer)

        # update the lists of used and unused sequencers that will be needed later on
        self._used_sequencers_numbers = []
        for port in self._output_ports_keys:
            for sequencer in self._sequencers[port]:
                self._used_sequencers_numbers.append(sequencer.number)
        self._unused_sequencers_numbers = []
        for n in range(self._device_num_sequencers):
            if not n in self._used_sequencers_numbers:
                self._unused_sequencers_numbers.append(n)

        # generate and store the Waveforms dictionary, the Acquisitions dictionary, the Weights and the Program
        for port in self._output_ports_keys:
            for sequencer in self._sequencers[port]:
                pulses = sequencer.pulses
                program = sequencer.program

                ## pre-process sweepers ##
                # TODO: move qibolab sweepers preprocessing to qblox controller

                # attach a sweeper attribute to the pulse so that it is easily accesible by the code that generates
                # the pseudo-assembly program
                pulse = None
                for pulse in pulses:
                    pulse.sweeper = None

                pulse_sweeper_parameters = [
                    Parameter.frequency,
                    Parameter.amplitude,
                    Parameter.duration,
                    Parameter.relative_phase,
                    Parameter.start,
                ]

                for sweeper in sweepers:
                    if sweeper.parameter in pulse_sweeper_parameters:
                        # check if this sequencer takes an active role in the sweep
                        if sweeper.pulses and set(sequencer.pulses) & set(sweeper.pulses):
                            # plays an active role
                            reference_value = None
                            if sweeper.parameter == Parameter.frequency:
                                if sequencer.pulses:
                                    reference_value = self.get_if(
                                        sequencer.pulses[0]
                                    )  # uses the frequency of the first pulse (assuming all same freq)
                            if sweeper.parameter == Parameter.amplitude:
                                for pulse in pulses:
                                    if pulse in sweeper.pulses:
                                        reference_value = pulse.amplitude  # uses the amplitude of the first pulse
                            if sweeper.parameter == Parameter.duration and pulse in sweeper.pulses:
                                # for duration sweepers bake waveforms
                                sweeper.qs = QbloxSweeper(
                                    program=program, type=QbloxSweeperType.duration, rel_values=pulse.idx_range
                                )
                            else:
                                # create QbloxSweepers and attach them to qibolab sweeper
                                if sweeper.type == SweeperType.OFFSET and reference_value:
                                    sweeper.qs = QbloxSweeper.from_sweeper(
                                        program=program, sweeper=sweeper, add_to=reference_value
                                    )
                                elif sweeper.type == SweeperType.FACTOR and reference_value:
                                    sweeper.qs = QbloxSweeper.from_sweeper(
                                        program=program, sweeper=sweeper, multiply_to=reference_value
                                    )
                                else:
                                    sweeper.qs = QbloxSweeper.from_sweeper(program=program, sweeper=sweeper)

                            # finally attach QbloxSweepers to the pulses being swept
                            sweeper.qs.update_parameters = True
                            pulse.sweeper = sweeper.qs
                        else:
                            # does not play an active role
                            sweeper.qs = QbloxSweeper(
                                program=program,
                                type=QbloxSweeperType.number,
                                rel_values=range(len(sweeper.values)),
                                name=sweeper.parameter.name,
                            )

                    else:  # qubit_sweeper_parameters
                        if sweeper.qubits and sequencer.qubit in [_.name for _ in sweeper.qubits]:
                            # plays an active role
                            if sweeper.parameter == Parameter.bias:
                                reference_value = self.ports[port].offset
                                # create QbloxSweepers and attach them to qibolab sweeper
                                if sweeper.type == SweeperType.ABSOLUTE:
                                    sweeper.qs = QbloxSweeper.from_sweeper(
                                        program=program, sweeper=sweeper, add_to=-reference_value
                                    )
                                elif sweeper.type == SweeperType.OFFSET:
                                    sweeper.qs = QbloxSweeper.from_sweeper(program=program, sweeper=sweeper)
                                elif sweeper.type == SweeperType.FACTOR:
                                    raise Exception("SweeperType.FACTOR for Parameter.bias not supported")
                                sweeper.qs.update_parameters = True
                        else:
                            # does not play an active role
                            sweeper.qs = QbloxSweeper(
                                program=program,
                                type=QbloxSweeperType.number,
                                rel_values=range(len(sweeper.values)),
                                name=sweeper.parameter.name,
                            )

                    # FIXME: for qubit sweepers (Parameter.bias, Parameter.attenuation, Parameter.gain), the qubit
                    # information alone is not enough to determine what instrument parameter is to be swept.
                    # For example port gain, both the drive and readout ports have gain parameters.
                    # Until this is resolved, and since bias is only implemented with QCMs offset, this instrument will
                    # never take an active role in those sweeps.

                # Waveforms
                for index, waveform in enumerate(sequencer.waveforms_buffer.unique_waveforms):
                    sequencer.waveforms[waveform.serial] = {"data": waveform.data.tolist(), "index": index}

                # Program
                minimum_delay_between_instructions = 4

                sequence_total_duration = pulses.finish  # the minimum delay between instructions is 4ns
                time_between_repetitions = repetition_duration - sequence_total_duration
                assert time_between_repetitions > minimum_delay_between_instructions
                # TODO: currently relaxation_time needs to be greater than acquisition_hold_off
                # so that the time_between_repetitions is equal to the sequence_total_duration + relaxation_time
                # to be compatible with th erest of the platforms, change it so that time_between_repetitions
                # is equal to pulsesequence duration + acquisition_hold_off if relaxation_time < acquisition_hold_off

                # create registers for key variables
                # nshots is used in the loop that iterates over the number of shots
                nshots_register = Register(program, "nshots")
                # navgs is used in the loop of hardware averages
                navgs_register = Register(program, "navgs")

                header_block = Block("setup")

                body_block = Block()

                body_block.append(f"wait_sync {minimum_delay_between_instructions}")
                if self.ports[port].hardware_mod_en:
                    body_block.append("reset_ph")
                    body_block.append_spacer()

                pulses_block = Block("play")
                # Add an initial wait instruction for the first pulse of the sequence
                initial_wait_block = wait_block(
                    wait_time=pulses.start, register=Register(program), force_multiples_of_four=False
                )
                pulses_block += initial_wait_block

                for n in range(pulses.count):
                    if pulses[n].sweeper and pulses[n].sweeper.type == QbloxSweeperType.start:
                        pulses_block.append(f"wait {pulses[n].sweeper.register}")

                    if self.ports[port].hardware_mod_en:
                        # # Set frequency
                        # _if = self.get_if(pulses[n])
                        # pulses_block.append(f"set_freq {convert_frequency(_if)}", f"set intermediate frequency to {_if} Hz")

                        # Set phase
                        if pulses[n].sweeper and pulses[n].sweeper.type == QbloxSweeperType.relative_phase:
                            pulses_block.append(f"set_ph {pulses[n].sweeper.register}")
                        else:
                            pulses_block.append(
                                f"set_ph {convert_phase(pulses[n].relative_phase)}",
                                comment=f"set relative phase {pulses[n].relative_phase} rads",
                            )

                    # Calculate the delay_after_play that is to be used as an argument to the play instruction
                    if len(pulses) > n + 1:
                        # If there are more pulses to be played, the delay is the time between the pulse end and the next pulse start
                        delay_after_play = pulses[n + 1].start - pulses[n].start
                    else:
                        delay_after_play = sequence_total_duration - pulses[n].start

                    if delay_after_play < minimum_delay_between_instructions:
                        raise Exception(
                            f"The minimum delay between the start of two pulses in the same channel is {minimum_delay_between_instructions}ns."
                        )

                    if pulses[n].sweeper and pulses[n].sweeper.type == QbloxSweeperType.duration:
                        RI = pulses[n].sweeper.register
                        if pulses[n].type == PulseType.FLUX:
                            RQ = pulses[n].sweeper.register
                        else:
                            RQ = pulses[n].sweeper.aux_register

                        pulses_block.append(
                            f"play  {RI},{RQ},{delay_after_play}",  # FIXME delay_after_play won't work as the duration increases
                            comment=f"play pulse {pulses[n]} sweeping its duration",
                        )
                    else:
                        # Prepare play instruction: play wave_i_index, wave_q_index, delay_next_instruction
                        pulses_block.append(
                            f"play  {sequencer.waveforms_buffer.unique_waveforms.index(pulses[n].waveform_i)},{sequencer.waveforms_buffer.unique_waveforms.index(pulses[n].waveform_q)},{delay_after_play}",
                            comment=f"play waveforms {pulses[n]}",
                        )

                body_block += pulses_block
                body_block.append_spacer()

                final_reset_block = wait_block(
                    wait_time=time_between_repetitions, register=Register(program), force_multiples_of_four=False
                )
                body_block += final_reset_block

                footer_block = Block("cleaup")
                footer_block.append(f"stop")

                # wrap pulses block in sweepers loop blocks
                for sweeper in sweepers:
                    body_block = sweeper.qs.block(inner_block=body_block)

                nshots_block: Block = loop_block(
                    start=0, stop=nshots, step=1, register=nshots_register, block=body_block
                )
                navgs_block = loop_block(start=0, stop=navgs, step=1, register=navgs_register, block=nshots_block)
                program.add_blocks(header_block, navgs_block, footer_block)

                sequencer.program = repr(program)

    def upload(self):
        """Uploads waveforms and programs of all sequencers and arms them in preparation for execution.

        This method should be called after `process_pulse_sequence()`.
        It configures certain parameters of the instrument based on the needs of resources determined
        while processing the pulse sequence.
        """
        # Setup
        for sequencer_number in self._used_sequencers_numbers:
            target = self.device.sequencers[sequencer_number]
            self._set_device_parameter(target, "sync_en", value=True)
            self._set_device_parameter(target, "marker_ovr_en", value=True)  # Default after reboot = False
            self._set_device_parameter(target, "marker_ovr_value", value=15)  # Default after reboot = 0

        for sequencer_number in self._unused_sequencers_numbers:
            target = self.device.sequencers[sequencer_number]
            self._set_device_parameter(target, "sync_en", value=False)
            self._set_device_parameter(target, "marker_ovr_en", value=True)  # Default after reboot = False
            self._set_device_parameter(target, "marker_ovr_value", value=0)  # Default after reboot = 0
            if sequencer_number >= 4:  # Never disconnect default sequencers
                self._set_device_parameter(target, "channel_map_path0_out0_en", value=False)
                self._set_device_parameter(target, "channel_map_path0_out2_en", value=False)
                self._set_device_parameter(target, "channel_map_path1_out1_en", value=False)
                self._set_device_parameter(target, "channel_map_path1_out3_en", value=False)

        # There seems to be a bug in qblox that when any of the mappings between paths and outputs is set,
        # the general offset goes to 0 (eventhough the parameter will still show the right value).
        # Until that is fixed, I'm going to always set the offset just before playing (bypassing the cache):
        self.device.out0_offset(self._device_parameters[self.device.name + "." + "out0_offset"])
        self.device.out1_offset(self._device_parameters[self.device.name + "." + "out1_offset"])
        self.device.out2_offset(self._device_parameters[self.device.name + "." + "out2_offset"])
        self.device.out3_offset(self._device_parameters[self.device.name + "." + "out3_offset"])

        # Upload waveforms and program
        qblox_dict = {}
        sequencer: Sequencer
        for port in self._output_ports_keys:
            for sequencer in self._sequencers[port]:
                # Add sequence program and waveforms to single dictionary
                qblox_dict[sequencer] = {
                    "waveforms": sequencer.waveforms,
                    "weights": sequencer.weights,
                    "acquisitions": sequencer.acquisitions,
                    "program": sequencer.program,
                }

                # Upload dictionary to the device sequencers
                self.device.sequencers[sequencer.number].sequence(qblox_dict[sequencer])

                # DEBUG: QCM Save sequence to file
                if self._debug_folder != "":
                    filename = self._debug_folder + f"Z_{self.name}_sequencer{sequencer.number}_sequence.json"
                    with open(filename, "w", encoding="utf-8") as file:
                        json.dump(qblox_dict[sequencer], file, indent=4)
                        file.write(sequencer.program)

        # Arm sequencers
        for sequencer_number in self._used_sequencers_numbers:
            self.device.arm_sequencer(sequencer_number)

        # DEBUG: QCM Print Readable Snapshot
        # print(self.name)
        # self.device.print_readable_snapshot(update=True)

        # DEBUG: QCM Save Readable Snapshot
        from qibolab.instruments.qblox.debug import print_readable_snapshot

        if self._debug_folder != "":
            filename = self._debug_folder + f"Z_{self.name}_snapshot.json"
            with open(filename, "w", encoding="utf-8") as file:
                print_readable_snapshot(self.device, file, update=True)

    def play_sequence(self):
        """Executes the sequence of instructions."""

        for sequencer_number in self._used_sequencers_numbers:
            # Start used sequencers
            self.device.start_sequencer(sequencer_number)

    def start(self):
        """Empty method to comply with Instrument interface."""

        settings: ClusterQCM_BB_Settings = self.settings
        if self.is_connected:
            try:
                for port in ["o1", "o2", "o3", "o4"]:
                    if port in settings.ports:
                        port_settings: ClusterBB_OutputPort_Settings = settings.ports[port]
                        self.ports[port].offset = port_settings.offset
            except:
                log.warning("Unable to set offsets")

    def stop(self):
        """Stops all sequencers"""

        for sequencer_number in self._used_sequencers_numbers:
            state = self.device.get_sequencer_state(sequencer_number)
            if state.status != "STOPPED":
                log.warning(
                    f"Device {self.device.sequencers[sequencer_number].name} did not stop normally\nstate: {state}"
                )
        try:
            self.device.stop_sequencer()
        except:
            log.warning("Unable to stop sequencers")

        try:
            for port in self.ports:
                self.ports[port].offset = 0

            # self._set_device_parameter(self.device, "out0_offset", value=0)
            # self._set_device_parameter(self.device, "out1_offset", value=0)
            # self._set_device_parameter(self.device, "out2_offset", value=0)
            # self._set_device_parameter(self.device, "out3_offset", value=0)
            # self.device.out0_offset(0)
            # self.device.out1_offset(0)
            # self.device.out2_offset(0)
            # self.device.out3_offset(0)
        except:
            log.warning("Unable to clear offsets")

    def disconnect(self):
        """Empty method to comply with Instrument interface."""
        self._erase_device_parameters_cache()
        self._cluster = None
        self.is_connected = False
