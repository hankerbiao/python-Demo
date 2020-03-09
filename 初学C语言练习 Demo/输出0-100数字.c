/*
		2018年2月21日10:45:07

		目标： 输出 0-100

*/

# include<stdio.h>

int main()
{
	int a = 0;      //！没有给a赋值 代码规范
	while(a <= 100) //！ 写了；
	{
		printf("%d \n",a);
		a++;
	}

	return 0;
}