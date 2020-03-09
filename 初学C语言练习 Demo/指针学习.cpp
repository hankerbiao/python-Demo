
/*
		2018年2月23日20:23:17
				《指针》
		
		指针其实是一个整形变量,与其它数据不同的是,它的作用是用来存储其它变量的地址,比如说
		int a;
		int *p = &a;
		这里面,a是普通的整形变量,p则是指针,用来存储变量a的地址,
		这样做的话,就可以很容易的找到变量a所在的位置,从而得到a的值
	
	
	1. 什么是指针
	   1.1 常量：不能改变的
		   变量：可以随便修改的 随便赋值
		   想去查看一个变量的地址： & 取地址运算符
		   
	指针类型变量
		char*, short*, int*, long*, flooat*, double*




*/



# include <stdio.h>

int main(void)
{
	int a = 10;
	int b = 5;
	printf("a = %d\n",a);
	printf("b = %d\n",b);
	printf("a = %d\n",&a);
	printf("b = %d\n",&b);

													//printf("%d %d",&a,&b);	查看 a，b地址 
	int* pa = &a;
	int* pb = &b;
	//2.通过指针读取变量
	printf("pa = %d\n", pa);//* ： 解析引用符（*pa 看做 a）
	printf("pb = %d\n", pb);
	//3.通过指针来就该变量
	*pa = 10;
	*pb = 11;
	printf("a = %d\n",a);
	printf("b = %d\n",b);

	//4.指针能不能改变指向？
	pa = &b;
	printf("pa = %d\n",pa);

	*pa = 45;
	printf("a = %d\n", a);
	printf("b = %d\n", b);

	pa = pb;
	printf("a = %d\n", pa);
	printf("b = %d\n", pb);

	//指针的赋值
	pa = (int *)51561561;  //地址就是一个整数值 指针占四个字节
	printf("%d\n",pa);

	//指针高级
	//数组？数组是什么？  ：存储数据的仓库（0，5,8,9，‘a’“happy”）
	//指针和数组的关系？
	int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }; // 一维数组
	//数组名： arr代表什么意思？数组名 数组的首地址，（地址 ：指针）
	printf("数组的首地址：%d\n",arr);
	// arr  到底是什么类型呢









	return 0;
}

//     去你爹的   这都啥？