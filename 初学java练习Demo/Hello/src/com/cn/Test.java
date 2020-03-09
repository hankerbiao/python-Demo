package com.cn;

public class Test {

	public static void main(String[] args) {
	
			GirlFriend girl = new ChinaGirlFriend();
			Boy boy = new Boy();
			boy.setGirlfriend(girl);
			boy.showGirlFriend();
			
			girl = new AmericaGirlFriend();
			boy.setGirlfriend(girl);
			boy.showGirlFriend();		
	}

}
