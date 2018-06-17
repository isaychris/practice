#include <iostream>
#include <string>

template <class T>
class Node
{
public:
	Node();
	Node(T data)
	{
		this->data = data;
		this->next = nullptr;
	}

	T data;
	Node * next;
};

template <class T>
class LinkedList
{
public:
	Node<T> * head;

	LinkedList()
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

	void addBack(T data)
	{
		Node<T> * new_node = new Node<T>(data);

		if (isEmpty()) {
			head = new_node;
			return;
		}

		Node<T> * p = head;
		while(p->next != nullptr) {
			p = p->next;
		}

		p->next = new_node;
	}

	void deleteBack()
	{
		Node<T> * p = head;
		Node<T> * lag = head;

		if (isEmpty()) {
			return;
		}

		while (p->next != nullptr) {
			lag = p;
			p = p->next;
		}
		
		delete p;
		lag->next = nullptr;
	}
	void deleteFront()
	{
		Node<T> * p = head->next;
		delete head;

		head = p;
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
	bool search(T data)
	{
		Node<T> * p = head;
		while(p != nullptr) {
			if(p->data == data) {
				std::cout << "[Success] '" + data << "' was found." << std::endl;
				return true;
			}
			p = p->next;
		}
		std::cout << "[Error] '" + data << "' was not found." << std::endl;
		return false;
	}
	void reverse()
	{
		Node<T> * current = head;
		Node<T> * prev = nullptr;
		Node<T> * next = nullptr;

		while (current != nullptr) {
			next = current->next;
			current->next = prev;
			prev = current;
			current = next;
		}

		head = prev;
	}
};

int main()
{
	LinkedList<std::string> LL;
	LL.addBack("Hey");
	LL.addBack("Hello");
	LL.addBack("World");
	LL.addBack("!");
	LL.deleteFront();
	LL.deleteBack();
	LL.reverse();
	LL.traverse();

	return 0;
}