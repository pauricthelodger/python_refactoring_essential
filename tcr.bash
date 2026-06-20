git add .
uv run python -m pytest && git commit -m "It works!" || git reset --hard
