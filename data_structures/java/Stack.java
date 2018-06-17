public class Stack {
    private final int size;
    private Object data[];
    private int top;

    public Stack(int size) {
        this.size = size;
        this.data = new Object[size];
        this.top = -1;
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public void push(Object element) {
        if (top > size - 1) {
            System.out.println("stack overflow");
            return;
        }

        data[++top] = element;
    }
    public Object pop() {
        if (top == -1) {
            System.out.println("stack underflow");
            return null;
        }
        Object temp = data[top--];
        return temp;
    }

    public Object top() {
        return data[top];
    }

    public int getSize() {
        return top + 1;
    }

    public void traverse() {
        if (top == -1) {
            System.out.println("stack is empty");
        }
        for (int i = 0; i <= top; ++i) {
            System.out.println(data[i]);
        }
    }
    public static void main(String[] args) {
        Stack s = new Stack(3);
        s.push(1);
        s.push(2);
        s.push(3);
        s.pop();
        s.traverse();
        s.top();
    }
}
