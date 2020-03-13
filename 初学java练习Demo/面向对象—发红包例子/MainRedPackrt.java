package com.cn.发红包例子;

import java.util.ArrayList;

public class MainRedPackrt {
    public static void main(String[] args) {
        Manage manage = new Manage("群主",100);

        Member one = new Member("成员A",0);
        Member two = new Member("成员B",0);
        Member three = new Member("成员C",0);

        manage.show();//100
        one.show();//0
        two.show();//0
        three.show();//0
        System.out.println("====================");
        //群主总共发20块钱，总共分3个红包
        ArrayList<Integer> redList = manage.send(20,3);
        //三个成员来收红包
        one.receive(redList);
        two.receive(redList);
        three.receive(redList);
        manage.show();//100-20=80
        one.show();
        two.show();
        three.show();
        System.out.println("====================");

    }
}
