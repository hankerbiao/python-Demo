/*
		2018年3月7日16:35:30

		for的循环使用

  从一加到一百


*/


# include<stdio.h>

int main(void)
{
	int i,sum;
	sum = 0;
	for(i = 1; i <= 100; i++)
		sum = sum + i;

	printf("%d",sum);


    return 0;
}