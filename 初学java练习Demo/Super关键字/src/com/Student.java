package com;

public class Student {

	int number;
	String name;
	Student(){
	}
	Student(int number,String name)
	{		
		this.number = number;
		this.name = name;		
		System.out.println("我的名字是："+name+"学号是："+number);
	}
}


