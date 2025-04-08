"""Examples of set and dictionary syntax"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

    ice_cream.pop("strawberry")
