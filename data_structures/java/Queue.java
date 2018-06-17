public class Queue {
    private Stack s1;
    private Stack s2;
    int front, rear;

    public Queue(int size) {
        this.s1 = new Stack(size);
        this.s2 = new Stack(size);
    }

    public void enqueue(Object element) {
        s1.push(element);
    }

    public Object dequeue() {
        if (getSize() == 0) {
            return null;
        }
        if (s2.isEmpty()) {
            while(!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }
        return s2.pop();
    }

    public int getSize() {

        return s1.getSize() + s2.getSize();
    }

    public Object peek() {
        if(getSize() == 0) {
            return null;
        }
        return s2.top();
    }
    public void traverse() {
        if (getSize() == 0) {
            System.out.println("Queue is empty");
            return;
        }
        s2.traverse();
    }
    public static void main(String[] args) {
        Queue q = new Queue(3);
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.dequeue();
        q.peek();
        q.traverse();
    }
}
