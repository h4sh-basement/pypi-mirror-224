import logging
import re

from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.logging import LoggingMixin


class Flags(SendableMixin, LoggingMixin):
    """
    Basic but flexible handler for terminal command flags

    Allows for inplace modification:

    >>> f = Flags('abcdd')
    >>> f -= 'd'
    >>> f.flags
    >>> '-abcd'

    Arguments:
        initial_flags (str):
            initial base flags to be used and modified if needed
    """

    _logger = logging.getLogger(__name__ + ".Flags")

    def __init__(self, *initial_flags):
        if not isinstance(initial_flags, str):
            initial_flags = " ".join(initial_flags)

        self._logger.debug(f"creating Flags with initial flags " f"{initial_flags}")

        self._flags = {}
        self.flags = initial_flags

    def __repr__(self):
        return self.flags

    def _add(self, section):
        raw, prefix = self.parse_string(section)
        if prefix == "-":
            self.ensure_prefix_exists(prefix)
            self._flags["-"] += list(raw)
        else:
            self.ensure_prefix_exists(prefix)
            self._flags[prefix].append(raw)

        self._logger.debug(f"adding {raw} to flags. " f"Flags are now {self.flags}")

    def __add__(self, other):
        sections = other.split(" ")
        for section in sections:
            self._add(section)

    def __iadd__(self, other):
        self.__add__(other)
        self._logger.debug(
            f"adding {other} to flags inplace. " f"Flags are now {self.flags}"
        )
        return self

    def _sub(self, section):
        raw, prefix = self.parse_string(section)
        if prefix == "-":
            for char in raw:
                try:
                    self._flags["-"].remove(char)
                except ValueError:
                    pass
        else:
            try:
                self._flags["--"].remove(raw)
            except ValueError:
                pass

        self._logger.debug(
            f"subtracting {raw} from flags. " f"Flags are now {self.flags}"
        )

    def __sub__(self, other):
        """Subtract unique flags in `other` once."""
        sections = other.split(" ")
        for section in sections:
            self._sub(section)

    def __isub__(self, other):
        self.__sub__(other)
        self._logger.debug(
            f"subtracting {other} from flags inplace. " f"Flags are now {self.flags}"
        )
        return self

    def ensure_prefix_exists(self, prefix):
        """Ensures that the prefix exists in the internal storage, creating
        it if not"""
        if prefix not in self._flags:
            self._flags[prefix] = []

    def parse_string(self, string) -> [str, bool]:
        """
        Takes a string, and strips away any non-alphanumeric chars.
        Returns True in secondary return if this is a verbose flag

        Args:
            string (str):
                input flags

        Returns (str, bool):
            filtered input
            True if this is a verbose flag
        """
        raw = strip_non_alphanumeric(string)
        num = string.count("-")

        # special case
        if num == 0:
            num = 1

        return raw, "-" * num

    @property
    def flags(self):
        """Returns the fully qualified flags as a string"""
        if sum([len(f) for f in self._flags.values()]) == 0:
            self._logger.info("sum of lens is 0, returning ''")
            return ""
        self._logger.info(f"creating string from internal flags {self._flags}")
        output = []
        for prefix, flags in self._flags.items():
            if prefix == "-":
                output.append("-" + "".join(flags))
            else:
                output.append(prefix + f" {prefix}".join(flags))

        string = " ".join(output)
        self._logger.info(f"done -> {string}")
        return string

    @flags.setter
    def flags(self, inp):
        """Set the flags to the new input

        Arguments:
            inp (str):
                new flags to use (will overwrite old ones)
        """
        self._flags = {}
        self.__add__(inp)


def strip_non_alphanumeric(string):
    """
    remove any non-alphanumeric strings from input string

    Args:
        string (str):
            input string

    Returns (str):
        input string, sans any non-alphanumeric chars

    """
    pattern = re.compile("[\W_]+", re.UNICODE)  # noqa: W605

    return pattern.sub("", string)
