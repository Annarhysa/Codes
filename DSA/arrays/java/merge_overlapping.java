import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        List<Integer> startTimes = new ArrayList<>();
        List<Integer> endTimes = new ArrayList<>();

        // Read start times
        while (input.hasNextInt()) {
            startTimes.add(input.nextInt());
        }

        // Read end times
        input = new Scanner(System.in);
        while (input.hasNextInt()) {
            endTimes.add(input.nextInt());
        }

        // Validate input length
        if (startTimes.size() != endTimes.size() || startTimes.isEmpty()) {
            System.out.println("Invalid Input");
            return;
        }

        List<Interval> intervals = new ArrayList<>();
        int invalidCount = 0;

        // Create intervals and count invalid ones
        for (int i = 0; i < startTimes.size(); i++) {
            int start = startTimes.get(i);
            int end = endTimes.get(i);
            if (start >= end) {
                invalidCount++;
            } else {
                intervals.add(new Interval(start, end));
            }
        }

        if (intervals.isEmpty()) {
            System.out.println("Invalid Input");
            return;
        }

        // Sort intervals by start time
        intervals.sort(Comparator.comparingInt(a -> a.start));

        // Merge intervals
        List<Interval> mergedIntervals = new ArrayList<>();
        Interval current = intervals.get(0);

        for (int i = 1; i < intervals.size(); i++) {
            Interval next = intervals.get(i);

            if (current.end >= next.start) {
                // Merge intervals
                current.end = Math.max(current.end, next.end);
            } else {
                mergedIntervals.add(current);
                current = next;
            }
        }

        mergedIntervals.add(current);

        // Output the merged intervals
        for (Interval interval : mergedIntervals) {
            System.out.print(interval.start + " " + interval.end + " ");
        }
        System.out.println();

        // Output the count of non-overlapping intervals and invalid intervals
        System.out.println(mergedIntervals.size());
        System.out.println(invalidCount);
    }

    static class Interval {
        int start;
        int end;

        Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}