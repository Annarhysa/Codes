import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input array
        String[] inputStr = scanner.nextLine().split(" ");
        int n = inputStr.length;
        
        // Check if input length is less than 4
        if (n < 4) {
            System.out.println("Invalid Input");
            return;
        }
        
        // Parse input array
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputStr[i]);
        }

        // Calculate modulo values of all consecutive subarrays of length 4
        int maxMod = Integer.MIN_VALUE;
        int luckyArrayStart = 0;
        boolean multipleLuckyArrays = false;
        for (int i = 0; i <= n - 4; i++) {
            int mod = ((arr[i] * arr[i+1] % 9) * arr[i+2] % 9) * arr[i+3] % 9;
            if (mod > maxMod) {
                maxMod = mod;
                luckyArrayStart = i;
                multipleLuckyArrays = false;
            } else if (mod == maxMod) {
                multipleLuckyArrays = true;
            }
        }
        
        // Output
        if (multipleLuckyArrays) {
            System.out.println("There is more than one lucky arrays");
        } else {
            System.out.println(arr[luckyArrayStart] + " " + arr[luckyArrayStart+1] + " " +
                               arr[luckyArrayStart+2] + " " + arr[luckyArrayStart+3]);
            System.out.println(maxMod);
        }
    }
}
                                                                                                                            