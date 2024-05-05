import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // Array size
        int q = scanner.nextInt(); // Query count
        
        int[] arr = new int[n + 1]; // Initialize array with size n+1
        
        // Perform queries
        for (int i = 0; i < q; i++) {
            int l = scanner.nextInt(); // Left index
            int r = scanner.nextInt(); // Right index
            int val = scanner.nextInt(); // Value to add
            
            arr[l] += val; // Add value to left index
            if (r < n) { // If right index is within array bounds, subtract value from right index + 1
                arr[r + 1] -= val;
            }
        }
        
        // Calculate prefix sum
        for (int i = 2; i <= n; i++) {
            arr[i] += arr[i - 1];
        }
        
        // Find maximum value in array
        int max = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            max = Math.max(max, arr[i]);
        }
        
        System.out.println(max);
    }
}
                                                                                                                            