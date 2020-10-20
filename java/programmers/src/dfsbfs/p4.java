package dfsbfs;

import java.util.*;
import java.util.zip.CheckedOutputStream;

public class p4 {

    static String[][] tickets;

    static HashMap<String, PriorityQueue> graph;


    static ArrayList ans;


    public static void dfs(String via) {
        if (graph.get(via).isEmpty()) {
            return;
        }

        while (!graph.get(via).isEmpty()) {
            String next = (String) graph.get(via).poll();
            dfs(next);
            ans.add(next);
        }


    }


    public static void makeGraph() {


        for (String[] elm : tickets) {
            String start = elm[0];
            String end = elm[1];
            if (graph.containsKey(start)) {
                graph.get(start).add(end);


            } else {
                PriorityQueue<String> info = new PriorityQueue<String>();
                info.add(end);


                graph.put(start, info);

            }

        }
        System.out.println(graph);


    }


    public static void main(String[] args) {

        tickets = new String[][]{{"ICN", "SFO" }, {"ICN", "ATL" }, {"SFO", "ATL" }, {"ATL", "ICN" }, {"ATL", "SFO" }};
        graph = new HashMap<>();
        makeGraph();
        System.out.println(graph);
        ans = new ArrayList();
        dfs("ICN");

        Collections.reverse(ans);
        String[] returnans = new String[ans.size()+1];

        returnans[0] = "ICN";
        returnans.
    }
}
