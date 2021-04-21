#include<iostream>
using namespace std;
int * ma()
{
int * a;
*a=10;
free(a);
return a;
}

int main()
{
	int* a=ma();
	cout<<a;
	return 0;
}
