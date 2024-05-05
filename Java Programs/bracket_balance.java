import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // Input strings separated by comma
        String[] strings = input.nextLine().split(",");
        
        for (String s : strings) {
            int pairs = countPairs(s);
            if (pairs == -1) {
                System.out.println("NO " + pairs);
            } else {
                System.out.println("YES " + pairs);
            }
        }
    }
    
    // Method to count the number of matched pairs of brackets
    public static int countPairs(String s) {
        Stack<Character> stack = new Stack<>();
        int count = 0;
        
        for (char bracket : s.toCharArray()) {
            if (bracket == '(' || bracket == '{' || bracket == '[') {
                stack.push(bracket);
            } else {
                if (stack.isEmpty()) {
                    return -1; // Unmatched closing bracket
                }
                char top = stack.pop();
                if ((bracket == ')' && top != '(') || (bracket == '}' && top != '{') || (bracket == ']' && top != '[')) {
                    return -1; // Mismatched opening and closing brackets
                }
                count++;
            }
        }
        
        // Check for unmatched opening brackets
        if (!stack.isEmpty()) {
            return -1;
        }
        
        // Adjust count for unmatched closing brackets
        count -= stack.size();
        
        return count;
    }
}