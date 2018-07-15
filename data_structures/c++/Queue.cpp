#include <vector>
#include <iostream>
#include <string>

template <class T>
class Queue
{
public:
	std::vector<T> data;
	Queue() {};

	bool isEmpty()
	{
		return data.size() == 0;
	}

	void enqueue(T item)
	{
		data.insert(data.begin(),item);
	}

	void dequeue()
	{
		if (isEmpty()) {
			return;
		}

		data.pop_back();
	}

	T peek()
	{
		if(isEmpty()) {
			return 0;
		}

		return data.front();
	}

	void traverse()
	{
		if(isEmpty()) {
			std::cout << "Queue is empty." << std::endl;
			return;
		}

		for(int i = data.size() - 1; i >= 0; --i) {
			std::cout << data[i] << std::endl;
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