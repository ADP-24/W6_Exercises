def get_supplier_code(part_code):
    return part_code.split(":")[0]

def get_product_num(part_code):
    return part_code.split(":")[1].split("-")[0]

def get_size(part_code):
    return part_code.split("-")[1]

part_code_1 = "ACME:123-L"
part_code_2 = "DI:12345-M"
part_code_3 = "ACE:1-12"

part_codes = [part_code_1, part_code_2, part_code_3]

for part_code in part_codes:
    supplier_code = get_supplier_code(part_code)
    product_num = get_product_num(part_code)
    size = get_size(part_code)

    print(f"Part Code: {part_code}")
    print(f"Supplier Code: {supplier_code}")
    print(f"Product Number: {product_num}")
    print(f"Size: {size}\n")