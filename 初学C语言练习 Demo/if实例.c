/*
		2018��2��23��13:36:52

		if���÷�

*/







# include<stdio.h>

int main()
{
	float score;

	printf("���������Ŀ��Գɼ���");
	scanf("%f",&score);

	if(score > 100)
		printf("����");

	else if(score >= 90 && score <= 100)
		printf("����");

	else if(score >= 60 && score <= 90)
		printf("�ϸ�");

	else if(score < 60)
		printf("������");


    return 0;
}