import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int m = input.nextInt(); // Number of items
        int r = input.nextInt(); // Number of variations for each item
        int target = input.nextInt(); // Desired total
        
        int count = countCombinations(m, r, target);
        System.out.println(count);
    }
    
    public static int countCombinations(int m, int r, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1; // Base case
        
        // Iterate through each item
        for (int i = 1; i <= m; i++) {
            for (int j = target; j >= 0; j--) {
                // Calculate the number of combinations for the current target
                for (int k = 1; k <= r && k <= j; k++) {
                    dp[j] += dp[j - k];
                }
            }
        }
        
        return dp[target];
    }
}