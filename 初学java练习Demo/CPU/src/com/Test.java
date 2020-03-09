package com;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		CPU cpu = new CPU();
		cpu.setSpeed(2200);
		
		HardDisk disk = new HardDisk();
		disk.setAmmount(200);
		
		PC pc = new PC();
		pc.setCPU(cpu);
		pc.setHardDisk(disk);
		
		pc.show();
	}

}
