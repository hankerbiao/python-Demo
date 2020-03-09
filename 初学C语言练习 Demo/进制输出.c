/*
	2018年2月13日13:59:56
	目的：
	测试 %d，%x,%#X，%#x的用法
*/

# include<stdio.h>

int main(void)
{
	int i=64;

	printf("%d\n",i);//%d，以十进制格式输出
	printf("%x\n",i);//%x 以十六进制格式输出
	printf("%#o\n",i);//%o 结果为 0100，以八进制格式输出
	printf("%#X\n",i);//结果为 OX40
	printf("%#x\n",i);


	return 0;
}

/*
结果

  以0开头  八进制
  OX开头   十六进制
*/
