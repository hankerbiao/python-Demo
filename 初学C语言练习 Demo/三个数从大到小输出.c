/*
		2018��2��26��11:43:07
			�������Ӵ�С���


*/
# include<stdio.h>
# include<stdlib.h>
int main(void)
{	
	
	int a,b,c;
	int t;
		
	system("color 6F");

	printf("���������������ÿո���� ");
	scanf("%d %d %d",&a,&b,&c);
	
	if(a < b)
	{
		t = b;
		b = a;
		a = t;
	
	}
	if(a<c)
	{
		t = c;
		c = a;
		a = t;
	}
	if(b<c)
	{	
		t = b;
		b = c;
		c = t;
	
	}

	printf("%d %d %d\n",a,b,c);



    return 0;
}
