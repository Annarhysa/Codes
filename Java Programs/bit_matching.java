import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] numbers = input.nextLine().split(" ");
        
        // Convert input strings to integers
        int[] arr = new int[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            arr[i] = Integer.parseInt(numbers[i]);
            // Check if input integer is greater than 7
            if (arr[i] > 7) {
                System.out.println("Invalid Input");
                return;
            }
        }
        
        // Calculate sum of matching bits
        int sum = findSumOfMatchingBits(arr);
        System.out.println(sum);
    }
    
    public static int findSumOfMatchingBits(int[] arr) {
        int sum = 0;
        
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                sum += countMatchingBits(arr[i], arr[j]);
            }
        }
        
        return sum;
    }
    
    public static int countMatchingBits(int x, int y) {
        int count = 0;
        
        // Count matching bits by performing bitwise AND operation
        for (int i = 0; i < 3; i++) {
            if (((x >> i) & 1) == ((y >> i) & 1)) {
                count++;
            }
        }
        
        return count;
    }
}