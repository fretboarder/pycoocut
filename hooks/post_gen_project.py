"""Cookiecutter hooks."""
import shutil as sh
from pathlib import Path

layout = "{{ cookiecutter.project_layout }}"
slug = "{{ cookiecutter.project_slug }}"
publish_workflow = "{{ cookiecutter.publish_workflow }}"

if layout == "src":
    sh.rmtree(slug)
    print(f"removed path {slug!r}")
elif layout == "flat":
    sh.rmtree("src")
    print("removed path 'src'")

if publish_workflow.lower() in ["0", "false", "f", "no", "n", "off"]:
    Path(".github/workflows/publish.yml").unlink()
    print("removed publish.yml workflow")
