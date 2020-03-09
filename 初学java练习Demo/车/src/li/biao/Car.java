package li.biao;

public class Car extends Vehicle {
	public int loader;
	
	Car(String brand, String color,int loader) {
		super(brand, color);
		this.loader = loader;
	}
    public void run() {
   	 System.out.println("车的品牌是："+super.getBrand()
   	 +",车的颜色是："+super.getColor()
   	 +",车的座位有"+this.loader
   	 +"个，速度是："+super.getSpeed());
    }


}
