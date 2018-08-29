public class LinkedList<T> {
    public Node<T> head;

    public LinkedList() {
        this.head = null;
    }

    public boolean isEmpty() {
        if (head == null)
            return true;
        return false;
    }

    public void addFront(T data) {
        Node<T> new_node = new Node<T>(data);

        if (head == null) {
            head = new_node;

            return;
        }

        new_node.next = head;
        head = new_node;
    }

    public void addBack(T data) {
        Node<T> new_node = new Node<T>(data);

        if (head == null) {
            head = new_node;

            return;
        }

        Node p = this.head;
        while(p.next != null) {
            p = p.next;
        }

        p.next = new_node;
    }

    public void deleteFront() {
        if(isEmpty()) {
            return;
        }

        head = head.next;
    }

    public void deleteBack() {
        if (isEmpty()) {
            return;
        }

        Node<T> p = head;
        Node<T> prev = head;

        while (p.next != null) {
            prev = p;
            p = p.next;
        }

        prev.next = null;
    }

    public void reverse() {
        Node<T> prev = null;
        Node<T> next = null;
        Node current = head;

        while(current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    public void traverse(){
        Node<T> p = head;
        while (p != null) {
            System.out.println(p.data);
            p = p.next;
        }
    }
    public static void main(String[] args) {
        LinkedList<String> LL = new LinkedList();
        LL.addBack("Hey");
        LL.addBack("Hello");
        LL.addBack("World");
        LL.addBack("!");
        LL.deleteFront();
        LL.deleteBack();
        LL.reverse();
        LL.traverse();
    }
}
