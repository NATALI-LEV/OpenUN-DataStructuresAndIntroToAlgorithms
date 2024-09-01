from FuncDHeap import DHeap
from InputInts import InputInts

"""
    The main file of the project! enjoy! :)
"""

def main():
    file_path = "integers.txt"
    d = InputInts.get_intput()
    heap_integers = InputInts.read_integers(file_path)

    d_heap = DHeap(len(heap_integers), d)

    for integer in heap_integers:
        d_heap.insert(integer)

    print("The Print of heap example:")
    print(d_heap)

    print()

    print(" Print of extract max heap:")
    extracted_elements = [str(d_heap.extract_max()) for _ in range(len(heap_integers))]
    print(" -> ".join(extracted_elements))

if __name__ == "__main__":
    main()
