import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String output = generatePIN(input);
        System.out.println(output);
    }

    public static String generatePIN(String input) {
        String[] tokens = input.split(" ");
        StringBuilder result = new StringBuilder();

        for (String token : tokens) {
            int sum = 0;
            for (char c : token.toCharArray()) {
                sum += Character.getNumericValue(c);
            }
            while (sum > 9) {
                sum = sum % 10 + sum / 10;
            }
            char ch = (char) (sum + 'a' - 1);
            if (sum % 2 == 1) {
                result.append(ch);
            } else {
                result.append(sum);
            }
        }

        return result.toString();
    }
}
                                                                                                                            