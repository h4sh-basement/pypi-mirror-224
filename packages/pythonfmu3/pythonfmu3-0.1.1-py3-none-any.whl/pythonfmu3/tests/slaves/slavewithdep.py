import math
from pythonfmu3.fmi3slave import Fmi3Slave, Fmi3Causality, Real
from localmodule import get_amplitude, get_time_constant


class PythonSlaveWithDep(Fmi3Slave):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.realIn = 22.0
        self.realOut = 0.0
        self.register_variable(Real("realIn", causality=Fmi3Causality.input))
        self.register_variable(Real("realOut", causality=Fmi3Causality.output))

    def do_step(self, current_time, step_size):
        self.realOut = self.realIn * get_amplitude() * math.exp((current_time + step_size) / get_time_constant())
        return True
