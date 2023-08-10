"""Class for controlling a swarm of Crazyflie UAVs."""
import time
from typing import List

import numpy as np
from scipy.optimize import linear_sum_assignment

from .drone_controller import DroneController


class SwarmController:
    """SwarmController.

    Class for controlling a swarm of Crazyflie UAVs.
    """

    def __init__(self, URIs: List[str]):
        """__init__.

        Args:
            URIs (List[str]): list of URIs for the drones
        """
        self.UAVs = [DroneController(URI, in_swarm=True) for URI in URIs]
        time.sleep(1)
        print(f"Swarm with {self.num_drones} drones ready to go...")
        time.sleep(1)

    def reshuffle(self, new_pos: np.ndarray, new_orn: np.ndarray):
        """reshuffle.

        Args:
            new_pos (np.ndarray): (n, 4) array for the target position to assign to all the drones
            new_orn (np.ndarray): (n, 4) array for the target orientation to assign to all the drones
        """
        # reshuffle the drones given a new start_pos such that all drones map to the new start_pos cleanly
        assert (
            new_pos.shape == new_orn.shape
        ), "start_pos must have same shape as start_orn"
        assert (
            len(new_pos) == self.num_drones
        ), "must have same number of drones as number of drones"
        assert (
            new_pos.shape[1] == 3
        ), "start pos must have only xyz, start orn must have only pqr"

        # compute cost matrix
        cost = abs(
            np.expand_dims(self.states[:, :3], axis=0) - np.expand_dims(new_pos, axis=1)
        )
        cost = np.sum(cost, axis=-1)

        # compute optimal assignment using Hungarian algo
        _, reassignment = linear_sum_assignment(cost)
        self.UAVs = [self.UAVs[i] for i in reassignment]

        # send setpoints
        setpoints = np.concatenate(
            (new_pos, np.expand_dims(new_orn[:, -1], axis=-1)), axis=-1
        )
        self.set_pos_control(True)
        self.set_setpoints(setpoints)

        cost = np.choose(reassignment, cost.T)
        return cost

    @property
    def num_drones(self):
        """num_drones."""
        return len(self.UAVs)

    @property
    def position_estimate(self):
        """position_estimate."""
        return np.stack([UAV.position_estimate for UAV in self.UAVs], axis=0)

    @property
    def states(self):
        """states."""
        return self.position_estimate

    def set_pos_control(self, setting: bool):
        """set_pos_control.

        Args:
            setting (bool): whether to set all drones to pos control
        """
        for UAV in self.UAVs:
            UAV.set_pos_control(setting)

    def arm(self, settings: list[bool] | np.ndarray):
        """arm.

        Args:
            settings (list[bool] | np.ndarray): (n, ) list of booleans corresponding to which drones to arm
        """
        assert len(settings) == len(
            self.UAVs
        ), "masks length must be equal to number of drones"

        for mask, UAV in zip(settings, self.UAVs):
            if mask:
                UAV.start()
            else:
                UAV.stop()

    def end(self):
        """end."""
        # """disarms each drone and closes all connections"""
        for UAV in self.UAVs:
            UAV.end()
        time.sleep(1)

    def set_setpoints(self, setpoints: np.ndarray):
        """set_setpoints.

        Args:
            setpoints (np.ndarray): (n, 4) array for setpoint corresponding to (x, y, z, yaw) or (vx, vy, vz, vyaw)
        """
        # """sets setpoints for each drone, setpoints must be ndarray where len(setpoints) == len(UAVs)"""
        assert len(setpoints) == len(
            self.UAVs
        ), "number of setpoints must be equal to number of drones"

        for setpoint, UAV in zip(setpoints, self.UAVs):
            UAV.set_setpoint(setpoint)

    def sleep(self, seconds: float):
        """sleep.

        Args:
            seconds (float): seconds
        """
        time.sleep(seconds)
