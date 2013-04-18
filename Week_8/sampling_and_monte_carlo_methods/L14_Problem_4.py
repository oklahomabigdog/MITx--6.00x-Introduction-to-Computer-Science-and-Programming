Hash table size = 10 buckets; number of unique insertions = 10
1. Expected average length of the list for each bucket =
    Answer: 1

Hash table size = 10 buckets; number of unique insertions = 20
2. Expected average length of the list for each bucket =
    Answer: 2

Hash table size = 10 buckets; number of unique insertions = 100
3. Expected average length of the list for each bucket =
    Answer: 10

4. Consider the class intDict, particulary the method getValue. If there are no collisions, what would the complexity of getValue be?
    Answer: O(1)

Obviously, the drawback of making a hash table so huge there's no collisions is the space required for the hash table. If a set has 10^9 elements, and each element takes up even just 1 byte of space, that's still a 1 GB hash table!
5. So let's reduce the number of buckets... to 1! What would the complexity of getValue be if n elements were hashed to the same bucket?
    Answer: O(n)