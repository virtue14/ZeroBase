package Java_07_클래스와객체;//  Practice
//  다음 클래스 직접 만든 후 객체 생성
//  클래스명: Java_07_클래스와객체1.Animal
//  특성: 이름, 무게, 분류
//  기능: 먹기, 잠자기, 걷기, 뛰기

class Animal {
    String name;
    double weight;
    String classfication;

    public Animal(String name, Double weight, String classfication) {
        this.name = name;
        this.weight = weight;
        this.classfication = classfication;
    }

    public void printInfo() {
        System.out.println("name = " + name);
        System.out.println("weight = " + weight);
        System.out.println("classfication = " + classfication);
    }

    public void eat() {
        System.out.println("냠냠!");
    }

    public void sleep() {
        System.out.println("쿨쿨!");
    }

    public void walk() {
        System.out.println("걷기!");
    }

    public void run() {
        System.out.println("뛰기!");
    }
}

public class Java_07_01_클래스와_객체_2 {
    public static void main(String[] args) {
        // Test code
        Animal animal1 = new Animal("강아지", 5.0, "포유류");
        Animal animal2 = new Animal("구피", 0.01, "어류");

        animal1.printInfo();
        animal2.printInfo();
    }
}
