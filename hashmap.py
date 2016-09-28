#this function creates an empty list and then populates it with 256 empty lists (buckets)
def new(num_buckets=256):
    """Initiliazes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

# this function returns the hash value of the key that it takes as an argument allowing for quick dictionary lookups. 
def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to a an index for the aMap's buckets."""
    return hash(key) % len(aMap)

# this function uses the hash key function to navigate to the bucket stored in the hashmap and returns that bucket
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v 
    # the aMap is a list of lists.
    # this will iterate through that list and enumerate each item
    # how does the k, v = kv attribution fully work in the for loop?
    
    return -1, key, default 
    # this only returns if the key is not found in the particular bucket

def get(aMap, key, default=None):
    """Gets the value in a bucket for a given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing the existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    
    if i >= 0:
        #the key exists, replace it
        bucket[i] =  (key, value)
    else:
        #the key does not exist, append to create it
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

