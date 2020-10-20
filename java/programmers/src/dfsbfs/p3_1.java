package dfsbfs;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class p3_1 {


        static public boolean makeCount(String str1, String str2) {

            int cnt = 0;

            for (int i = 0; i < str1.length(); i++) {
                if (str1.charAt(i) != str2.charAt(i)) {
                    cnt++;
                }
            }
            if (cnt == 1) {
                return true;
            }
            return false;
        }





        public int solution(String begin, String target, String[] words) {


            HashMap<String, List>  graph = new HashMap<>();
            HashMap<String,Boolean> visit = new HashMap<>();
            HashMap<String,Integer> layer = new HashMap<>();

            for (int i = 0; i < words.length + 1; i++) {
                if (i == words.length) {
                    graph.put(begin, new LinkedList());
                    visit.put(begin,false);
                    layer.put(begin,0);

                } else {
                    graph.put(words[i], new LinkedList());
                    visit.put(words[i], false);

                }
            }
            for (String str1 : graph.keySet()) {

                for (String str2 : words) {
                    if (makeCount(str1, str2) == true) {
                        graph.get(str1).add(str2);
                    }
                }

            }

            if(!graph.containsKey(target)){
                return 0;
            }
            Queue<String> queue = new LinkedList<>();

            queue.add(begin);

            while (!queue.isEmpty()){

                String out= queue.poll();

                for(Object elm : graph.get(out)){
                    String tmp = (String)elm;
                    if(visit.get(tmp).booleanValue() == false){
                        visit.put(tmp,true);
                        layer.put(tmp, layer.getOrDefault(tmp,1)+layer.get(out));
                        queue.add(tmp);

                    }
                }


            }
            return layer.get(target);



        }

    }
