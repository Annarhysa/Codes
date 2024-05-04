import java.util.*;

public class Main {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int target = input.nextInt();
        int n = input.nextInt();
        int[] candies = new int[n];
        for (int i = 0; i < n; i++) {
            candies[i] = input.nextInt();
        }
        int steps = findSteps(target, candies);
        System.out.println(steps);
    }
    
    public static int findSteps(int target, int[] candies) {
        Arrays.sort(candies); // Sort the candies in ascending order
        int steps = 0;
        int i = 0, j = candies.length - 1;
        while (i < j) {
            if (candies[i] + 2 * candies[i + 1] >= target) {
                return steps + 1; // If sweetness is already >= target, return steps + 1
            }
            candies[i + 1] = candies[i] + 2 * candies[i + 1]; // Combine two least sweet candies
            i++;
            steps++;
        }
        return steps;
    }
}
                                                                                                                            