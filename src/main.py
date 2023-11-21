import yaml
import json

yamlDocument = """
---
- item    : Super Hoop
  quantity: 1
- item    : Basketball
  quantity: 4
- item    : Big Shoes
  quantity: 1
"""
JSONned = ""
inputYAML = open("../var/")
deserialized = yaml.load(yamlDocument)
print(json.load(deserialized))
