package Java_18_연습문제풀이3;

public class Practice1 {
    public static void solution(int[] nums) {
        int idx = 0;
        for (int num : nums) {
            if (idx == 0 || num > nums[idx - 1]) {
                nums[idx++] = num;
            }
        }
        System.out.print("[" + idx + "]");
        for (int i = 0; i < idx; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Test code
        solution(new int[] {1, 1, 2});
        solution(new int[] {0, 0, 1, 1, 1, 2, 2, 3, 3, 4});
    }
}
