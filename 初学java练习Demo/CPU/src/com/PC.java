package com;

public class PC {
	CPU cpu;
	HardDisk HD;
	
	public void setHardDisk(HardDisk h)
	{	
		this.HD = h;	
	}
	
	
	public void setCPU(CPU c) {
		this.cpu = c;
		
	}

	void show()
	{
		System.out.println("CPU的速度为："+cpu.getSpeed());
		System.out.println("硬盘的大小为："+HD.getAmount());
		
	}


}
