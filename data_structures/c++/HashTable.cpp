#include <iostream>
#include <string>

using namespace std;

class HashNode {
public:
    HashNode() {}
    HashNode(int k, string v)
    {
        this->key = k;
        this->value = v;
        this->next = NULL;
    }

    int key;
    string value;
    HashNode* next;
};

class HashTable {
public:
    int size;
    HashNode** table;

    HashTable() {}
    HashTable(int s) {
        this->size = s;
        this->table = new HashNode*[s];
        for (int i = 0; i < size; i++) {
            table[i] = NULL;
        }
    }

    int hash(int key) {
        int idx = key % this->size;
        return idx;
    }


    void insert(int key, string value) {
        int idx = this->hash(key);

        HashNode* temp = new HashNode(key, value);

        if (table[idx] == NULL) {
            this->table[idx] = temp;
            return;
        }

        HashNode* p = this->table[idx];

        while (p->next != NULL) {
            p = p->next;
        }

        p->next = temp;
    }

    void remove(int key) {
        int idx = this->hash(key);

        HashNode* prev = NULL;
        HashNode* current = this->table[idx];

        if (current != NULL && current->key == key) {
            table[idx] = current->next;
            return;
        }
        while (current != NULL && current->key != key) {
            prev = current;
            current = current->next;
        }

        if (current == NULL) {
            return;
        }

        prev->next = current->next;
    }

    string retrieve(int key) {
        int idx = this->hash(key);

        HashNode* p = this->table[idx];

        while (p != NULL) {
            if (p->key == key) {
                return p->value;
            }
            
            p = p->next;
        }

        return "Unable to find value";
    }
};

int main() {
    HashTable my_hash(10);

    my_hash.insert(2, "chris");
    my_hash.insert(115, "billy");
    my_hash.insert(15, "kevin");

    cout << my_hash.retrieve(115) << endl;
    cout << my_hash.retrieve(15) << endl;

    my_hash.remove(15);
    cout << my_hash.retrieve(15) << endl;
}