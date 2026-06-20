git add .
uv run pytest && git commit -m "It works!" || git reset --hard
