/*

1 - 100 之间所有奇数之和的平均数

  2018年3月8日12:02:39
*/

# include<stdio.h>

int main(void)
{
	int i;
	int sum = 0;
	int j = 0;
	int k;


	for(i = 1; i <= 100; i++)
	{
		if(i%2 != 0)
			j+= 1;
		sum = sum +i;
	
		}
	
	k = sum/j;
	printf("奇数的个数为：%d\n",j);
	printf("奇数之和为：%d\n",sum);
	printf("平均数为：%d\n",k);

    return 0;
}