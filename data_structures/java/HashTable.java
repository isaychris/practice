public class HashTable<T> {
    public int size;
    public HashEntry<T> [] table;

    public HashTable(int size) {
        this.size = size;
        this.table = new HashEntry[size];
    }

    public int hash(int key) {
        return key % size;
    }

    public void insert(int key, T value) {
        int idx = hash(key);

        HashEntry<T> temp =  new HashEntry(key, value);

        if (table[idx] == null) {
            table[idx]= temp;
            return;
        }

        HashEntry<T> p = table[idx];

        while(p.next != null) {
            p = p.next;
        }
        p.next = temp;
    }

    public T retrieve(int key) {
        int idx = hash(key);

        HashEntry<T> p = table[idx];
        while (p != null) {
            if (p.key == key) {
                return p.value;
            }

            p = p.next;
        }

        return null;
    }

    public void delete(int key) {
        int idx = hash(key);

        HashEntry<T> prev = null;
        HashEntry<T> current = table[idx];

        if (current != null && current.key == key)
        {
            table[idx] = current.next;
            return;
        }
        while (current != null && current.key != key)
        {
            prev = current;
            current = current.next;
        }

        if (current == null) {
            return;
        }

        prev.next = current.next;
    }

    public void display() {
        for (HashEntry<T> slot : table) {
            if (slot != null) {
                HashEntry<T> p = slot;

                while(p != null) {
                    System.out.print("[" + p.key + ", " + p.value + "]");
                    p = p.next;
                }
                System.out.println("");
            }
        }
    }
    public static void main(String[] args) {
        HashTable<String> my_hash = new HashTable(10);
        my_hash.insert(2, "chris");
        my_hash.insert(115, "billy");
        my_hash.insert(15, "kevin");
        my_hash.display();

        System.out.println(my_hash.retrieve(115));
        System.out.println(my_hash.retrieve(15));
        System.out.println(my_hash.retrieve(2));

        my_hash.delete(15);
        my_hash.display();
    }
}
