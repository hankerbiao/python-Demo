/*

1 - 100 ֮����������֮�͵�ƽ����

  2018��3��8��12:02:39
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
	printf("�����ĸ���Ϊ��%d\n",j);
	printf("����֮��Ϊ��%d\n",sum);
	printf("ƽ����Ϊ��%d\n",k);

    return 0;
}