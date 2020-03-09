//强制类型转换

# include<stdio.h>

int main(void)
{
	int i;
	float sum = 0;

	for(i=1; i<=100; ++i)
	{
	
		sum = sum + 1/(float)(i);
	
	
	}
	printf("%f",sum);



    return 0;
}