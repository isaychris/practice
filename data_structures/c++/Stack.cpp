#include <iostream>
#include <string>

template<class T>
class Stack
{
private:
	int top;
	int size;
	T * data;

	bool isEmpty()
	{
		return top == -1;
	}

	bool isFull()
	{
		return top == size - 1;
	}

public:
	Stack(int size)
	{
		this->size = size;
		this->top = -1;
		this->data = new T[size];
	}

	void push(T element)
	{
		if (isFull())
			return;

		data[++top] = element;
	}

	void pop()
	{
		if(isEmpty())
			return;

		top--;
	}

	T peek()
	{
		if(isEmpty())
			return;

		return data[top];
	}

	void traverse()
	{
		if(isEmpty()) {
			std::cout << "stack is empty" << std::endl;
			return;
		}

		for(auto i = 0; i <= top; ++i) {
			std::cout << data[i] << std::endl;
		}
	}
};

int main()
{
	Stack<std::string> s(5);
	s.push("Hey");
	s.push("Hello");
	s.push("World");
	s.push("!");
	s.pop();
	s.traverse();

	return 0;
}