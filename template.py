import os
from pathlib import Path

project_name = "src"

list_of_files = [

    f"{project_name}/market_orders.py",
    f"{project_name}/limit_orders.py",
    f"{project_name}/stop_limit.py",
    f"{project_name}/grid_orders.py",
    f"{project_name}/utils.py",
    f"{project_name}/logger.py",
    f"{project_name}/advanced/oco.py",  
    f"{project_name}/advanced/twap.py",
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")