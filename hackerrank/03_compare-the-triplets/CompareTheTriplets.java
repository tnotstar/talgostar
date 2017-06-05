/* */

import java.util.Scanner;

public class CompareTheTriplets {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] a = new int[3];
        for(int i = 0; i < 3; i++)
            a[i] = in.nextInt();

        int[] b = new int[3];
        for(int i = 0; i < 3; i++)
            b[i] = in.nextInt();

        int[] rs = compareTheTriplets(a, b);
        System.out.print(rs[0] + " " + rs[1]);
    }

    static int[] compareTheTriplets(int[] a, int[] b) {
        int[] rs = {0, 0};
        for(int i = 0; i < 3; i++) {
            if(a[i] > b[i])
                rs[0]++;
            else if (a[i] < b[i])
                rs[1]++;
        }
        return rs;
    }
}
