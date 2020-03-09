/*
		2018年2月23日13:36:52

		if的用法

*/







# include<stdio.h>

int main()
{
	float score;

	printf("请输入您的考试成绩：");
	scanf("%f",&score);

	if(score > 100)
		printf("厉害");

	else if(score >= 90 && score <= 100)
		printf("优秀");

	else if(score >= 60 && score <= 90)
		printf("合格");

	else if(score < 60)
		printf("不及格");


    return 0;
}