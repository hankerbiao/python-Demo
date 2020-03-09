/*
			2018年2月25日17:33:49

				两个数互换



*/


/*
# include<stdio.h>

int main(void)
{
	int a,b,c;

	printf("请输入两个数");
	scanf("%d %d",&a,&b);
	c = a;
	a = b;
	b = c;

	printf("a = %d, b = %d \n",a,b);


    return 0;
}
*/

/*
				求两个数中的最大数

*/

# include<stdio.h>

int main(void)
{
	int a,b;
	printf("请输入两个数：");
	scanf("%d %d",&a,&b);
	if(a > b)
	
	printf("最大数为：%d",a);
		else
	printf("最大数为：%d",b);
	


    return 0;
}