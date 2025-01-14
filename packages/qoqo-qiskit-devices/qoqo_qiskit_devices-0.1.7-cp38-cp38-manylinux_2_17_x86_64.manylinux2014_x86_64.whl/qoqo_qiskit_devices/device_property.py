"""Device information-gathering routines."""
# Copyright © 2023 HQS Quantum Simulations GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

from qiskit_ibm_provider import IBMProvider

from .mocked_properties import MockedProperties

import types


def _qiskit_gate_equivalent(gate: str) -> str:
    """Outputs qiskit equivalent of a Qoqo gate name.

    Args:
        gate (str): The name of the qoqo gate.

    Returns:
        str: The name of the equivalent Qiskit.
    """
    if gate == "PauliX":
        return "x"
    elif gate == "RotateZ":
        return "rz"
    elif gate == "SqrtPauliX":
        return "sx"
    elif gate == "CNOT":
        return "cx"


def set_qiskit_noise_information(
    device: types.ModuleType, get_mocked_information: bool = False
) -> types.ModuleType:
    """Sets a qoqo_qiskit_devices.ibm_devices instance noise info.

    Obtains the device info from qiskit's IBMProvider and performs the following updates:
        - adds damping
        - adds dephasing
        - sets single qubit gate times
        - sets two qubit gate times

    Args:
        device (ibm_devices): The qoqo_qiskit_devices instance to update.
        get_mocked_information (bool): Whether the returned information is mocked or not.

    Returns:
        ibm_devices: The input instance updated with qiskit's physical device info.
    """
    name = device.name()
    if get_mocked_information:
        properties = MockedProperties()
    else:
        properties = IBMProvider().get_backend(name).properties()

    for qubit in range(device.number_qubits()):
        damping = 1 / properties.t1(qubit=qubit)
        dephasing = 1 / properties.t2(qubit=qubit) - 1 / (2 * properties.t1(qubit=qubit))
        device.add_damping(qubit=qubit, damping=damping)
        device.add_dephasing(qubit=qubit, dephasing=dephasing)
        for gate in device.single_qubit_gate_names():
            qiskit_gate = _qiskit_gate_equivalent(gate)
            device.set_single_qubit_gate_time(
                gate=gate,
                qubit=qubit,
                gate_time=properties.gate_property(
                    gate=qiskit_gate, qubits=qubit, name="gate_length"
                )[0],
            )

    for edge in device.two_qubit_edges():
        for gate in device.two_qubit_gate_names():
            qiskit_gate = _qiskit_gate_equivalent(gate)
            device.set_two_qubit_gate_time(
                gate=gate,
                control=edge[0],
                target=edge[1],
                gate_time=properties.gate_property(
                    gate=qiskit_gate, qubits=[edge[0], edge[1]], name="gate_length"
                )[0],
            )
            device.set_two_qubit_gate_time(
                gate=gate,
                control=edge[1],
                target=edge[0],
                gate_time=properties.gate_property(
                    gate=qiskit_gate, qubits=[edge[1], edge[0]], name="gate_length"
                )[0],
            )

    return device
