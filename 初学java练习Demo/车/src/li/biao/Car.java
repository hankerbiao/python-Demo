package li.biao;

public class Car extends Vehicle {
	public int loader;
	
	Car(String brand, String color,int loader) {
		super(brand, color);
		this.loader = loader;
	}
    public void run() {
   	 System.out.println("����Ʒ���ǣ�"+super.getBrand()
   	 +",������ɫ�ǣ�"+super.getColor()
   	 +",������λ��"+this.loader
   	 +"�����ٶ��ǣ�"+super.getSpeed());
    }


}
