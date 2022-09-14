#include<iostream>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a,b;
    cin>>a;
    for(int j=0;j<a;j++){
        cin>>b;
        int x[b];
        int s=0,c=0;
        for (int i=0;i<b;i++){
            int temp;
            cin>>temp;
            s+=temp;
            x[i]=temp;
        }
        double average=s/double(b);
        if (int(average)==average){
            for (int i=0;i<b;i++){
                if(x[i]>average){
                    c++;
                }
            }
            cout<<c<<"\n";
        }
        else{
            cout<<-1<<"\n";
        }
    }
}
