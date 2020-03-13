package com.cn.发红包例子;

import java.util.ArrayList;
import java.util.Random;

//普通成员
public class Member extends User{
    public Member() {
    }

    public Member(String name, int monet) {
        super(name, monet);
    }
    public void receive(ArrayList<Integer> list){
        //从多个红包中随便抽取一个给我自己
        //随机获取一个集合中的索引编号
        int index = new Random().nextInt(list.size());
        //根据索引，从集合当中删除，并且得到被删除的红包给我自己
        int delta = list.remove(index);
        int money = super.getMonet();

        super.setMonet(money + delta);
    }
}
