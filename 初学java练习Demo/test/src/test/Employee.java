package test;

import java.util.Scanner;

class Employee {
	/*ID���������Ա𡢳������ڡ����ᡢѧ����ְ�ơ����ʡ���ͥסַ���绰�ȡ�ְ�����ͣ����ء���ʦ��ʵ���ҡ��о�Ա�ȣ�*/
	int id;
	String name;
	String sex;
	MyDate birthday=new MyDate();
	String placeofbirth;
	String educationbackground;
	String professionaltitle;
	int salary;
	String home;
	String phonenumber;
	String position;
	String type;
	int typeNumber;
	public Employee(){
		Scanner input=new Scanner(System.in);
		id=input.nextInt();
		name=input.next();
		sex=input.next();
		birthday.year=input.nextInt();
		birthday.month=input.nextInt();
		birthday.day=input.nextInt();
		placeofbirth=input.next();
		educationbackground=input.next();
		professionaltitle=input.next();
		salary=input.nextInt();
		home=input.next();
		phonenumber=input.next();
		position=input.next();
		type=input.next();
		if(type.equals("����")){
			typeNumber=1;
			//���ء���ʦ��ʵ���ҡ��о�Ա
		}
		else if(type.equals("��ʦ")){
			typeNumber=2;
			//���ء���ʦ��ʵ���ҡ��о�Ա
		}
		else if(type.equals("ʵ����")){
			typeNumber=3;
			//���ء���ʦ��ʵ���ҡ��о�Ա
		}
		else if(type.equals("�о�Ա")){
			typeNumber=4;
			//���ء���ʦ��ʵ���ҡ��о�Ա
		}
    }
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public MyDate getBirthday() {
		return birthday;
	}
	public void setBirthday(MyDate birthday) {
		this.birthday = birthday;
	}
	public String getPlaceofbirth() {
		return placeofbirth;
	}
	public void setPlaceofbirth(String placeofbirth) {
		this.placeofbirth = placeofbirth;
	}
	public String getEducationbackground() {
		return educationbackground;
	}
	public void setEducationbackground(String educationbackground) {
		this.educationbackground = educationbackground;
	}
	public String getProfessionaltitle() {
		return professionaltitle;
	}
	public void setProfessionaltitle(String professionaltitle) {
		this.professionaltitle = professionaltitle;
	}
	public int getSalary() {
		return salary;
	}
	public void setSalary(int salary) {
		this.salary = salary;
	}
	public String getHome() {
		return home;
	}
	public void setHome(String home) {
		this.home = home;
	}
	public String getPhonenumber() {
		return phonenumber;
	}
	public void setPhonenumber(String phonenumber) {
		this.phonenumber = phonenumber;
	}
	public String getPosition() {
		return position;
	}
	public void setPosition(String position) {
		this.position = position;
	}
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public int gettypeNumber() {
		return typeNumber;
	}
	public void settypeNumber(int typeNumber) {
		this.typeNumber = typeNumber;
	}
	@Override
	public String toString() {
		return "Ա�� [id=" + id + ", ����=" + name + ", �Ա�=" + sex + ", ��������=" + birthday + ", ����="
				+placeofbirth+ ", ѧ��=" + educationbackground + ", ְ��="
				+ professionaltitle + ", ����=" + salary + ", ��ͥסַ=" + home + ", ��ϵ�绰=" + phonenumber
				+ ", ְλ=" + position + ",����=" + type + "]";
	}
	
	

}
