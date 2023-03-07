#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;

struct Node {
    char data;
    int freq;
    Node* left, * right;

    Node(char data, int freq) : data(data), freq(freq), left(nullptr), right(nullptr) {}

    ~Node() {
        delete left;
        delete right;
    }
};

struct Compare {
    bool operator()(Node* l, Node* r) {
        return l->freq > r->freq;
    }
};

void encode(Node* root, string str, unordered_map<char, string>& huffmanCode) {
    if (!root) {
        return;
    }

    if (!root->left && !root->right) {
        huffmanCode[root->data] = str;
    }

    encode(root->left, str + "0", huffmanCode);
    encode(root->right, str + "1", huffmanCode);
}

void buildHuffmanTree(string text) {
    unordered_map<char, int> freq;
    for (char c : text) {
        freq[c]++;
    }

    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (auto& pair : freq) {
        pq.push(new Node(pair.first, pair.second));
    }

    while (pq.size() != 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        Node* parent = new Node('\0', left->freq + right->freq);
        parent->left = left;
        parent->right = right;
        pq.push(parent);
    }

    Node* root = pq.top();
    unordered_map<char, string> huffmanCode;
    encode(root, "", huffmanCode);

    for (auto& pair : huffmanCode) {
        cout << pair.first << " " << pair.second << endl;
    }

    delete root;
}

int main() {
    string text = "hello world";
    buildHuffmanTree(text);
    return 0;
}
