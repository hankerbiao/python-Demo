package china.amazing;

	class Person {
		private String name;
		private int age;
		/*
		 * ����һ�����캯��������person�����ʼ�� 
		 *��ʽ��
		 *1.��������������ͬ
		 *2.û�з���ֵ����
		 *3.û�о���ķ���ֵ
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
			System.out.println("������"+this.name+"������"+this.age);		
		}
}