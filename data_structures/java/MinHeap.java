import java.util.ArrayList;

public class MinHeap<T extends Comparable<T>> {
    public ArrayList<T> data;

    public MinHeap() {
        this.data = new ArrayList<T>();
    }

    public void swap(int idx1, int idx2) {
        T temp = data.get(idx1);
        data.set(idx1, data.get(idx2));
        data.set(idx2, temp);
    }

    public void heapifyUp() {
        int idx = data.size() - 1;

        while ((hasParent(idx)) && (data.get(getParent(idx)).compareTo(data.get(idx)) > 0)) {
            swap(idx, getParent(idx));
            idx = getParent(idx);
        }
    }

    public void heapifyDown() {
        int idx = 0;
        while (hasLeftChild(idx)) {
            int small_idx = getLeftChild(idx);
            if (hasRightChild(idx) && data.get(getRightChild(idx)).compareTo(data.get(getLeftChild(idx))) < 0) {
                small_idx = getRightChild(idx);
            }
            if (data.get(idx).compareTo(data.get(small_idx)) < 0) {
                break;
            }
            else {
                swap(idx, small_idx);
            }
            idx = small_idx;
        }
    }

    public void insert(T item) {
        data.add(item);
        heapifyUp();
    }

    public T extractMin() {
        T min = data.get(0);
        data.set(0, data.get((data.size() - 1)));
        data.remove(data.size() - 1);
        heapifyDown();
        return min;
    }

    public T peek() {
        if (isEmpty()) {
            return null;
        }

        return data.get(0);
    }

    public void traverse() {
        System.out.println(data);
    }

    public boolean isEmpty() {
        if (data.size() == 0) {
            System.out.println("Heap is empty.");
            return true;
        }
        return false;
    }

    public int getLeftChild(int idx) {
        return (2 * idx) + 1;
    }

    public int getRightChild(int idx) {
        return (2 * idx) + 2;
    }

    public int getParent(int idx) {
        return (idx- 1) / 2;
    }

    public boolean hasLeftChild(int idx) {
        return getLeftChild(idx) < data.size();
    }
    public boolean hasRightChild(int idx) {
        return getRightChild(idx) < data.size();
    }
    public boolean hasParent(int idx) {
        return getParent(idx) >= 0;
    }

    public static void main(String[] args) {
        MinHeap<Integer> my_heap = new MinHeap<Integer>();
        my_heap.insert(23);
        my_heap.insert(1);
        my_heap.insert(6);
        my_heap.insert(19);
        my_heap.insert(14);
        my_heap.insert(18);
        my_heap.insert(8);
        my_heap.insert(24);
        my_heap.insert(15);
        my_heap.traverse();

        while (!my_heap.isEmpty()) {
            System.out.println(my_heap.extractMin());
        }
    }
}
