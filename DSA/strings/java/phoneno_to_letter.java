import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
      
        String digits = input.nextLine();
        
        List<String> combinations = letterCombinations(digits);
       
        for (String combination : combinations) {
            System.out.print(combination + " ");
        }
    }
    
    public static List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return result;
        }
        String[] mapping = {
            "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };
        generateCombinations(result, digits, mapping, "", 0);
        return result;
    }
    
    private static void generateCombinations(List<String> result, String digits, String[] mapping, String current, int index) {
        if (index == digits.length()) {
            result.add(current);
            return;
        }
        String letters = mapping[digits.charAt(index) - '0'];
        if (!letters.equals("1")) { // Skip adding '1' to the combination
            for (int i = 0; i < letters.length(); i++) {
                generateCombinations(result, digits, mapping, current + letters.charAt(i), index + 1);
            }
        } else {
            generateCombinations(result, digits, mapping, current, index + 1);
        }
    }
}