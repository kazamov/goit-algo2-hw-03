import csv
from BTrees.OOBTree import OOBTree
import timeit

tree = OOBTree()
items_dict = {}

def add_item_to_tree(item):
    id = (float(item['Price']), int(item['ID']))
    item = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': float(item['Price'])
    }
    tree.update({id: item})

def add_item_to_dict(item):
    items_dict[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': float(item['Price'])
    }

def range_query_tree(min_price, max_price):
    return list(tree.items((min_price,), (max_price,)))

def range_query_dict(min_price, max_price):
    result = []
    for _id, data in items_dict.items():
        if min_price <= data['Price'] <= max_price:
            result.append(data)
    return result

def run_task2():
    with open('./src/generated_items_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            add_item_to_tree(row)
            add_item_to_dict(row)

    t_tree = timeit.timeit(
        stmt="range_query_tree(10, 100)",
        globals=globals(),
        number=100
    )
    t_dict = timeit.timeit(
        stmt="range_query_dict(10, 100)",
        globals=globals(),
        number=100
    )

    print(f"Total range_query time for OOBTree: {t_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {t_dict:.6f} seconds")

if __name__ == "__main__":
    run_task2()