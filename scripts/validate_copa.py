"""Validate Copa package structure using Python 3.11+ standard library.

The YAML checks deliberately support this package's simple string-only format;
this is not a general YAML parser or a replacement for quick_validate.py.
No live Dynatrace, DQL execution, or Codex discovery is tested.
"""
from pathlib import Path
import json
import re
import sys
import tomllib
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/copa-observabilidad"
EXPECTED = {
    "copa_coordinador", "copa_infraestructura", "copa_servicios_trazas",
    "copa_dql", "copa_implementador", "copa_verificador",
}


def validate(root=ROOT):
    root = Path(root).resolve()
    skill = root / ".agents/skills/copa-observabilidad"
    errors = []
    names = set()
    paths = list((root / ".codex/agents").glob("*.toml"))
    for path in paths:
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            for field in ("name", "description", "developer_instructions"):
                if not isinstance(data.get(field), str) or not data[field].strip():
                    raise ValueError(f"missing nonempty field: {field}")
            if data["name"] in names:
                raise ValueError("duplicate agent name")
            names.add(data["name"])
            if data["name"] != path.stem:
                raise ValueError("agent name differs from filename")
        except (ValueError, OSError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    if not EXPECTED.issubset(names):
        errors.append(f"missing agents: {sorted(EXPECTED - names)}")

    try:
        content = (skill / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            raise ValueError("missing frontmatter")
        fields = {}
        for line in match[1].splitlines():
            key, sep, value = line.partition(":")
            if not sep or key in fields:
                raise ValueError("invalid or duplicate frontmatter field")
            fields[key] = value.strip()
        if fields.get("name") != skill.name:
            raise ValueError("skill name differs from folder")
        description = json.loads(fields.get("description", '""'))
        if not isinstance(description, str) or not description.strip():
            raise ValueError("missing description")
    except (ValueError, OSError) as exc:
        errors.append(f"SKILL.md: {exc}")

    try:
        lines = (skill / "agents/openai.yaml").read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "interface:":
            raise ValueError("expected interface mapping")
        interface = {}
        for line in lines[1:]:
            if not line.strip():
                continue
            match = re.fullmatch(r"  ([a-z_]+): (.+)", line)
            if not match or match[1] in interface:
                raise ValueError("invalid or duplicate interface field")
            value = json.loads(match[2])
            if not isinstance(value, str):
                raise ValueError("interface fields must be quoted strings")
            interface[match[1]] = value
        if not interface.get("display_name"):
            raise ValueError("missing display_name")
        if not 25 <= len(interface.get("short_description", "")) <= 64:
            raise ValueError("short_description must have 25-64 characters")
        if "$copa-observabilidad" not in interface.get("default_prompt", ""):
            raise ValueError("default_prompt must mention the skill")
    except (ValueError, OSError) as exc:
        errors.append(f"openai.yaml: {exc}")

    links = 0
    docs = list(root.rglob("*.md"))
    for path in docs:
        content = path.read_text(encoding="utf-8")
        if len(re.findall(r"^\s*```", content, re.M)) % 2:
            errors.append(f"{path.relative_to(root)}: unclosed code fence")
        # Only inspect markdown prose; code samples can contain literal link syntax.
        prose = re.sub(r"```.*?```", "", content, flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            relative, _, anchor = target.partition("#")
            resolved = (path.parent / unquote(relative)).resolve() if relative else path
            if not resolved.is_relative_to(root) or not resolved.is_file():
                errors.append(f"{path.relative_to(root)}: missing local target {target}")
                continue
            if anchor:
                headings = re.findall(r"^#+ (.+)$", resolved.read_text(encoding="utf-8"), re.M)
                slugs = [re.sub(r"[^\w\s-]", "", h.lower()).replace(" ", "-") for h in headings]
                if unquote(anchor) not in slugs:
                    errors.append(f"{path.relative_to(root)}: missing anchor {target}")
            links += 1
    return errors, {"agents": len(paths), "markdown_files": len(docs), "local_links": links}


if __name__ == "__main__":
    errors, counts = validate()
    for error in errors:
        print("ERROR:", error)
    print(json.dumps({"status": "FAIL" if errors else "PASS", **counts}, ensure_ascii=True))
    sys.exit(bool(errors))
