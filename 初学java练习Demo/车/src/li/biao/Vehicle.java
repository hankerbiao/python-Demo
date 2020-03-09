/*
（一）定义一个汽车类Vehicle，要求如下：（知识点：类的继承 方法的覆盖）
（1）属性包括：汽车品牌brand（String类型）、颜色color（String类型）和速度speed（double类型）。
（2）至少提供一个有参的构造方法（要求品牌和颜色可以初始化为任意值，但速度的初始值必须为0）。
（3）为属性提供访问器方法。
（4）定义一个一般方法run()，用打印语句描述汽车奔跑的功能
定义测试类VehicleTest，在其main方法中创建一个品牌为“benz”、颜色为“black”的汽车。
（二）定义一个Vehicle类的子类轿车类Car，要求如下：
（1）轿车有自己的属性载人数loader（int 类型）。
（2）提供该类初始化属性的构造方法。
（3）重新定义run()，用打印语句描述轿车奔跑的功能。
（4）定义测试类，在其main方法中创建一个品牌为“Honda”、颜色为“red”，载人数为2人的轿车。
*/
package li.biao;

public class Vehicle {


	public String getBrand() {
		return brand;
	}
	public void setBrand(String brand) {
		this.brand = brand;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	public double getSpeed() {
		return speed;
	}
	public void setSpeed(double speed) {
		this.speed = speed;
	}
	private String brand;
	private String color;
	private double speed;

	Vehicle(String brand,String color)
	{
		this.brand = brand; 
		this.color = color; 
		speed = 0;
		
	}
	void run(){
		
	System.out.println(
			"车的品牌是："+this.brand+","
			+ "颜色是："+this.color+","
			+ "速度是："+this.speed
			);		
	}
	
}