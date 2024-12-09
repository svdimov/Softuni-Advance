from hash_tables.hash_table import HashTable

hash_tables = HashTable(1)


for i in range(20):
    pairs = len(hash_tables)
    empty_p = hash_tables.capacity - pairs
    print(f"{pairs:>2}/{hash_tables.capacity:>2}",
          ('x' * pairs) + ("." * empty_p))
    hash_tables[i] = i