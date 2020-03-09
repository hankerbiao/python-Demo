/*
			求 1 - 100 之间所有能被3整除的数之和
				for 和 if 的嵌套使用
*/

# include<stdio.h>

int main()
{
	int i;
	int sum = 0;
	
	for(i = 3; i <= 12; i++);
	{
		if(i%3 == 0)
		sum = sum + i;				//如果i能被3整除
			
	}
	printf("sum = %d\n",sum);	

   return 0;
}