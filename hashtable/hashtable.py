from linked_list import LinkedList
from linked_list import Node

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.resizingNewCapacity = 0
        self.itemsCount = 0
        self.resizingCount = 0
        self.loadFactor = self.itemsCount / self.capacity

        #self.table = [None] * capacity
        self.table = [LinkedList()] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        return self.itemsCount / self.capacity


    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        fnv_prime = 1099511628211
        offset_basis = 14695981039346656037

	    #FNV-1a Hash Function
        hash = offset_basis + seed

        for char in key:
            hash = hash ^ ord(char)
            hash = hash * fnv_prime
        
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def hash_index_for_new_capacity(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the NEW hash table.
        """
        return self.fnv1(key) % self.resizingNewCapacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        # Grab the slot were this item should be at
        slot = self.hash_index(key)
        # Grab the ll at this slot
        ll = self.table[slot]
        # Try to grab that node with this key
        node = ll.find(key)
        # If this node exists
        if node:
            # Change the value
            node.value = value
        # If it doesn't
        else:
            # Add to the head of this LL
            #new_node = Node(key, value)
            ll.insert_at_head(key, value)
            self.itemsCount += 1

    def put_on_resized_table(self, key, value, resized_table, new_capacity):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        # Grab the slot were this item should be at
        slot = self.hash_index_for_new_capacity(key)
        # Grab the ll at this slot
        ll = resized_table[slot]
        # Try to grab that node with this key
        node = ll.find(key)

        # If this node exists ( it shouldn't)
        #if node:
            # Change the value
            #node.value = value
        # If it doesn't
        #else:
            # Add to the head of this LL
        ll.insert_at_head(key, value)
        self.resizingCount += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        slot = self.hash_index(key)
        ll = self.table[slot]
        node = ll.find(key)

        if node:
            ll.delete(key)
            self.itemsCount -= 1
            return node
        else:
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        slot = self.hash_index(key)
        ll = self.table[slot]
        node = ll.find(key)

        if node:
            return node.value
        else:
            return None

    def check_if_table_needs_to_resize(self):
        # Check if the table needs to be resized
        if self.loadFactor > 0.7 and self.loadFactor < 0.2:
            # If it has too much items
            if self.loadFactor > 0.7:
                # Make the table bigger
                self.resizingNewCapacity = self.capacity * 2
                self.resize(self.resizingNewCapacity)


    def resize(self, new_capacity):
        new_table = [LinkedList()] * new_capacity
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        # Set resizingNewCapacity
        self.resizingNewCapacity = new_capacity
        # For each LL in the old table
        for ll in self.table:
            # Save the head in node
            node = ll.head
            # While node is not epty
            while node:
                # put this node in the new table
                self.put_on_resized_table(node.key, node.value, new_table, new_capacity)
                # Set node as the next node
                node = node.next
        # Set our Table as the resized table        
        self.table = new_table
        # Set item count
        self.itemsCount = self.resizingCount
        self.resizingCount = 0
        # Set capacity
        self.capacity = new_capacity
        self.resizingNewCapacity = 0       




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
