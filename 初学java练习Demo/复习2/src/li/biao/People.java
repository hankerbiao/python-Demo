package li.biao;

    class People {
	private String name;
	private int age;


	People(String n,int a){
		name = n;
		age = a;
		
	}

	public void show() {		
		System.out.println("�����ǣ�"+this.name+",�����ǣ�"+this.age);
	}

	public void sleep() {
		System.out.println("����");
	}
	
}
