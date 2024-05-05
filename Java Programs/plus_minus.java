import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt(); // Number of elements in the array
        int[] arr = new int[n]; // Array to store the elements
        for (int i = 0; i < n; i++) {
            arr[i] = input.nextInt(); // Taking input for the array
        }
        calculateFractions(arr); // Calling method to calculate fractions
    }
    
    public static void calculateFractions(int[] arr) {
        int positiveCount = 0;
        int negativeCount = 0;
        int zeroCount = 0;
        int n = arr.length;
        
        // Counting positive, negative, and zero elements
        for (int i = 0; i < n; i++) {
            if (arr[i] > 0)
                positiveCount++;
            else if (arr[i] < 0)
                negativeCount++;
            else
                zeroCount++;
        }
        
        // Calculating fractions
        double positiveFraction = (double) positiveCount / n;
        double negativeFraction = (double) negativeCount / n;
        double zeroFraction = (double) zeroCount / n;
        
        // Printing fractions with three decimal places
        System.out.printf("%.3f%n", positiveFraction);
        System.out.printf("%.3f%n", negativeFraction);
        System.out.printf("%.3f%n", zeroFraction);
    }
}
                                                                                                                            