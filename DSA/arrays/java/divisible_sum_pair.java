import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input divisor
        int divisor = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        // Input array
        String[] arrStr = scanner.nextLine().split(" ");
        int[] arr = new int[arrStr.length];
        for (int i = 0; i < arrStr.length; i++) {
            arr[i] = Integer.parseInt(arrStr[i]);
        }
        
        // Find the number of pairs of integers in the array whose sum is divisible by the given divisor
        int count = divisibleSumPairs(divisor, arr);
        
        // Output the result
        System.out.println(count);
    }
    
    public static int divisibleSumPairs(int divisor, int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if ((arr[i] + arr[j]) % divisor == 0) {
                    count++;
                }
            }
        }
        return count;
    }
}
                                                                                                                            