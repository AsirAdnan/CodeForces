#include<iostream>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a;
    cin>>a;
    while(a--){
        int n,h,m,mini=25*60,z=0;
        cin>>n>>h>>m;
        while(n--){
            int x,y;
            cin>>x>>y;
            if (x==h){
                if (y==m){
                    mini=0;
                }
                else if (y>m){
                    z=y-m;
                }
                else{
                    z=(23*60)+(60-m+y);
                }
            }
            else if(x>h){
                if (y==m){
                    z=(x-h)*60;
                }
                else if (y>m){
                    z=((x-h)*60)+(y-m);
                }
                else{
                    z=((x-h-1)*60)+(60-m+y);
                }
            }
            else{
                if (y==m){
                    z=24*60-((h-x)*60);
                }
                else if (y>m){
                    z=(24*60-((h-x)*60))+(y-m);
                }
                else{
                    z=((24-h+x-1)*60)+(60-m+y);
                }
            }
            if (z<mini){
            mini=z;
        }
        }

        cout<<mini/60<<" "<<mini%60<<endl;
    }
}
