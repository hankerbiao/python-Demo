package com.cn.算法;

import java.util.ArrayList;

public class BinarySearch {
    public int binarySearch(int[] list,int item){

        int low = 0;//low第一个数的下表
        int hight = list.length-1; //最后一个数的下表

        while (low<=hight){

            int mid = (hight+low)/2;//中间数
            int guss = list[mid]; //把中间值的坐标的数赋值给guss guss
            if (guss == item){
                return mid;
            }
            //如果程序猜的数小于输入的数，则中间+1为最小值
            if(guss < item){
                low = mid + 1;
            }
            //如果程序猜的数大于输入的数，则中间1为最大值
            if(guss > item){
                hight = mid - 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] list = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
        BinarySearch bSearch = new BinarySearch();
        int item = bSearch.binarySearch(list,8);
        System.out.println(item);
    }
}
