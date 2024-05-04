import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int largestSpecialPrime = findLargestSpecialPrime(n);
        System.out.println(largestSpecialPrime);
    }

    public static int findLargestSpecialPrime(int n) {
        // Iterate from n-1 to 2 to find the largest special prime
        for (int i = n - 1; i >= 2; i--) {
            if (isPrime(i) && isSpecialPrime(i)) {
                return i;
            }
        }
        return -1; // No special prime found
    }

    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    // Function to check if a number is a special prime
    public static boolean isSpecialPrime(int num) {
        String str = Integer.toString(num);
        for (int i = 0; i < str.length(); i++) {
            String temp = str.substring(i) + str.substring(0, i);
            int rotatedNum = Integer.parseInt(temp);
            if (!isPrime(rotatedNum)) {
                return false;
            }
        }
        return true;
    }
}
                                                                                                                            