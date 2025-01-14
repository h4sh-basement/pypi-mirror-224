from __future__ import annotations

import json
from copy import deepcopy
from functools import reduce
from operator import getitem
from typing import Any, Callable, Optional, Union

import yaml

from .dict_traverse import traverse
from .stop_conditions import generate_depth_stop_condition


def in_or_callable(d: Union[ndict, dict], k: Union[str, Callable]) -> bool:
    return isinstance(k, Callable) or isinstance(k, str) and k in d


# TODO: depth change to max_depth.
# TODO: add comments.
# TODO: Change keys, values and items to generators.
class ndict:
    """Nested dictionary.

    Users shouldn't modify the underling data outside of ndict class. Value overwritten is enabled.

    Args:
        d (Optional[Union[ndict, dict]]): If d is a dict, do make sure the path separator is the givein delimiter if
            path is used as key.
        delimiter (str): Path separator. Can be any string.
    """

    ALL_MISSING_METHODS = ["ignore", "false", "exception"]

    def __init__(self, d: Optional[Union[ndict, dict]] = None, delimiter: str = ";") -> None:
        assert isinstance(delimiter, str), f"delimiter must be str, but recieved {type(delimiter)}"

        self._delimiter = delimiter
        self._d = {}
        self._flatten_dict = {}

        if isinstance(d, ndict):
            self.load_state_dict(d.state_dict())
        elif isinstance(d, dict):
            for k, v in d.items():
                self[k] = v
        else:
            assert d is None, f"Unexpected type {type(d)}"

    @property
    def dict(self) -> dict:
        """Underling dictionary. Do not change it!"""
        return self._d

    @property
    def flatten_dict(self) -> dict[str, Any]:
        """Flattened dictionary of {path: value} pairs."""
        return self._flatten_dict

    @property
    def paths(self) -> list[str]:
        """Get all possible paths."""

        def _path_action(tree: dict, res: list[str], node: Any, path: str, depth: int):
            if path is not None:
                res.append(path)

        res = []
        traverse(tree=self.dict, res=res, actions=_path_action)
        return res

    @property
    def delimiter(self) -> str:
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter: str) -> None:
        if delimiter == self._delimiter:
            return
        self._flatten_dict = {
            p.replace(self._delimiter, delimiter): v for p, v in self.flatten_dict.items()
        }
        self._delimiter = delimiter

    def state_dict(self) -> dict:
        return {"dict": self.dict, "flatten_dict": self.flatten_dict, "delimiter": self.delimiter}

    def load_state_dict(self, states: Union[dict, ndict]) -> Any:
        """The delimiter is only for properly initialize the object."""
        assert isinstance(
            states["delimiter"], str
        ), f"Unexpected delimiter type: {states['delimiter']}."
        delimiter = self.delimiter
        self._d = states["dict"]
        self._flatten_dict = states["flatten_dict"]
        self._delimiter = states["delimiter"]
        self.delimiter = delimiter
        return self

    def get(
        self,
        path: Optional[str] = None,
        default: Optional[Any] = None,
        keys: Optional[list[Union[str, tuple[str, Callable]]]] = None,
        dict_as_ndict: bool = True,
    ) -> Any:
        """Get values from the nested dictionary.

        Args:
            path (Optional[str] = None):
            keys (Optional[list[Union[str, tuple[str, Callable]]]] = None). Callables should accept self (ndict),
                path: str 2 arguments.
        """

        def _get_value_or_default(
            key: Union[str, Callable], default: Any, path: Optional[str] = None
        ) -> Any:
            if isinstance(key, str):
                try:
                    return self._get_node(key, dict_as_ndict=dict_as_ndict)
                except KeyError:
                    return default

            assert isinstance(key, Callable), f"Unexpected key type: {type(key)}."
            try:
                return key(self, path)
            except:
                return default

        assert (path is not None or keys is not None) and not (
            path is not None and keys is not None
        ), f"Users can only provide path or keys: path: {path is not None}, keys: {keys is not None}."

        if path is not None:
            try:
                return self._get_node(path, dict_as_ndict=dict_as_ndict)
            except KeyError:
                return default

        return {
            **{k: _get_value_or_default(k, default) for k in keys if isinstance(k, str)},  # type: ignore
            **{
                k[0]: _get_value_or_default(k[1], default, path=k[0])
                for k in keys  # type: ignore
                if isinstance(k, tuple)
            },
        }

    def update(
        self, d: Union[dict, ndict], ignore_none: bool = False, ignore_missing: bool = False
    ) -> None:
        """Could be slow at current stage.

        Note that if leaves of the d is Callable, the leaves will be invoked with self: ndict and path: str 2 arguments.
        """
        d = ndict(d).flatten_dict
        for p, v in d.items():
            if (v is None and ignore_none) or (p not in self.flatten_dict and ignore_missing):
                continue
            self[p] = v(self, p) if isinstance(v, Callable) else v

    def keys(self, max_depth: int = 1) -> list[str]:
        """Return a list of leave and depth <= depth"""

        def _keys_action(tree: dict, res: list[str], node: Any, path: str, depth: int):
            if path is not None and (not isinstance(node, dict) or depth == max_depth):
                res.append(path)

        res = []
        traverse(tree=self.dict, res=res, actions=_keys_action, depth=max_depth)
        return res

    def values(self, max_depth: int = 1, dict_as_ndict: bool = True) -> list[Any]:
        def _values_action(tree: dict, res: list[Any], node: Any, path: str, depth: int):
            if path is not None and (not isinstance(node, dict) or depth == max_depth):
                if dict_as_ndict and isinstance(node, dict):
                    node = ndict(delimiter=self.delimiter).load_state_dict(
                        {
                            "dict": node,
                            "flatten_dict": self._get_flatten_dict_of_subtree(path),
                            "delimiter": self.delimiter,
                        }
                    )
                res.append(ndict(node) if dict_as_ndict and isinstance(node, dict) else node)

        res = []
        traverse(tree=self.dict, res=res, actions=_values_action, depth=max_depth)
        return res

    def items(self, max_depth: int = 1, dict_as_ndict: bool = True) -> list[tuple[str, Any]]:
        return list(
            zip(
                self.keys(max_depth=max_depth),
                self.values(max_depth=max_depth, dict_as_ndict=dict_as_ndict),
            )
        )

    # May let the users to cumstomize the conditions.
    def size(self, max_depth: int = 1, ignore_none: bool = False) -> int:
        def _size_action(tree: dict, res: list[int], node: Any, path: str, depth: int):
            if (
                path is not None
                and (not isinstance(node, dict) or depth == max_depth)
                and (not ignore_none or ignore_none and node is not None)
            ):
                res[0] += 1

        res = [0]
        traverse(tree=self.dict, res=res, actions=_size_action, depth=max_depth)
        return res[0]

    def diff(self, d: Union[ndict, dict]) -> dict[str, tuple[Any, Any]]:
        """Compare the leaves."""
        d = ndict(d)
        res = {}
        for p, v1 in self.flatten_dict.items():
            if p not in d.flatten_dict:
                res[p] = (v1, None)
            elif v1 != d[p]:
                res[p] = (v1, d[p])
        res.update({p: (None, v) for p, v in d.flatten_dict.items() if p not in self})
        return res

    def json_str(self, sort_keys: bool = False, indent: int = 2) -> str:
        return json.dumps(self.dict, sort_keys=sort_keys, indent=indent)

    def __getitem__(self, key: Union[str, int]) -> Any:
        path = key if isinstance(key, str) else list(self.keys())[key]
        return self._get_node(path, dict_as_ndict=True)

    def __delitem__(self, path: str) -> None:
        path_list = path.split(self._delimiter)
        d = self._get_node(path_list[:-1], dict_as_ndict=False)
        del d[path_list[-1]]
        if path:
            self._flatten_dict = {
                p: v for p, v in self._flatten_dict.items() if not p.startswith(path)
            }
        else:
            self._flatten_dict = {
                p: v for p, v in self._flatten_dict.items() if not p.startswith(";") and p != ""
            }
        if len(d) == 0:
            if len(path_list) > 1:
                parent_path = self._delimiter.join(path_list[:-1])
                self._flatten_dict[parent_path] = {}

    # TODO A more efficient approach.
    def __setitem__(self, path: str, value: Any) -> None:
        """Update values of the corresponding path.

        Args:
            path (str): Path can be an existed or non-exist path. If it's existed path and the corresponding values is
                not a dictionary, then the original value will be overwrittern.
            value (Any): The value for that path.
        """
        assert isinstance(path, str), f"Path can only be str, recieved {type(path)}."
        path_list = path.split(self.delimiter)

        # Adjust dict.
        d = self._d
        for i, node in enumerate(path_list[:-1]):
            if node not in d:
                d[node] = {}
            elif not isinstance(d[node], dict):
                d[node] = {}
                tmp_p = self.delimiter.join(path_list[: i + 1])
                del self.flatten_dict[tmp_p]
            d = d[node]

        to_be_delete_node = [
            f"{path}{self.delimiter}{k}" for k in self._get_flatten_dict_of_subtree(path).keys()
        ]
        for k in to_be_delete_node:
            del self._flatten_dict[k]
        parent_path = self.delimiter.join(path_list[:-1])
        if parent_path in self._flatten_dict:
            assert (
                isinstance(self._flatten_dict[parent_path], dict)
                and not self._flatten_dict[parent_path]
            )
            del self._flatten_dict[parent_path]

        # Adjust flatten dict.
        if isinstance(value, Union[dict, ndict]):
            tmp = ndict(value)
            d[path_list[-1]] = tmp.dict
            if tmp.flatten_dict:
                for p, v in tmp.flatten_dict.items():
                    combined_path = self._delimiter.join([path, p])
                    self._flatten_dict[combined_path] = v
            else:
                self._flatten_dict[path] = {}
        else:
            d[path_list[-1]] = value
            self._flatten_dict[path] = value

    def __len__(self) -> int:
        return len(self.dict)

    def __bool__(self) -> bool:
        return bool(len(self) > 0)

    def __contains__(self, path: str) -> bool:
        if path in self.flatten_dict:
            return True

        nodes = path.split(self._delimiter)
        d = self.dict
        for n in nodes:
            if n not in d:
                return False
            d = d[n]
        return True

    def __eq__(self, other: Union[dict, ndict]) -> bool:
        other = ndict(other)
        return self.flatten_dict == other.flatten_dict

    def __str__(self) -> str:
        return yaml.dump(self.dict, sort_keys=False, indent=2)

    def __repr__(self) -> str:
        return f"<Nested dictionary of {len(self)} leaves.>: {self.dict}"

    def _get_node(self, path: Union[str, list[str]], dict_as_ndict: bool) -> Any:
        """Return the value of a particular path.

        Return
            Node value. If the node is a dictionary, __class__(node) will be returned.
        """
        if isinstance(path, list):
            path_list = path
            path = self.delimiter.join(path)
        elif isinstance(path, str):
            path_list = path.split(self.delimiter)
        else:
            raise ValueError(f"Unexpected path type: {type(path)}")

        v = reduce(getitem, path_list, self._d)

        if isinstance(v, dict) and dict_as_ndict:
            states = {
                "dict": v,
                "flatten_dict": self._get_flatten_dict_of_subtree(path),
                "delimiter": self.delimiter,
            }
            return ndict(delimiter=self.delimiter).load_state_dict(states)
        else:
            return v

    def _get_flatten_dict_of_subtree(self, prefix: str) -> dict[str, Any]:
        prefix = f"{prefix}{self.delimiter}"
        return deepcopy(
            {
                path[len(prefix) :]: value
                for path, value in self.flatten_dict.items()
                if path.startswith(prefix) and len(path) >= len(prefix)
            }
        )

    def _flatten(self) -> dict[str, Any]:
        def flatten_action(tree: dict, res: dict, node: Any, path: str, depth: int) -> None:
            if not isinstance(node, dict):
                res[path] = node

        res = {}
        traverse(self.dict, res, flatten_action)
        return res
