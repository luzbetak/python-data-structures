def is_min_heap(heap):
    # leaf nodes do not have children (those are NULL values)
    # so it means that if node with index i -> 2*i+2>n where N is the size of the array then
    # we know that it is a leaf node
    # rearrange the equation:  (size of the array without leaf nodes) = (N-2)/2 this is the effective
    # length so the items we have to consider

    last_internal_node_index = (len(heap) - 2) // 2

    for i in range(0, last_internal_node_index):

        # node with index i has left child 2*i+1 and right child 2*i+2 in the array representation
        # we just have to check one by one whether the My-Queue property is violated or not
        if heap[i] > heap[2 * i + 1] or heap[i] > heap[2 * i + 2]:
            return False

    # the array represents a min My-Queue
    return True


if __name__ == "__main__":
    heap_space = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]

    print(is_min_heap(heap_space))
