from pathlib import Path
import shutil
import subprocess

root = Path.cwd()
license_choice = "{{ cookiecutter.license }}"
project_type = "{{ cookiecutter.project_type }}"
include_example = "{{ cookiecutter.include_example_code }}"
initialize_git = "{{ cookiecutter.initialize_git }}"
agent_provider = "{{ cookiecutter.agent_provider }}"

agent_skills_paths = {
    "claude": ".claude/skills",
    "codex": ".codex/skills",
    "gemini": ".gemini/skills",
    "cursor": ".cursor/skills",
}
agent_skills_path = agent_skills_paths.get(agent_provider, ".agents/skills")

license_files = {
    "MIT": "LICENSE-MIT",
    "BSD-3-Clause": "LICENSE-BSD-3-Clause",
    "GPL-3.0-or-later": "LICENSE-GPL-3.0-or-later",
}
for filename in license_files.values():
    path = root / filename
    if filename == license_files.get(license_choice):
        path.rename(root / "LICENSE")
    elif path.exists():
        path.unlink()

if license_choice == "No license":
    for filename in license_files.values():
        (root / filename).unlink(missing_ok=True)

if project_type == "application":
    (root / "src" / "{{ cookiecutter.package_name }}" / "cli_library.py").unlink(missing_ok=True)
else:
    (root / "src" / "{{ cookiecutter.package_name }}" / "cli_application.py").unlink(missing_ok=True)

if include_example == "no":
    for filename in ["cli_application.py", "cli_library.py"]:
        (root / "src" / "{{ cookiecutter.package_name }}" / filename).unlink(missing_ok=True)
    (root / "tests" / "test_example.py").unlink(missing_ok=True)

default_skills_dir = root / ".agents" / "skills"
target_skills_dir = root / agent_skills_path
if target_skills_dir != default_skills_dir and default_skills_dir.exists():
    target_skills_dir.parent.mkdir(parents=True, exist_ok=True)
    default_skills_dir.rename(target_skills_dir)
    default_skills_dir.parent.rmdir()

for path in root.rglob("*"):
    if not path.is_file() or path.suffix in {".pyc", ".png"}:
        continue
    try:
        text = path.read_text()
    except UnicodeDecodeError:
        continue
    updated = text.replace("__AGENT_SKILLS_PATH__", agent_skills_path)
    updated = updated.replace(".agents/skills", agent_skills_path)
    if updated != text:
        path.write_text(updated)

if initialize_git == "yes":
    try:
        subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Warning: Git repository initialization was skipped.")

shutil.rmtree(root / ".template", ignore_errors=True)
