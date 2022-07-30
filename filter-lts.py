#!/usr/bin/python3

import json
import sys

if len(sys.argv) != 3:
    print("Usage: filter-lts LTS-VER JSON-FILE")
    sys.exit(0)

LTS_VER = sys.argv[1]
JSON_FILE = sys.argv[2]

with open(JSON_FILE, "r", encoding="latin-1") as myfile:
    data = json.load(myfile)

if "releases" not in data:
    print("Unexpected releases.json format", file=sys.stderr)
    sys.exit(1)

stable_ver = ""
for release in data["releases"]:
    if release["iseol"]:
        continue
    if release["moniker"] != "longterm":
        continue
    ver = release["version"]
    if ver.startswith(f"{LTS_VER}."):
        stable_ver = ver

if not stable_ver:
    print(f"No version found for {LTS_VER} series", file=sys.stderr)
    sys.exit(1)

print(stable_ver)
