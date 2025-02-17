import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

categories = {
    'Electronics': ['smartphone', 'screen', 'memory', 'battery'],
    'Apparel': ['t-shirt', 'jeans', 'jacket', 'cotton'],
    'Home & Kitchen': ['kitchen', 'knife', 'steel', 'cookware']
}

def tag_products(descriptions, categories):
    tagged_products = []
    for description in descriptions:
        tag = 'Uncategorized'  
        for category, keywords in categories.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE):
                    tag = category
                    break
            if tag != 'Uncategorized':
                break
        tagged_products.append((description, tag))
    return tagged_products

tagged_products = tag_products(descriptions, categories)

for description, tag in tagged_products:
    print(f"Description: '{description}' -> Tag: '{tag}'")
