from ..utils.doe_formatters import short_name
from .story import Doe2Story
from dataclasses import dataclass
from typing import List
from uuid import uuid4

from honeybee.room import Room


@dataclass
class Zone:

    name: str
    heating_setpoint: float
    cooling_setpoint: float

    @classmethod
    def from_room(cls, room: Room):
        if not isinstance(room, Room):
            raise ValueError(
                f'Unsupported type: {type(room)}\n'
                'Expected honeybee room'
            )

        name = room.display_name
        if room.properties.energy.is_conditioned:
            heating_setpoint = room.properties.energy.program_type.setpoint.heating_setpoint
            cooling_setpoint = room.properties.energy.program_type.setpoint.cooling_setpoint
        else:
            heating_setpoint = 72
            cooling_setpoint = 75

        return cls(name=name, heating_setpoint=heating_setpoint,
                   cooling_setpoint=cooling_setpoint)

    def to_inp(self):
        inp_str = f'"{self.name} Zn"   = ZONE\n  ' \
            'TYPE             = UNCONDITIONED\n  ' \
            f'DESIGN-HEAT-T    = {self.heating_setpoint}\n  ' \
            f'DESIGN-COOL-T    = {self.cooling_setpoint}\n  ' \
            'SIZING-OPTION    = ADJUST-LOADS\n  ' \
            f'SPACE            = "{self.name}"\n  ..\n'
        return inp_str

    def __repr__(self) -> str:
        return self.to_inp()


@dataclass
class HVACSystem:
    """Placeholder HVAC system class, returns each floor as a doe2,
    HVAC system, with rooms as zones.
    Args:
        name: story display name
        zones: list of doe2.hvac.Zone objects serviced by the system
    Init method(s):
        1. from_story(story: DFStory) -> doe2_system:
    """
    name: str
    zones: List[Zone]

    @classmethod
    def from_story(cls, story: Doe2Story):
        if not isinstance(story, Doe2Story):
            raise ValueError(
                f'Unsupported type: {type(story)}\n'
                'Expected dragonfly.story.Story'
            )
        name = story.display_name
        zones = [Zone.from_room(room) for room in story.rooms]
        return cls(name=name, zones=zones)

    def to_inp(self):
        sys_str = f'"{self.name}flr_Sys (SUM)" = SYSTEM\n' \
            '   TYPE             = SUM\n' \
            '   HEAT-SOURCE      = NONE\n' \
            '   SYSTEM-REPORTS   = NO\n   ..\n'
        zones_str = '\n'.join(zone.to_inp() for zone in self.zones)
        inp_str = '\n'.join([sys_str, zones_str])
        return inp_str

    def __repr__(self):
        return self.to_inp()
