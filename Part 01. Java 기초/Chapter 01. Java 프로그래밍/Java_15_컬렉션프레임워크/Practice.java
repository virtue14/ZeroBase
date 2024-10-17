// Practice
package Java_15_컬렉션프레임워크;
// 로또 번호 만들기

import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;

public class Practice {
    public static void main(String[] args) {

        HashSet set = new HashSet();

        for (int i = 0; set.size() < 6; i++) {
            int num = (int) (Math.random() * 45) + 1;
            set.add(num);
        }

        System.out.println("정렬 전 = " + set);

        LinkedList list = new LinkedList(set);
        Collections.sort(list);
        System.out.println("로또 번호 = " + list);


    }
}
