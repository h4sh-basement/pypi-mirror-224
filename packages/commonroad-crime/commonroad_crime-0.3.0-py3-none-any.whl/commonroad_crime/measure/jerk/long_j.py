__author__ = "Yuanfei Lin"
__copyright__ = "TUM Cyber-Physical Systems Group"
__credits__ = ["KoSi"]
__version__ = "0.3.0"
__maintainer__ = "Yuanfei Lin"
__email__ = "commonroad@lists.lrz.de"
__status__ = "beta"

import math
import logging

from commonroad_crime.measure.jerk.lat_j import LatJ
from commonroad_crime.data_structure.configuration import CriMeConfiguration
from commonroad_crime.data_structure.type import TypeJerk, TypeMonotone
import commonroad_crime.utility.general as utils_gen
import commonroad_crime.utility.logger as utils_log
import commonroad_crime.utility.solver as utils_sol

logger = logging.getLogger(__name__)


class LongJ(LatJ):
    """
    Jerk is the rate of change in acceleration, and thus quantifies over the abruptness of a maneuver.
    """

    measure_name = TypeJerk.LongJ
    monotone = TypeMonotone.POS

    def __init__(self, config: CriMeConfiguration):
        super(LongJ, self).__init__(config)

    def compute(self, time_step: int, vehicle_id: int = None, verbose: bool = True):
        self.time_step = time_step
        utils_log.print_and_log_info(
            logger,
            f"* Computing the {self.measure_name} at time step {time_step}",
            verbose,
        )
        evaluated_state = self.ego_vehicle.state_at_time(self.time_step)
        lanelet_id = self.sce.lanelet_network.find_lanelet_by_position(
            [self.ego_vehicle.state_at_time(time_step).position]
        )[0]
        # orientation of the ego vehicle and the other vehicle
        ego_orientation = utils_sol.compute_lanelet_width_orientation(
            self.sce.lanelet_network.find_lanelet_by_id(lanelet_id[0]),
            self.ego_vehicle.state_at_time(time_step).position,
        )[1]
        self.value = utils_gen.int_round(
            abs(evaluated_state.jerk * math.cos(ego_orientation)), 2
        )
        utils_log.print_and_log_info(
            logger, f"*\t\t {self.measure_name} = {self.value}", verbose
        )
        return self.value

    def visualize(self):
        pass
