package test;


import java.util.Scanner;

class proceeding {
	Employee[] list = new Employee[5];
	int count = 0;

	public void add() {
		System.out.println("请输入员工的ID、姓名、性别、出生日期（年月日中间用空格隔开）、籍贯、学历、职称、工资、家庭住址、电话等、职务、类型（机关、教师、实验室、研究员等）");
		Employee em = new Employee();
		list[count] = em;
		count++;
	}

	public void travel() {
		for (int i = 0; i < count; i++) {
			System.out.println(list[i]);
		}
	}

	public void search() {
		int in = 0;
		System.out.println("请选择查询功能：id查询请按1，职工类型查询请按2");
		Scanner input = new Scanner(System.in);
		in = input.nextInt();
		switch (in) {
		case 1:
			System.out.print("请输入所要查询员工的id：");
			int on = 0;
			Scanner input1 = new Scanner(System.in);
			on = input1.nextInt();
			for (int i = 0; i < count; i++) {
				if (list[i].id == on) {
					System.out.println(list[i]);
					return;
				}
			}
			System.out.println("您输入的员工id不存在");
			break;
		case 2:
			System.out.print("请输入所要查询员工的类型：");
			String on1=null;
			Scanner input2 = new Scanner(System.in);
			on1 = input2.next();
			for (int i = 0; i < count; i++) {
				if (on1.equals(list[i].type)) {
					System.out.println(list[i]);
					return;
				}
			}
			System.out.println("您输入的员工类型不存在");
			break;
		default:
			System.out.println("您的指令输入错误，请用心考虑后再重新输入");
			break;
		}
	}

	public void modify() {
		System.out.print("请输入所要修改员工的id：");
		int on = 0;
		Scanner input = new Scanner(System.in);
		on = input.nextInt();
		for (int i = 0; i < count; i++) {
			if (list[i].id == on) {
				Employee em = new Employee();
				list[i] = em;
				System.out.println("员工信息修改成功：");
				System.out.println(list[i]);
				return;
			}

		}
		System.out.println("您输入的员工id不存在");

	}

	public void delete() {
		System.out.print("请输入所要修改员工的id：");
		int on = 0;
		Scanner input = new Scanner(System.in);
		on = input.nextInt();
		for (int i = 0; i < count; i++) {
			if (list[i].id == on) {
				list[i] = list[i + 1];
				list[count] = null;
				count--;
				System.out.println("员工信息删除成功：");
				return;
			}

		}
		System.out.println("您输入的员工id不存在");
	}

	void sort() {
		System.out.println("请选择排序方式:1 按ID排序 2 按类型排序");
		int a;
		Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		    Employee t;
		if (a == 1) {
		System.out.println("请选择排序方式:1 升序 2 降序");
		int b;
		b = sc.nextInt();
		if (b == 1) {
		for (int i = 0; i < count; i++) {
		for (int j = i + 1; j < count; j++) {
		if (list[i].id > list[j].id) {
		t = list[i];
		list[i] = list[j];
		list[j] = t;
		}
		}
		}
		} else if (b == 2) {
		for (int i = 0; i < count; i++) {
		for (int j = i + 1; j < count; j++) {
		if (list[i].id < list[j].id) {
		t = list[i];
		list[i] = list[j];
		list[j] = t;
		}
		}
		}
		}
		} else if (a == 2) {
		System.out.println("请选择排序方式:1 升序 2 降序");
		int b;
		b = sc.nextInt();
		if(b==1){
		for (int i = 0; i < count; i++) {
		for (int j = i + 1; j < count; j++) {
		if (list[i].typeNumber > list[j].typeNumber) {
		t = list[i];
		list[i] = list[j];
		list[j] = t;
		}
		}
		}
		}else if(b==2){
		for (int i = 0; i < count; i++) {
		for (int j = i + 1; j < count; j++) {
		if (list[i].typeNumber < list[j].typeNumber) {
		t = list[i];
		list[i] = list[j];
		list[j] = t;
		}
		}
		}
		}
		} else {
		System.out.println("排序方式输入错误，请重新输入");
		return;
		}
		for(int i=0;i<count;i++){
			System.out.println(list[i]);
		}
		}
}
