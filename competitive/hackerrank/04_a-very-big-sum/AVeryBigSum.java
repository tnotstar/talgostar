/* */

import java.util.Scanner;

public class AVeryBigSum {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] data = new long[n];
        for(int i = 0; i < n; i++)
            data[i] = in.nextLong();
        System.out.println(aVeryBigSum(data));
    }

    static long aVeryBigSum(long[] data) {
        long sum = 0L;
        for(int i = 0; i < data.length; ++i)
            sum += data[i];
        return sum;
    }
}
