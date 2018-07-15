#include <iostream>

template <class T>
class Node
{
public:
	T data;
	Node * next;

	Node() {};
	Node(T data)
	{
		this->data = data;
		this->next = nullptr;
	}

};


template <class T>
class Queue
{
public:
	Node<T> * head;

	Queue()
	{
		head = nullptr;
	}

	bool isEmpty()
	{
		if (head == nullptr) {
			return true;
		}
		return false;
	}

	void enqueue(T item)
	{
		Node<T> * new_node = new Node<T>(item);

		if (isEmpty()) {
			head = new_node;
			return;
		}

		Node<T> * p = head;
		while (p->next != nullptr) {
			p = p->next;
		}

		p->next = new_node;
	}

	void dequeue()
	{
		if(isEmpty()) {
			std::cout << "Queue is empty." << std::endl;
 			return;
		}

		Node<T> * p = head->next;
		delete head;

		head = p;
	}


	T peek()
	{
		if (isEmpty()) {
			return NULL;
		}

		return head->data;
	}

	void traverse()
	{
		Node<T> * p = head;

		if (isEmpty()) {}
		while (p != nullptr) {
			std::cout << p->data << std::endl;
			p = p->next;
		}
	}
};

int main()
{
	Queue<int> q;
	q.enqueue(1);
	q.enqueue(2);
	q.enqueue(3);
	q.enqueue(4);
	q.dequeue();
	q.peek();
	q.traverse();

}