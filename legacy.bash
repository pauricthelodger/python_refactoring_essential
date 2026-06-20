echo Running ShippingApp for multiple orders...
echo

for I in 1001 1002 1003 1004; do
    echo ============================
    echo Running order ID: $I
    echo ============================

    uv run python -m legacy_code.src.ShippingApp $I

    echo
done

echo Done.
