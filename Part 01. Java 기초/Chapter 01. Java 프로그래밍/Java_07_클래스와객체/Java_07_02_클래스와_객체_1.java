package Java_07_클래스와객체;// Java 프로그래밍 - 클래스와 객체_2

import Java_07_클래스와객체.car.Car2;

class Car3 {
    String name;
    String type;

    Car3(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public void printCarInfo() {
        System.out.println("=== Java_07_클래스와객체.Car4 Info ===");
        System.out.println("name: " + name);
        System.out.println("type: " + type);
    }

    // 오버로딩 구현
    public void printCarInfo(String date) {
        this.printCarInfo();
        System.out.println("date: " + date);
    }

    public void printCarInfo(int number) {
        this.printCarInfo();
        System.out.println("number: " + number);
    }

    public void printCarInfo(String date, int number) {
        this.printCarInfo();
        System.out.println("date: " + date);
        System.out.println("number: " + number);

    }

}


class Car4 {
    // 스태틱 변수
    static String name = "None";
    String type;

    Car4(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public void printCarInfo() {
        System.out.println("=== Java_07_클래스와객체.Car4 Info ===");
        System.out.println("name: " + name);
        System.out.println("type: " + type);
    }

    // 스태틱 메소드
    public static void getName() {
        System.out.println("Car name: " + name);
    }
}


public class Java_07_02_클래스와_객체_1 {

    public static void main(String[] args) {
        Car3 myCar13 = new Car3("a", "sedan");
        myCar13.printCarInfo();

//      1. 오버로딩 사용
        System.out.println("=== 오버로딩 사용 ===");
        myCar13.printCarInfo("2022");
        myCar13.printCarInfo(1234);
        myCar13.printCarInfo("2022", 1234);


//      2. 접근 제어자
        System.out.println("=== 접근 제어자 ===");
        Car2 myCar2 = new Car2("a", "b", "c", "d");
        System.out.println(myCar2.name1);
//        System.out.println(myCar2.name2);
//        System.out.println(myCar2.name3);
//        System.out.println(myCar2.name4);


//      3. Static
        System.out.println("=== Static ===");
        Car4.getName();
        Car4 myCar3_1 = new Car4("a", "sedan");
        Car4 myCar3_2 = new Car4("b", "suv");
        Car4 myCar3_3 = new Car4("c", "rv");
        myCar3_1.printCarInfo();
        myCar3_2.printCarInfo();
        myCar3_3.printCarInfo();

    }

}
