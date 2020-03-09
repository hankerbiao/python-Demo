/*
	\t 制表符
*/
#include<time.h>
# include<stdio.h>
# include<stdlib.h>
# include<conio.h>
# include<string.h>
# include<list.h>

//定义一个结构体  表示银行账户信息
typedef struct tagperson
{

	char szUsername[20];// 账号
	char szPassworld[7];// 密码
	char szAccountNumber[20]; //银行账号
	float fmoney;//定义钱

}person;

//链表 火车头--车厢1--车厢2
//定义一个节点
struct tagNode
{

	person per;//银行账户信息  数据域
	struct tagNode* pNext;  //指针域
	
}Node;

tagNode* g_pHead = NULL;


//开户
int CreatAccount();
//登录
int Login();
int main(void)
{
	system("color 2F"); // 控制台颜色
	//打印提示文字	
	printf("***************************************************************\n");
	printf("************************欢迎来到银行***************************\n");
	printf("***************************************************************\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t1.开户\t\t\t\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t2.登录\t\t\t\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t3.前台客户信息查询中心\t\t\t\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t4.请选择您的需求\t\t\t\n");
	printf("\t------------------------------------------\n");

	char ch = getch();
	switch (ch)

	{
	case '1':// 开户
		 CreatAccount();
		break;
	case 2: //登录
		Login();
		break;
	case 3://前台客户信息查询中心
		
		break;
	case 4://请选择您的需求
		
		break;
	}
	
	
	
	return 0;
}
//创建账户
int CreatAccount()
{
	char szUsername[20]; //存贮名字
	printf("请输入您的姓名：\n");
	scanf("%s", szUsername);//不要使用&   因为 szUsername是数组名 就是地址

	char szPassword[7];
	char szRePassword[7];
	printf("请设置您的银行卡新密码\n");
	scanf("%s", szPassword);
	
	printf("请再一次确认银行卡密码");
	scanf("%s",szRePassword);

	//判断两次密码是否一样；
	if (0 != strcmp(szPassword, szRePassword))
	{
		printf("两次密码输入不相等");
		return 0;

	}

	//随机生成银行卡账号 6228 4800 2827 8148 672
	//生成一个四位数随机数 1000 - 9999
	//rand()%10000 ==> 0 - 9999
	//rand()% 9000 ==> 0 - 8999
	//rand()%9000 + 1000 ==>	
	char szAccountNumber[20];
	srand((unsigned int)time(NULL));
	sprintf(szAccountNumber,"%d%d%d%d%d%d",
		rand() % 9000 + 1000,
		rand() % 9000 + 1000, 
		rand() % 9000 + 1000,
		rand() % 9000 + 1000, 
		rand() % 100, 
		rand() % 100
		);

	//钱
	Node *p = g_pHead;
	while (g_pHead != NULL && p->pNext = NULL)
	{
		p = p->pNext;

	}

	//开辟新节点
	Node* pNewNode = malloc((sizeof(Node)));
	strcpy(pNewNode->per.szUsername, szUsername);
	strcpy(pNewNode->per.szPassword, szRePassword);
	strcpy(pNewNode->per.szUsername, szUsername);
	strcpy(pNewNode->per.szAccountNumber, szAccountNumber);
	pNewNode -> per.fmoney = 0.0f;
	pNewNode->pNext = NULL;
	
	if (g_pHead == NULL)
	{
		g_pHead = pNewNode;

	}
	else
	{

		p->pNext = pNewNode;

	}





	printf("您的账户信息如下：\n");
	printf("\t姓名：%s\n", pNewNode->per.szUsername);
	printf("");
	
	
	system("pause");
	system("cls");
	
	return 1;//成功1 ， 失败0；

}

//登录

int Login()
{
	printf("***************************************************************\n");
	printf("************************欢迎来到银行***************************\n");
	printf("***************************************************************\n");


	char szAccountNum[20];




}
