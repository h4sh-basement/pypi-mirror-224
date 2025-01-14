from functools import partial

from .util import cache_bool, cache_string


def channel_bool_prop(param):
    """meta function for channel boolean parameters"""

    @partial(cache_bool, param=param)
    def fget(self):
        return (
            not int.from_bytes(
                getattr(
                    self.public_packet,
                    f"{'strip' if 'strip' in type(self).__name__.lower() else 'bus'}state",
                )[self.index],
                "little",
            )
            & getattr(self._modes, f"_{param.lower()}")
            == 0
        )

    def fset(self, val):
        self.setter(param, 1 if val else 0)

    return property(fget, fset)


def channel_label_prop():
    """meta function for channel label parameters"""

    @partial(cache_string, param="label")
    def fget(self) -> str:
        return getattr(
            self.public_packet,
            f"{'strip' if 'strip' in type(self).__name__.lower() else 'bus'}labels",
        )[self.index]

    def fset(self, val: str):
        self.setter("label", str(val))

    return property(fget, fset)


def strip_output_prop(param):
    """meta function for strip output parameters. (A1-A5, B1-B3)"""

    @partial(cache_bool, param=param)
    def fget(self):
        return (
            not int.from_bytes(self.public_packet.stripstate[self.index], "little")
            & getattr(self._modes, f"_bus{param.lower()}")
            == 0
        )

    def fset(self, val):
        self.setter(param, 1 if val else 0)

    return property(fget, fset)


def bus_mode_prop(param):
    """meta function for bus mode parameters"""

    @partial(cache_bool, param=param)
    def fget(self):
        modelist = {
            "amix": (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1),
            "repeat": (0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2),
            "bmix": (1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3),
            "composite": (0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0),
            "tvmix": (1, 0, 1, 4, 5, 4, 5, 0, 1, 0, 1),
            "upmix21": (0, 2, 2, 4, 4, 6, 6, 0, 0, 2, 2),
            "upmix41": (1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3),
            "upmix61": (0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8),
            "centeronly": (1, 0, 1, 0, 1, 0, 1, 8, 9, 8, 9),
            "lfeonly": (0, 2, 2, 0, 0, 2, 2, 8, 8, 10, 10),
            "rearonly": (1, 2, 3, 0, 1, 2, 3, 8, 9, 10, 11),
        }
        vals = (
            int.from_bytes(self.public_packet.busstate[self.index], "little") & val
            for val in self._modes.modevals
        )
        if param == "normal":
            return not any(vals)
        return tuple(round(val / 16) for val in vals) == modelist[param]

    def fset(self, val):
        self.setter(param, 1 if val else 0)

    return property(fget, fset)


def action_fn(param, val=1):
    """A function that performs an action"""

    def fdo(self):
        self.setter(param, val)

    return fdo
