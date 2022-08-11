def product_max(a, triplets):
    products = []
    for triplet in triplets:
        product = a[triplet[0]] * a[triplet[1]] * a[triplet[2]]
        products.append(product)

    return max(products)


slices = [(0, 1, 2), (1, 2, 4), (2, 4, 5)]
print(product_max([-3, 1, 2, -2, 5, 6], slices))
