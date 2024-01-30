def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return len(common_elements)

def get_list_input():
    return list(map(int, input("Enter space-separated integers: ").split()))

def main():
    list1 = get_list_input()
    list2 = get_list_input()
    common_count = find_common_elements(list1, list2)
    print(f"Number of common elements: {common_count}")

if __name__ == "__main__":
    main()
