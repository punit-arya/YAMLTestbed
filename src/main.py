import yaml
import json

yamlDocument = \
"""
---
- item    : Super Hoop
  quantity: 1
- item    : Basketball
  quantity: 4
- item    : Big Shoes
  quantity: 1
"""
deserialized = yaml.load(yamlDocument, None)
print(json.dumps(deserialized, indent = 4))
