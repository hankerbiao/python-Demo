/*
			�� 1 - 100 ֮�������ܱ�3��������֮��
				for �� if ��Ƕ��ʹ��
*/

# include<stdio.h>

int main()
{
	int i;
	int sum = 0;
	
	for(i = 3; i <= 12; i++);
	{
		if(i%3 == 0)
		sum = sum + i;				//���i�ܱ�3����
			
	}
	printf("sum = %d\n",sum);	

   return 0;
}