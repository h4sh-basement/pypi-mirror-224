import sys
from typing import List, Optional, TypeVar, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ValueChart = TypedDict("ValueChart", {"countCurrent": Union[int, float], "countPrevious": Optional[Union[int, float]]})

DistributionChart = List[TypedDict("DistributionChartEntry", {"key": str, "value": Union[int, float]})]

TimeBasedChart = List[TypedDict("TimeBasedChartEntry", {"label": str, "value": Union[int, float]})]

PercentageChart = Union[int, float]

ObjectiveChart = TypedDict("ObjectiveChart", {"value": Union[int, float], "objective": Optional[Union[int, float]]})

LeaderboardChart = List[TypedDict("LeaderboardChartEntry", {"key": str, "value": Union[int, float]})]

SmartChart = TypeVar("SmartChart")

Chart = Union[
    ValueChart,
    DistributionChart,
    TimeBasedChart,
    PercentageChart,
    ObjectiveChart,
    LeaderboardChart,
    SmartChart,
]
