/*
��һ������һ��������Vehicle��Ҫ�����£���֪ʶ�㣺��ļ̳� �����ĸ��ǣ�
��1�����԰���������Ʒ��brand��String���ͣ�����ɫcolor��String���ͣ����ٶ�speed��double���ͣ���
��2�������ṩһ���вεĹ��췽����Ҫ��Ʒ�ƺ���ɫ���Գ�ʼ��Ϊ����ֵ�����ٶȵĳ�ʼֵ����Ϊ0����
��3��Ϊ�����ṩ������������
��4������һ��һ�㷽��run()���ô�ӡ��������������ܵĹ���
���������VehicleTest������main�����д���һ��Ʒ��Ϊ��benz������ɫΪ��black����������
����������һ��Vehicle�������γ���Car��Ҫ�����£�
��1���γ����Լ�������������loader��int ���ͣ���
��2���ṩ�����ʼ�����ԵĹ��췽����
��3�����¶���run()���ô�ӡ��������γ����ܵĹ��ܡ�
��4����������࣬����main�����д���һ��Ʒ��Ϊ��Honda������ɫΪ��red����������Ϊ2�˵Ľγ���
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
			"����Ʒ���ǣ�"+this.brand+","
			+ "��ɫ�ǣ�"+this.color+","
			+ "�ٶ��ǣ�"+this.speed
			);		
	}
	
}