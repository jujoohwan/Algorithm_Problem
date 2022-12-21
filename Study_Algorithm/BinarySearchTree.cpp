// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
struct node {
    int data;
    node* left;
    node* right;
};

struct bst {
    node* root = nullptr;
    
    // 삽입 함수를 만들기전에 find() 작성
    node* find(int value) {
        return find_impl(root, value);
    }
private:
    // 원소 찾는 find() 함수
    node* find_impl(node* current, int value) {
        if(!current) {
            cout << endl;
            return NULL;
        }
        
        if(current->data == value) {
            cout << value << "을 찾았습니다." << endl;
            return current;
        }
        
        if(value < current->data) {
            cout << current->data << "에서 왼쪽으로 이동: ";
            return find_impl(current->left, value);
        }
        cout << current->data << "에서 오른쪽으로 이동";
        return find_impl(current->right,value);
    }
    
    // 재귀적으로 하위 노드로 이동하면서 삽입할 부모 노드를 찾는다.
    void insert_impl(node* current, int value) {
        if (value < current->data) {
            if(!current->left) 
                current->left = new node {value, NULL,NULL};
            else
                insert_impl(current->left, value);
        } else {
            if(!current->right)
                current->right = new node {value, NULL, NULL};
            else
                insert_impl(current->right, value);
        }
    }
    // 중위 순회 로직
    void inorder_impl(node* start) {
        if(!start) 
            return;
        inorder_impl(start->left);
        cout << start->data << " ";
        inorder_impl(start->right);
    }
    // 원소 삭제 구현 함수
    node* delete_impl(node* start, int value){
        if(!start)
            return NULL;
        if(value < start-> data) 
            start->left = delete_impl(start->left, value);
        else if(value > start->data)
            start->right = delete_impl(start->right, value);
        else{
            // 왼쪽 자식이 없는 경우
            if(!start->left){
                auto tmp = start->right;
                delete start;
                return tmp;
            }
            // 오른쪽 자식이 없는 경우
            if(!start->right) {
                auto tmp = start->left;
                delete start;
                return tmp;
            }
            // 자식 노드가 둘다 있는 경우
            auto succNode = successor(start);
            start->data = succNode->data;
            
            //오른쪽 서브 트리에서 후속을 찾아 삭제
            start->right = delete_impl(start->right, succNode->data);
        }
        return start;
    }
    
public:
   
    void insert(int value){
        if(!root) {
            root = new node {value, NULL,NULL};
        } else {
            insert_impl(root,value);
        }
    }
    // 중위 순회  BST에서 중위 순회는 꽤 중요한 의미가 있다.
    void inorder() {
        inorder_impl(root);
    }
    
    // 후손노드를 찾아주는 함수
    node* successor(node* start) {
        auto current = start->right;
        while(current && current->left) 
            current = current->left;
        return current;
    }
    
    void deleteValue(int value) {
        root = delete_impl(root, value);
    }
};

int main() {
    bst tree;
    
    tree.insert(12);
    tree.insert(10);
    tree.insert(20);
    tree.insert(8);
    tree.insert(11);
    tree.insert(15);
    tree.insert(28);
    tree.insert(4);
    tree.insert(2);
    
    cout << "중위 순회: ";
    tree.inorder(); // BST 모든 원소가 오름차순으로 출력
    cout << endl;
    
    tree.deleteValue(12);
    cout << "12를 삭제한 후 중위 순회";
    tree.inorder();
    cout << endl;
    if(tree.find(12))
        cout << "원소 12는 트리에 있습니다." << endl;
    else 
        cout << "원소 12는 트리에 없습니다." << endl;
    return 0;
}
