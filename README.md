#python-project8
MinMaxList Python Module
Overview
MinMaxList is a Python class designed to manage a list of elements with efficient access to both the smallest and largest values. It maintains a sorted list and provides methods to insert items, retrieve the maximum or minimum value, and print the current list.

Features
Sorted List Maintenance: Automatically keeps the list in sorted order upon insertion of new elements.
Dynamic Insertion: Inserts new elements into the list while maintaining the sorted order.
Max and Min Retrieval: Provides methods to retrieve and remove the maximum and minimum elements from the list.
Print Functionality: Offers a method to print the current state of the list.
Methods
__init__(self, initializeList)
Constructor for the MinMaxList class.

Parameters:
initializeList: A list of initial elements to populate the MinMaxList.
insertItem(self, item, printResult=False / True)
Inserts an item into the list.

Parameters:
item: The item to be inserted.
printResult (optional): A boolean flag. If set to True, the method will print the insertion details and the current state of the list.
getMax(self)
Retrieves and removes the maximum element from the list.

Returns: The maximum element, or None if the list is empty.
getMin(self)
Retrieves and removes the minimum element from the list.

Returns: The minimum element, or None if the list is empty.
printList(self)
Prints the current state of the list.

Requirements
This module requires Python 3.x.

