package test;


import java.util.Scanner;

class proceeding {
	Employee[] list = new Employee[5];
	int count = 0;

	public void add() {
		System.out.println("������Ա����ID���������Ա𡢳������ڣ��������м��ÿո�����������ᡢѧ����ְ�ơ����ʡ���ͥסַ���绰�ȡ�ְ�����ͣ����ء���ʦ��ʵ���ҡ��о�Ա�ȣ�");
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
		System.out.println("��ѡ���ѯ���ܣ�id��ѯ�밴1��ְ�����Ͳ�ѯ�밴2");
		Scanner input = new Scanner(System.in);
		in = input.nextInt();
		switch (in) {
		case 1:
			System.out.print("��������Ҫ��ѯԱ����id��");
			int on = 0;
			Scanner input1 = new Scanner(System.in);
			on = input1.nextInt();
			for (int i = 0; i < count; i++) {
				if (list[i].id == on) {
					System.out.println(list[i]);
					return;
				}
			}
			System.out.println("�������Ա��id������");
			break;
		case 2:
			System.out.print("��������Ҫ��ѯԱ�������ͣ�");
			String on1=null;
			Scanner input2 = new Scanner(System.in);
			on1 = input2.next();
			for (int i = 0; i < count; i++) {
				if (on1.equals(list[i].type)) {
					System.out.println(list[i]);
					return;
				}
			}
			System.out.println("�������Ա�����Ͳ�����");
			break;
		default:
			System.out.println("����ָ��������������Ŀ��Ǻ�����������");
			break;
		}
	}

	public void modify() {
		System.out.print("��������Ҫ�޸�Ա����id��");
		int on = 0;
		Scanner input = new Scanner(System.in);
		on = input.nextInt();
		for (int i = 0; i < count; i++) {
			if (list[i].id == on) {
				Employee em = new Employee();
				list[i] = em;
				System.out.println("Ա����Ϣ�޸ĳɹ���");
				System.out.println(list[i]);
				return;
			}

		}
		System.out.println("�������Ա��id������");

	}

	public void delete() {
		System.out.print("��������Ҫ�޸�Ա����id��");
		int on = 0;
		Scanner input = new Scanner(System.in);
		on = input.nextInt();
		for (int i = 0; i < count; i++) {
			if (list[i].id == on) {
				list[i] = list[i + 1];
				list[count] = null;
				count--;
				System.out.println("Ա����Ϣɾ���ɹ���");
				return;
			}

		}
		System.out.println("�������Ա��id������");
	}

	void sort() {
		System.out.println("��ѡ������ʽ:1 ��ID���� 2 ����������");
		int a;
		Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		    Employee t;
		if (a == 1) {
		System.out.println("��ѡ������ʽ:1 ���� 2 ����");
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
		System.out.println("��ѡ������ʽ:1 ���� 2 ����");
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
		System.out.println("����ʽ�����������������");
		return;
		}
		for(int i=0;i<count;i++){
			System.out.println(list[i]);
		}
		}
}
