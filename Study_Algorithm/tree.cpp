#include <iostream>
#include <queue>

using namespace std;
// 이진 트리
struct node {
    string position;
    node* first; // 각각의 노드는 다른 두 개의 노드(하위노드) 에 대한 링크를 가진다.
    node* second;
};

struct org_tree{
    node* root;
    
    // 새로운 트리는 만드는 정적 함수 
    static org_tree create_org_structure(const std::string& pos) {
        org_tree tree;
        tree.root = new node {pos, NULL, NULL};
        return tree;
    }
    
    // 특정 원소를 찾기 위해 트리를 탐색
    static node* find(node* root, const std::string& value) {
        if(root == NULL) 
            return NULL;
        if (root->position == value) 
            return root;
        auto firstFound = org_tree::find(root->first, value);
        
        if (firstFound != NULL)
            return firstFound;
        return org_tree::find(root->second, value);
    }
    
    // 새로운 부하직원 추가하는 삽입 함수
    bool addSubordinate(const std::string& manager, const std::string& subordinate) {
        auto managerNode = org_tree::find(root, manager);
        
        if(!managerNode){
            cout << manager << "을 찾을 수 없습니다. " << endl;
            return false;
        }
        if(managerNode->first && managerNode->second) {
            cout << manager << " 아래에" << subordinate << "을 추가할 수 없습니다." << endl;
            return false;
        }
        if(!managerNode->first) 
            managerNode->first = new node {subordinate, NULL, NULL};
        else
            managerNode->second = new node {subordinate, NULL, NULL};
        cout << manager << " 아래에 " << subordinate << "을 추가 했습니다." << endl;
        return true;
    }
};

int main() {
    auto tree = org_tree::create_org_structure("CEO");
    
    tree.addSubordinate("CEO", "부사장");
    tree.addSubordinate("부사장", "IT부장");
    tree.addSubordinate("부사장", "마케팅부장");
    tree.addSubordinate("IT부장", "보안팀장");
    tree.addSubordinate("IT부장", "앱개발팀장");
    tree.addSubordinate("마케팅부장", "물류팀장");
    tree.addSubordinate("마케팅부장", "홍보팀장");
    tree.addSubordinate("부사장", "재무부장");
    return 0;
}
