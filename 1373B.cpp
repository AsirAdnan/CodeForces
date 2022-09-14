#include<iostream>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a;
    cin>>a;
    for (int i=0;i<a;i++){
        string c;
        int x=0,y=0;
        cin>>c;
        for (int i=0;i<c.length();i++){
            if (c[i]=='0'){
                x++;
            }
            else{
                y++;
            }
        }
        if (min(x,y)%2==0){
            cout<<"NET\n";
        }
        else{
            cout<<"DA\n";
        }
    }
}
