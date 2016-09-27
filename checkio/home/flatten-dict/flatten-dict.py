#!/usr/bin/env python
# -*- coding: utf-8 -*-

def flatten(data):
    if not isinstance(data, dict):
        return data
    result = {}
    for key in data.keys():
        children = flatten(data[key])
        if not isinstance(children, dict):
            result[key] = children
            continue
        for subkey in children.keys():
            result["/".join([key, subkey])] = children[subkey]
    return result or ""

if __name__ == "__main__":
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}

# EOF
