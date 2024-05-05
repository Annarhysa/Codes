import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] tasks = new int[n];
        for (int i = 0; i < n; i++) {
            tasks[i] = input.nextInt();
        }
        int k = input.nextInt();
        
        int minTime = minTimeToComplete(tasks, k);
        System.out.println(minTime);
    }
    
    public static int minTimeToComplete(int[] tasks, int k) {
        int start = Arrays.stream(tasks).max().getAsInt();
        int end = Arrays.stream(tasks).sum();
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isPossible(tasks, mid, k)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
    
    public static boolean isPossible(int[] tasks, int maxTime, int k) {
        int workers = 1;
        int totalTime = 0;
        
        for (int task : tasks) {
            totalTime += task;
            if (totalTime > maxTime) {
                totalTime = task;
                workers++;
            }
        }
        
        return workers <= k;
    }
}