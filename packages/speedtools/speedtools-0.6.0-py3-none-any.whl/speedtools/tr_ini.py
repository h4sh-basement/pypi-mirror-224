#
# Copyright (c) 2023 Rafał Kuźnia <rafal.kuznia@protonmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from __future__ import annotations

import logging
from collections.abc import Iterator
from configparser import ConfigParser
from dataclasses import dataclass
from itertools import starmap
from pathlib import Path

from parse import parse, search  # type: ignore[import]

from speedtools.types import Color, LightAttributes

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SunIni:
    angle_theta: float
    angle_rho: float
    radius: float
    rotates: bool
    additive: bool
    in_front: bool


class TrackIni:
    def __init__(self, parser: ConfigParser) -> None:
        self.parser = parser

    @classmethod
    def from_file(cls, path: Path) -> TrackIni:
        parser = ConfigParser()
        with open(path, "r", encoding="utf-8") as file:
            parser.read_file(file)
        return cls(parser=parser)

    @classmethod
    def _make_glow(cls, name: str, string: str) -> LightAttributes:
        no_spaces = string.replace(" ", "")
        results = search("[{:d},{:d},{:d},{:d}],{:d},{:d},{:d},{:f}", no_spaces)
        (identifier,) = parse("glow{:d}", name)
        alpha, red, green, blue, is_blinking, interval, _, flare_size = results
        color = Color(alpha=alpha, red=red, green=green, blue=blue)
        blink_interval = interval if is_blinking == 1 else None
        return LightAttributes(
            identifier=identifier,
            color=color,
            blink_interval_ms=blink_interval,
            flare_size=flare_size,
        )

    @property
    def glows(self) -> Iterator[LightAttributes]:
        return starmap(self._make_glow, self.parser["track glows"].items())

    @property
    def sun(self) -> SunIni | None:
        try:
            sun = self.parser["sun"]
            if sun["hasSun"] == "0":
                return None
            return SunIni(
                angle_theta=float(sun["angleTheta"]),
                angle_rho=float(sun["angleRho"]),
                radius=float(sun["radius"]),
                rotates=sun.get("rotates", "0") != "0",
                additive=sun.get("additive", "0") != "0",
                in_front=sun.get("inFront", "0") != "0",
            )
        except KeyError:
            return None
