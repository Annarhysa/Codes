import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s = input.next();
        int longestLength = lengthOfLongestSubstring(s);
        System.out.println(longestLength);
    }
    
    public static int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int longestLength = 0;
        Map<Character, Integer> lastIndex = new HashMap<>();
        
        int start = 0;
        for (int end = 0; end < n; end++) {
            char c = s.charAt(end);
            if (lastIndex.containsKey(c)) {
                start = Math.max(start, lastIndex.get(c) + 1);
            }
            longestLength = Math.max(longestLength, end - start + 1);
            lastIndex.put(c, end);
        }
        
        return longestLength;
    }
}
                                                                                                                            