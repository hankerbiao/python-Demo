package china.amazing;

	class Person {
		private String name;
		private int age;
		/*
		 * 定义一个构造函数，来给person对象初始化 
		 *格式：
		 *1.函数名和类名相同
		 *2.没有返回值类型
		 *3.没有具体的返回值
		 * */		
		Person(String n,int a){
			name = n;
			age = a;
		}
			
		public void setName(String n){		
			name = n;
		}

		public String getName(){	
			return name;	
		}
		public void setAge(int a){
			age = a;
		}
		public int  getAge(){	
			return age;	
		}
		public void show()
		{		
			System.out.println("姓名是"+this.name+"年龄是"+this.age);		
		}
}