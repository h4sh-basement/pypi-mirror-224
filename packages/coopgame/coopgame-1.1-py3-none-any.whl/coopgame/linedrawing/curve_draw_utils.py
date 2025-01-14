import pygame
from coopgame.colors import Color
from typing import List, Dict, Callable
from coopstructs.geometry.curves.curves import Curve
from coopstructs.geometry import Line, PolygonRegion
import numpy as np
from shapely.geometry import LineString
import coopgame.pygamehelpers as help
from dataclasses import dataclass
import coopgame.linedrawing.line_draw_utils as lutils
import coopgame.pointdrawing.point_draw_utils as putils

@dataclass(frozen=True)
class CurveDrawArgs:
    line_args: lutils.DrawLineArgs = None
    control_point_args: putils.DrawPointArgs = None
    control_line_args: lutils.DrawLineArgs = None
    draw_scale_matrix: np.ndarray = None
    buffer: int = None
    buffer_color: Color = None
    resolution: int = 30

    @property
    def BaseArgs(self):
        return CurveDrawArgs(
            line_args=self.line_args.BaseArgs,
            draw_scale_matrix=self.draw_scale_matrix,
            resolution=self.resolution
        )

    @property
    def OverlayArgs(self):
        return CurveDrawArgs(
            draw_scale_matrix=self.draw_scale_matrix,
            control_point_args=self.control_point_args,
            control_line_args=self.control_line_args
        )

    @property
    def BufferArgs(self):
        return CurveDrawArgs(
            draw_scale_matrix=self.draw_scale_matrix,
            buffer=self.buffer,
            buffer_color=self.buffer_color,
        )

def draw_curves(curves: Dict[Curve, CurveDrawArgs],
                surface: pygame.Surface):

    for curve, args in curves.items():
        line_rep = curve.line_representation(resolution=args.resolution)

        if args.buffer_color:
            line = LineString([
                line_rep[0].origin] +
                [x.destination for x in line_rep]
            )

            dilated = line.buffer(args.buffer)
            poly = PolygonRegion.from_shapely_polygon(dilated)
            buffer_color = Color.GREEN if args.buffer_color is None else args.buffer_color
            help.draw_polygon(surface, [x.as_tuple() for x in poly.boundary_points], buffer_color)

        if args.control_line_args:
            lutils.draw_lines(
                {x: args.control_line_args for x in curve.ControlLines},
                surface=surface,
                draw_scale_matrix=args.draw_scale_matrix
            )

        lutils.draw_lines(
            lines={x: args.line_args for x in line_rep},
            surface=surface,
            draw_scale_matrix=args.draw_scale_matrix

        )

        if args.control_point_args:
            putils.draw_points(
                points={
                    x.as_tuple(): args.control_point_args for x in curve.ControlPoints
                },
                surface=surface,
                draw_scale_matrix=args.draw_scale_matrix
            )