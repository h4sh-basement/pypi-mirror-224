__author__ = "Yuanfei Lin"
__copyright__ = "TUM Cyber-Physical Systems Group"
__credits__ = ["KoSi"]
__version__ = "0.3.0"
__maintainer__ = "Yuanfei Lin"
__email__ = "commonroad@lists.lrz.de"
__status__ = "beta"

import logging
from typing import Union

from commonroad_crime.measure.time.ttb import TTB
from commonroad_crime.measure.time.ttk import TTK
from commonroad_crime.measure.time.tts import TTS
from commonroad_crime.measure.time.ttm import TTM
from commonroad_crime.data_structure.configuration import CriMeConfiguration
from commonroad_crime.data_structure.type import TypeTime
from commonroad_crime.utility.simulation import Maneuver
import commonroad_crime.utility.logger as utils_log

logger = logging.getLogger(__name__)


class TTR(TTM):
    """
    Time-to-react: latest possible time before the TTC, at which an evasive maneuver still exists. This
    under-approximative approach is obtained from Tamke, Andreas, Thao Dang, and Gabi Breuel.
    "A flexible method for criticality assessment in driver assistance systems." 2011 IEEE intelligent
     vehicles symposium (IV). IEEE, 2011.
    """

    measure_name = TypeTime.TTR

    def __init__(self, config: CriMeConfiguration):
        super(TTR, self).__init__(config, Maneuver.NONE)
        self._evaluator = None

    def initialize_evaluator(self, time_step: int, verbose: bool):
        """
        Initializes the evaluators for underestimating the ttr.
        """
        self._evaluator = [
            TTB(self.configuration),
            TTK(self.configuration),
            TTS(self.configuration),
        ]
        self.time_step = time_step
        self.state_list_set = []
        self.ttc = self.ttc_object.compute(time_step, verbose=verbose)

    def compute(
        self,
        time_step: int = 0,
        vehicle_id: Union[int, None] = None,
        ttc: float = None,
        verbose: bool = True,
    ):
        utils_log.print_and_log_info(
            logger,
            f"* Computing the {self.measure_name} at time step {time_step}",
            verbose,
        )
        self.initialize_evaluator(time_step, verbose)
        ttm = dict()
        for evl in self._evaluator:
            ttm[evl] = evl.compute(time_step, self.ttc, verbose=False)
            self.state_list_set += evl.state_list_set
        self.value = max(ttm.values())
        # plots the selected state list as the last evasive maneuver.
        self.selected_state_list = max(ttm, key=ttm.get).selected_state_list
        self.maneuver = max(ttm, key=ttm.get).maneuver
        utils_log.print_and_log_info(logger, "*\t maximum of the values")
        utils_log.print_and_log_info(
            logger, f"*\t\t {self.measure_name} = {self.value}", verbose
        )
        return self.value
