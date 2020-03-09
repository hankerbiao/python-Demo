package li.biao;

    class People {
	private String name;
	private int age;


	People(String n,int a){
		name = n;
		age = a;
		
	}

	public void show() {		
		System.out.println("名字是："+this.name+",年龄是："+this.age);
	}

	public void sleep() {
		System.out.println("呼呼");
	}
	
}
