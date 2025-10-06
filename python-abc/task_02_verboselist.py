#!/usr/bin/python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {num_items} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        if not self:  # Handle empty list case for pop
            raise IndexError("pop from empty list")
        
        item_to_pop = self[index]
        print(f"Popped {item_to_pop} from the list.")
        return super().pop(index)

# Testing the VerboseList
if __name__ == "__main__":
    my_list = VerboseList()

    print("--- Testing append ---")
    my_list.append(10)
    my_list.append("hello")
    print(f"Current list: {my_list}\n")

    print("--- Testing extend ---")
    my_list.extend([20, 30, "world"])
    print(f"Current list: {my_list}\n")

    print("--- Testing remove ---")
    my_list.remove(10)
    try:
        my_list.remove(99)  # Attempt to remove a non-existent item
    except ValueError as e:
        print(f"Error: {e}")
    print(f"Current list: {my_list}\n")

    print("--- Testing pop ---")
    popped_item = my_list.pop()  # Pop last item
    print(f"Current list: {my_list}")
    popped_item = my_list.pop(0) # Pop item at index 0
    print(f"Current list: {my_list}\n")

    print("--- Testing pop on empty list ---")
    empty_list = VerboseList()
    try:
        empty_list.pop()
    except IndexError as e:
        print(f"Error: {e}")
