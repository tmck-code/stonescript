#!/usr/bin/env python3

import json

recipes = json.load(open('recipes.json'))

def get_ingredients(recipes, item, n):
    print(f'looking for {n} {item}')
    i = []
    for k, variations in recipes.items():
        if item == k:
            print(f'found {item=} {variations=}')
            for recipe in variations:
                v = {}
                print(f'checking {recipe=}')
                for ingredient in recipe:
                    found = get_ingredients(recipes, ingredient, n)
                    if isinstance(found, dict):
                        v.update(found)
                    else:
                        v[ingredient] = found
                i.append(v)

    return {item: i} if i else item


print(json.dumps(recipes, indent=2))
result = get_ingredients(recipes, 'Heavy Hammer', 1)
print(json.dumps(result, indent=2))

