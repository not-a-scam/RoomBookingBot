import json
import os
import config

GROUP_ID_FILE = "./data/group_id.json"

def save_group_id(group_id):
    with open(GROUP_ID_FILE, "w") as f:
        json.dump({"RBC_GRP_ID": group_id}, f)

def load_group_id():
    if not os.path.exists(GROUP_ID_FILE):
        return config.TEST_GRP_ID
    with open(GROUP_ID_FILE, "r") as f:
        data = json.load(f)
        return data.get("RBC_GRP_ID")
