from pathlib import Path


def load_policy(file_path: str) -> str:
    """Load a policy from a text file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Policy not found: {file_path}")

    return path.read_text(encoding="utf-8")


def split_sections(policy_text: str) -> list[str]:
    """Split a policy into numbered sections."""

    sections = []
    current_section = []

    for line in policy_text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line[0].isdigit() and "." in line:
            if current_section:
                sections.append("\n".join(current_section))

            current_section = [line]
        else:
            current_section.append(line)

    if current_section:
        sections.append("\n".join(current_section))

    return sections