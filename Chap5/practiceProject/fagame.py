inventory = {"Arrows": 12, "Swords": 30, "Bombs": 2, "Shields": 40}
item_names = ["Arrows", "Swords", "Bombs", "Shields"]
def add_item(inv, itemsAdded):
    for item in itemsAdded:
        inv.setdefault(item, 0)
        inv[item] += 1
def count_items(inv):
    total_items = 0
    for name in inv.keys():
        total_items += count_item(inv, name)
    return total_items
def count_item(inv, item_name):
    return inv.get(item_name, 0)
def displayStuff(inv):
    for k, v in inv.items():
        print(f"{k}: {v}")
def main():
    itemsAdded = ["Nashor", "Arrow", "Shor", "Shor"]
    add_item(inventory, itemsAdded)
    displayStuff(inventory)

if __name__ == "__main__":
    main()
    