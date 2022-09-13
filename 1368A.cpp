#include <iostream>
using namespace std;
int main() {
    int a;
    cin>>a;
    for (int i=0;i<a;i++){
        int b,c,d,x=0;
        cin>>b>>c>>d;
        while (b<=d&&c<=d){
            if(b<c){
                b+=c;
            }
            else{
                c+=b;
            }
            x++;
        }
        cout<<x<<endl;
    }
}
