import json
import os
from json import JSONDecodeError
from os import path
from typing import Final

EMPTY_STR: Final = "[[EMPTY]]"


def set_screen_shader(shader_path: str) -> int:
    return os.system(f"hyprctl keyword decoration:screen_shader '{shader_path}'")


def clear_screen_shader() -> int:
    return set_screen_shader(EMPTY_STR)


def get_screen_shader() -> str | None:
    """Gets full path of currently set screen shader."""

    try:
        o = json.load(
            # TODO: Remove sed workaround when hyprwm/Hyprland@4743041 is pushed to
            # a stable release
            os.popen("hyprctl -j getoption decoration:screen_shader | sed '/^adding/d'")
        )
    except JSONDecodeError as e:
        raise RuntimeError("Failed to parse JSON returned by hyprctl") from e

    shader = str(o["str"]).strip()
    if shader == EMPTY_STR:
        return None
    if not path.isfile(shader):
        raise RuntimeError(f"Got shader {shader} from hyprctl, which does not exist")

    return shader
