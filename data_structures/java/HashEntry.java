public class HashEntry<T> {
    public int key;
    public T value;
    public HashEntry<T> next;

    public HashEntry(int key, T value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}
