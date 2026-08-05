from __future__ import annotations

import os
import shutil
import sys

RESET = "\033[0m"
BOLD = "\033[1m"

FG_GOLD = "\033[38;5;214m"
FG_SKY = "\033[38;5;117m"
FG_MINT = "\033[38;5;79m"
FG_SLATE = "\033[38;5;250m"


def _use_color() -> bool:
	return sys.stdout.isatty() and os.getenv("TERM", "") != "dumb"


def _paint(text: str, color: str, enabled: bool) -> str:
	if not enabled:
		return text
	return f"{color}{text}{RESET}"


def _fit(text: str, width: int) -> str:
	if len(text) <= width:
		return text
	if width <= 3:
		return text[:width]
	return text[: width - 3] + "..."


def _build_banner() -> str:
	colors = _use_color()
	term_width = shutil.get_terminal_size(fallback=(100, 24)).columns
	term_width = max(72, min(term_width, 140))

	large_logo = [
		"     **      ******        *****    ******   **        **** ",
		"    ****       **         **        **   **  **      **     ",
		"   **  **      **    ===   ****     **   **  **      **     ",
		"  ********     **             **    **   **  **      **     ",
		" **      **  ******       *****     ******   ******    **** ",
	]
	compact_logo = ["ai-sdlc-python-template"]

	subtitle_1 = "ai-sdlc-python-template"
	subtitle_2 = "Cookiecutter scaffold with approval-gated workflow"

	# Keep rendering stable on narrower terminals to avoid border wrapping.
	use_large_logo = term_width >= 98
	content_lines = large_logo[:] if use_large_logo else compact_logo[:]
	if use_large_logo:
		content_lines = content_lines + ["", subtitle_1, subtitle_2]
	else:
		content_lines = content_lines + ["", subtitle_2]

	max_len = max(len(line) for line in content_lines)
	inner_width = min(max_len + 10, term_width - 2)
	inner_width = max(inner_width, 68)

	border = "*"
	top = _paint(border * (inner_width + 2), FG_GOLD, colors)
	rows = [top]

	for idx, raw in enumerate(content_lines):
		text = _fit(raw, inner_width - 2)
		centered = text.center(inner_width)
		if use_large_logo and idx < len(large_logo):
			styled = _paint(centered, f"{BOLD}{FG_SKY}", colors)
		elif raw == subtitle_1:
			styled = _paint(centered, f"{BOLD}{FG_MINT}", colors)
		elif raw == subtitle_2:
			styled = _paint(centered, FG_SLATE, colors)
		else:
			styled = centered
		rows.append(_paint(border, FG_GOLD, colors) + styled + _paint(border, FG_GOLD, colors))

	rows.append(top)
	return "\n" + "\n".join(rows) + "\n"


print(_build_banner())
