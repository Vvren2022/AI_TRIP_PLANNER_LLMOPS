import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "llmops"

list_of_files = [
    # ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",

    f"src/{project_name}/agents/__init__.py",
    f"src/{project_name}/agents/base_agent.py",
    f"src/{project_name}/agents/task_agent.py",

    f"src/{project_name}/tools/__init__.py",
    f"src/{project_name}/tools/search_tool.py",

    f"src/{project_name}/memory/__init__.py",
    f"src/{project_name}/memory/vector_store.py",

    f"src/{project_name}/prompts/__init__.py",
    f"src/{project_name}/prompts/system_prompt.txt",

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/agent_pipeline.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/constants/__init__.py",

    f"src/{project_name}/observability/__init__.py",
    f"src/{project_name}/observability/tracing.py",

    f"src/{project_name}/api/__init__.py",
    f"src/{project_name}/api/routes.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/helpers.py",

    "config/config.yaml",
    "params.yaml",
    "schema.yaml",

    "main.py",
    "app.py",

    "requirements.txt",
    "setup.py",
    "Dockerfile",

    "research/experiments.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
