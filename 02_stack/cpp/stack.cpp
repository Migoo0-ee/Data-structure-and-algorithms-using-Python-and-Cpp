#include <iostream>
using namespace std ; 
const int MAX_SIZE = 100 ; 

class Stack {
    int top ; 
    int item[MAX_SIZE]; 
   
public : 
    Stack() : top(-1){} 

    bool isEmpty (){
        return top == -1 ;
    }

    bool isFull(){
        return top == MAX_SIZE -1 ; 
    }

    void push (int val){
        if(isFull()){
           cout << "Stack is Overwhelmed"; 
        }
        else {
            top ++ ; 
            item[top] = val ; 
        }
    }

    void pop (int&val){
        if (isEmpty()){
            cout << "Stack is Undeflow" ; 
        }
        else {
            val = item[top]; 
            top -- ; 
        }
    }

    void getTop () {
      cout << item[top] ; 
    }

    void getStack () {
       cout <<"Stack elements : ["; 
       for (int i=0; i <=top; i++){
           cout << item[i] << "," ; 
       }
       cout << "]\n" ; 
    }
}; 

int main() {
    Stack myStack;
    
    cout << "=== PUSHING ELEMENTS ===" << endl;
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    
    cout << "\n=== STATUS ===" << endl;
    myStack.getStack();
    myStack.getTop();
    
    cout << "\n=== POPPING ELEMENT ===" << endl;
    int poppedVal;
    myStack.pop(poppedVal);
    cout << "-> Popped Value: " << poppedVal << "\n";
    
    cout << "\n=== FINAL STATUS ===" << endl;
    myStack.getStack();
    myStack.getTop();
    return 0;
}