from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class FigureOptions:
    """ -- """
    title: str = 'figure title'
    size: Tuple[int, int] = (15, 11)
    size_single: Tuple[int, int] = (11, 7)
    font_size: int = 14
    font_face: str = 'Cambria'
    save: bool = False
    show: bool = True
    show_differed: bool = True

@dataclass
class PlotOptions:
    title: str = None
    labels: Tuple[str, str, str] = ('x [-]', 'y [-]', 'z [-]')
    font_size: int = 10
    font_face: str = 'Calibri'
    type: str = 'contourf'
    colorbar: bool = True
    colorbar_lvls: int = 10
    colormap: str = 'viridis'
    vrange: Tuple[float, float] = (0.0, 1.0)
    vrange_ext: float = 0.0
    vrange_auto: bool = True
    vrange_lvls: int = 21
    contours_skip: int = 2
    contours_alpha: float = 0.6
    persist: bool = False

@dataclass
class AnimationOptions:
    print_time: bool = True
    print_dt: bool = True
    interval: int = 70
    repeat_delay: int = 1000
    blit: bool = True
