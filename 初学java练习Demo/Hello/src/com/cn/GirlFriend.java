package com.cn;
abstract class GirlFriend {
	abstract void speak();
	abstract void cooking();	
}
class ChinaGirlFriend extends GirlFriend
{
	void speak()
	{
		System.out.println("���");		
	}
	void cooking() 
	{		
		System.out.println("ˮ����");
	}
}
class AmericaGirlFriend extends GirlFriend
{
	void speak()
	{
		System.out.println("hello");		
	}
	void cooking() 
	{		
		System.out.println("roast beef");
	}	
}
class Boy
{
	GirlFriend friend;
	void setGirlfriend(GirlFriend f)
	{
		friend = f;
	}	
	void showGirlFriend()
	{
		friend.speak();
		friend.cooking();
	}

}

 

