package com.cn.发红包例子;
//User类
public class User {
    //设置两个属性，名字 金额
    private String name;
    private int monet;

    public User() {
    }
    //有参构造方法，每个用户必须有姓名和金额

    public User(String name, int monet) {
        this.name = name;
        this.monet = monet;
    }
    //输出用户信息
    public void show(){
        System.out.println("我叫："+name+"我有"+monet+"元钱");
    }
    //访问属性方法
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMonet() {
        return monet;
    }

    public void setMonet(int monet) {
        this.monet = monet;
    }
}
