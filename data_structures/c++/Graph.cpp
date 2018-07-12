#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Vertex
{
public:
	string name;
	map<string, int> neighbors;

	Vertex() {};
	Vertex(string n) : name(n) {};

	void add_neighbors(string v, int weight)
	{
		neighbors.insert(pair<string, int>(v, weight));
	}

};


class Graph
{
public:
	map<string, Vertex> vertices;

	Graph() {};

	void add_vertex(string v)
	{
		vertices.insert(pair<string, Vertex>(v, Vertex(v)));
	}
	void add_edge(string u, string v, int weight)
	{
		if (vertices.find(u) != vertices.end() && vertices.find(v) != vertices.end()) {
			vertices[u].add_neighbors(v, weight);
			vertices[v].add_neighbors(u, weight);
		}
	}

	void printNeighbors(string v)
	{
		for (auto& t : vertices[v].neighbors)
			std::cout << t.first << " : " << t.second << ", ";
	}

	void printGraph()
	{

		for (auto& t : vertices) {
			std::cout << t.first << " = ";
			printNeighbors(t.first);
			std::cout << "\n";
		}
	}
};

int main()
{
	Graph g;
	g.add_vertex("A");
	g.add_vertex("B");
	g.add_vertex("C");
	g.add_edge("A", "B", 1);
	g.add_edge("A", "C", 2);
	g.add_edge("C", "B", 3);
	g.printGraph();
}