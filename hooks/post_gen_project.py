import shutil as sh

layout = "{{ cookiecutter.project_layout }}"
slug = "{{ cookiecutter.project_slug }}"

if layout == "src":
    sh.rmtree(slug)
    print(f"removed path {slug!r}")
elif layout == "flat":
    sh.rmtree("src")
    print("removed path 'src'")
