"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    """
    I used a set because it automatically removes duplicates, so it's easy to check 
    if anything repeats. The only operation here is turning the list into a set, 
    which goes through the list once.
    """
    return len(product_ids) != len(set(product_ids))


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        """
        I chose a list since it keeps tasks in order the way they were added. 
        Adding with append is quick and simple.
        """
        self.queue.append(task)

    def remove_oldest_task(self):
        """
        I remove from the front with pop(0) because that gives me the oldest task. 
        It's not the fastest way, but it works fine for small cases.
        """
        if self.queue:
            return self.queue.pop(0)
        return None


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        """
        I used a set so that I don't have to worry about duplicates. 
        Adding new values is straightforward.
        """
        self.unique_values.add(value)

    def get_unique_count(self):
        """
        Getting the count is just checking the size of the set. 
        It's a direct way to know how many unique numbers we've seen.
        """
        return len(self.unique_values)
