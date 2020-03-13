package com.cn.发红包例子;

import java.util.ArrayList;
//群主的类
public class Manage extends User {
    Manage(){
    }
    //有参构造方法，
    public Manage(String name, int monet) {
        super(name, monet);
    }
    //发红包方法，
    public ArrayList<Integer> send(int totalMoney,int count){
        //需要一个集合 存储若干红包金额
        ArrayList<Integer> redList = new ArrayList<>();
        //看一下群主有多少钱
        int leftMoney = super.getMonet();
        if(totalMoney>leftMoney){
            System.out.println("余额不足");
            return redList;  //返回空值
        }
        //扣钱，其实就是重新设置余额
        super.setMonet(leftMoney - totalMoney);
        //发红包需要拆分为count份
        int avg = totalMoney / count;
        int mod = totalMoney % count;
        //除不开的零头放在最后一个红包里//
        for(int i = 0;i<count-1;i++){
            redList.add(avg);
        }
        //最后一个红包
        int last = avg + mod;
        redList.add(last);

        return redList;
    }

}
