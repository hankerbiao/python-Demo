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
		System.out.println("CPU���ٶ�Ϊ��"+cpu.getSpeed());
		System.out.println("Ӳ�̵Ĵ�СΪ��"+HD.getAmount());
		
	}


}
