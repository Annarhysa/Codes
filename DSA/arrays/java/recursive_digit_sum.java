import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String number = input.nextLine();
        int repeat = input.nextInt();
        int ret = superDigit(number, repeat);        
        System.out.println(ret);
    }
    
    public static int superDigit(String n, int k) {
        // Calculate the super digit of the sum of digits of n
        int sum = 0;
        for (char c : n.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        // Calculate the super digit of the sum
        int superDigit = calculateSuperDigit(sum);
        // If k is 1, return the super digit of the sum
        if (k == 1) {
            return superDigit;
        }
        // Otherwise, calculate the super digit of the sum repeated k times
        return calculateSuperDigit(superDigit * k);
    }
    
    private static int calculateSuperDigit(int num) {
        // If the number has only one digit, return that digit
        if (num < 10) {
            return num;
        }
        // Otherwise, recursively calculate the super digit of the sum of digits
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return calculateSuperDigit(sum);
    }
}