package test;

import java.util.Scanner;

class Employee {
	/*ID、姓名、性别、出生日期、籍贯、学历、职称、工资、家庭住址、电话等、职务、类型（机关、教师、实验室、研究员等）*/
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
		if(type.equals("机关")){
			typeNumber=1;
			//机关、教师、实验室、研究员
		}
		else if(type.equals("教师")){
			typeNumber=2;
			//机关、教师、实验室、研究员
		}
		else if(type.equals("实验室")){
			typeNumber=3;
			//机关、教师、实验室、研究员
		}
		else if(type.equals("研究员")){
			typeNumber=4;
			//机关、教师、实验室、研究员
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
		return "员工 [id=" + id + ", 姓名=" + name + ", 性别=" + sex + ", 出生日期=" + birthday + ", 籍贯="
				+placeofbirth+ ", 学历=" + educationbackground + ", 职称="
				+ professionaltitle + ", 工资=" + salary + ", 家庭住址=" + home + ", 联系电话=" + phonenumber
				+ ", 职位=" + position + ",类型=" + type + "]";
	}
	
	

}
