import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] nums = new int[6]; // Array to store the six positive integers
        for (int i = 0; i < 6; i++) {
            nums[i] = input.nextInt(); // Taking input for the six positive integers
        }
        long[] result = findMinMax(nums); // Calling method to find minimum and maximum values
        System.out.println(result[0] + " " + result[1]); // Printing the minimum and maximum values
    }
    
    public static long[] findMinMax(int[] nums) {
        Arrays.sort(nums); // Sorting the array in ascending order
        long minSum = 0;
        long maxSum = 0;
        
        // Minimum sum can be obtained by summing the first four smallest numbers
        for (int i = 0; i < 4; i++) {
            minSum += nums[i];
        }
        
        // Maximum sum can be obtained by summing the last four largest numbers
        for (int i = 2; i < 6; i++) {
            maxSum += nums[i];
        }
        
        return new long[]{minSum, maxSum}; // Returning the minimum and maximum values
    }
}
                                                                                                                            