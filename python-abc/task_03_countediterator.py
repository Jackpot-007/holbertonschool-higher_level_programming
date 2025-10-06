#!/usr/bin/python3


class CountedIterator:
    """
    An iterator that extends a built-in iterator to keep track of the 
    number of items that have been iterated over.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable and sets the counter to zero.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Fetches the next item from the underlying iterator, increments the counter,
        and returns the item. Raises StopIteration if no more items exist.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def __iter__(self):
        """
        Returns the iterator itself, making it directly iterable.
        """
        return self

    def get_count(self):
        """
        Returns the current number of items that have been iterated over.
        """
        return self.count

if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    counted_iter = CountedIterator(my_list)

    print("Iterating through the CountedIterator:")
    for item in counted_iter:
        print(f"Fetched item: {item}, Current count: {counted_iter.get_count()}")

    print(f"\nFinal count after full iteration: {counted_iter.get_count()}")

    print("\nDemonstrating manual next calls:")
    another_list = ['a', 'b']
    manual_counted_iter = CountedIterator(another_list)

    try:
        print(f"Next item: {next(manual_counted_iter)}, Count: {manual_counted_iter.get_count()}")
        print(f"Next item: {next(manual_counted_iter)}, Count: {manual_counted_iter.get_count()}")
        print(f"Next item: {next(manual_counted_iter)}, Count: {manual_counted_iter.get_count()}")
    except StopIteration:
        print("StopIteration caught as expected.")
    
    print(f"Final count from manual iteration: {manual_counted_iter.get_count()}")
