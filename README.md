Immutable_Map

Implement an Immutable Mapping Type
Objective: Create a custom immutable mapping type in Python, named ImmutableMap. This type should behave like a dictionary but be immutable – once created, its contents cannot be changed.
Requirements:
1.Inheritance or Duck Typing:
  Your ImmutableMap can either inherit from the appropriate ABCs in collections.abc or use duck typing to   implement the required methods.
2.Implements Sized, Iterable, Container, and Mapping:
  Sized: Implement a method to return the number of items in the mapping.
  Iterable: Implement a method to allow iteration over the mapping’s items (key-value pairs).
  Container: Implement a method to check if a key is in the mapping.
  Mapping: Implement methods to access items and support other dictionary-like behaviors, except for mutable operations.
3.Immutable Design:
  Ensure that once an ImmutableMap instance is created, it cannot be modified. Attempts to modify the map (like adding or removing items) should raise appropriate exceptions.
4.Constructor:
  The constructor of ImmutableMap should take an initial set of key-value pairs and store them. This can be in the form of another mapping (like a dictionary) or iterable key-value pairs.
5.Additional Methods (Optional):
  For extra credit, implement methods like keys(), values(), and items(), similar to a standard Python dictionary.
6.Testing:
  Write test cases to verify that your ImmutableMap behaves correctly. Ensure tests cover creation, proper implementation of the Mapping interface, and immutability.
