import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String start = input.next();
        String end = input.next();
        boolean ret = canTransform(start, end);
        System.out.println(ret);
    }
    
    public static boolean canTransform(String start, String end) {
        if (start.length() != end.length()) {
            return false;
        }
        
        int i = 0, j = 0;
        while (i < start.length() && j < end.length()) {
            while (i < start.length() && start.charAt(i) == 'X') {
                i++;
            }
            while (j < end.length() && end.charAt(j) == 'X') {
                j++;
            }
            if ((i < start.length() && j >= end.length()) || (i >= start.length() && j < end.length())) {
                return false;
            }
            if (start.charAt(i) != end.charAt(j)) {
                return false;
            }
            if (start.charAt(i) == 'L' && i < j) {
                return false;
            }
            if (start.charAt(i) == 'R' && i > j) {
                return false;
            }
            i++;
            j++;
        }
        
        return true;
    }
}
                                                                                                                            