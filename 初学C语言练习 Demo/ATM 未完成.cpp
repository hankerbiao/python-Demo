/*
	\t �Ʊ��
*/
#include<time.h>
# include<stdio.h>
# include<stdlib.h>
# include<conio.h>
# include<string.h>
# include<list.h>

//����һ���ṹ��  ��ʾ�����˻���Ϣ
typedef struct tagperson
{

	char szUsername[20];// �˺�
	char szPassworld[7];// ����
	char szAccountNumber[20]; //�����˺�
	float fmoney;//����Ǯ

}person;

//���� ��ͷ--����1--����2
//����һ���ڵ�
struct tagNode
{

	person per;//�����˻���Ϣ  ������
	struct tagNode* pNext;  //ָ����
	
}Node;

tagNode* g_pHead = NULL;


//����
int CreatAccount();
//��¼
int Login();
int main(void)
{
	system("color 2F"); // ����̨��ɫ
	//��ӡ��ʾ����	
	printf("***************************************************************\n");
	printf("************************��ӭ��������***************************\n");
	printf("***************************************************************\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t1.����\t\t\t\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t2.��¼\t\t\t\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t3.ǰ̨�ͻ���Ϣ��ѯ����\t\t\t\n");
	printf("\t------------------------------------------\n");
	printf("\t\t\t4.��ѡ����������\t\t\t\n");
	printf("\t------------------------------------------\n");

	char ch = getch();
	switch (ch)

	{
	case '1':// ����
		 CreatAccount();
		break;
	case 2: //��¼
		Login();
		break;
	case 3://ǰ̨�ͻ���Ϣ��ѯ����
		
		break;
	case 4://��ѡ����������
		
		break;
	}
	
	
	
	return 0;
}
//�����˻�
int CreatAccount()
{
	char szUsername[20]; //��������
	printf("����������������\n");
	scanf("%s", szUsername);//��Ҫʹ��&   ��Ϊ szUsername�������� ���ǵ�ַ

	char szPassword[7];
	char szRePassword[7];
	printf("�������������п�������\n");
	scanf("%s", szPassword);
	
	printf("����һ��ȷ�����п�����");
	scanf("%s",szRePassword);

	//�ж����������Ƿ�һ����
	if (0 != strcmp(szPassword, szRePassword))
	{
		printf("�����������벻���");
		return 0;

	}

	//����������п��˺� 6228 4800 2827 8148 672
	//����һ����λ������� 1000 - 9999
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

	//Ǯ
	Node *p = g_pHead;
	while (g_pHead != NULL && p->pNext = NULL)
	{
		p = p->pNext;

	}

	//�����½ڵ�
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





	printf("�����˻���Ϣ���£�\n");
	printf("\t������%s\n", pNewNode->per.szUsername);
	printf("");
	
	
	system("pause");
	system("cls");
	
	return 1;//�ɹ�1 �� ʧ��0��

}

//��¼

int Login()
{
	printf("***************************************************************\n");
	printf("************************��ӭ��������***************************\n");
	printf("***************************************************************\n");


	char szAccountNum[20];




}
