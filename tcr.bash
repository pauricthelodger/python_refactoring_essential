git add .
uv run python -m unittest discover && git commit -m "It works!" || git reset --hard
