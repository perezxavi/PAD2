"""
Implementation of the 'Bucket' class. To determine which attributes to define, we ask ourselves what characteristics buckets have
 (just as we did with the PlainCat class). All buckets have a certain capacity, a color, are made of a certain material 
 (plastic, brass, etc.), and may or may not have a handle. A bucket is made for holding liquid; therefore, another characteristic
is the number of liters of liquid it contains at any given moment.

For now, we are only interested in knowing the maximum capacity (which cannot change) and the liters that the bucket contains at
any given moment, so those will be the attributes we take into account.

In this example, we use the magic method __str__() to visually represent the bucket and __repr__() for the canonical representation
of the object.


Date: 15/09/2023.
"""

class Bucket:

    def __init__(self, capacity, content=0):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError(f"The bucket's capacity must be a positive integer, received {capacity}")
        self.__capacity = capacity
        self.content = content

    @property
    def capacity(self):
        return self.__capacity

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if not isinstance(value, int) or value < 0 or value > self.capacity:
            raise ValueError(f"The bucket's content must be a positive integer and less than or equal to its capacity, received {value}")
        self.__content = value

    def empty(self):
        self.content = 0

    def fill(self):
        self.content = self.capacity

    def dump_in(self, destination):
        """
        Dumps the contents of one bucket into another. Before pouring the water, it checks how much the destination bucket can hold.
        """
        if not isinstance(destination, Bucket):
            raise TypeError(f"A bucket can only be poured into another bucket, received {destination}")
        free_capacity_at_destination = destination.capacity - destination.content
        if self.content <= free_capacity_at_destination:
            destination.content += self.content
            self.empty()
        else:
            self.content -= free_capacity_at_destination
            destination.fill()

    def __str__(self):
        """
        Returns a string with the bucket drawn. The edges of the bucket are displayed with the character # and the water it contains with the character ~
        """
        bucket_str = ""
        for _ in range(self.capacity, self.content, -1):
            bucket_str += "#          #\n"
        for _ in range(self.content, 0, -1):
            bucket_str += "#~~~~~~~~~~#\n"
        bucket_str += "############"
        return bucket_str

    def __repr__(self):
        """
        Returns the canonical representation of the object, with this value, we should be able to construct the object.
        """
        return f"Bucket({self.capacity}, {self.content})"
