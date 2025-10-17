import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self._prev_error = 0.0

    def control(self, reference: float, output: float) -> float:
        error = float(reference - output)
        derivative = error - self._prev_error
        u = self.kp * error + self.kd * derivative
        self._prev_error = error
        return float(u)