/* */

import java.util.Scanner;

public class SimpleArraySum {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] data = new int[n];
        for(int i = 0; i < n; i++)
            data[i] = in.nextInt();
        System.out.println(simpleArraySum(data));
    }

    static int simpleArraySum(int[] data) {
        int sum, i;
        for(sum = 0, i = 0; i < data.length; i++)
            sum += data[i];
        return sum;
    }
}
