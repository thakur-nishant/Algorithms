import java.util.*;
public class SubsequenceGenerator{

    public static void main(String []args){
        System.out.println("Hello World");
        System.out.println(16 & 1<<4);
        System.out.println();
        String s = "aabcd";
        ArrayList<String> res = getSubsequence(s);
        Collections.sort(res);
        System.out.println(res);
        System.out.println();
        ArrayList<String> res1 = dfsSubsequence(s);
        Collections.sort(res1);
        System.out.println(res1);

    }

    public static ArrayList getSubsequence(String s) {
        ArrayList<String> result = new ArrayList<String>();
        int n = s.length();
        for (int counter = 1; counter < 1<<n; ++counter) {
            String currString = "";
            for (int j = 0; j < n; ++j) {
                if ((counter & (1<<j)) != 0) {
                    currString += s.charAt(j);
                }
            }
            result.add(currString);
        }
        return result;
    }

    ///////////////////////////////////////////////////////
    //////    DFS Method for Unique Subsequences    ///////
    ///////////////////////////////////////////////////////
    public static ArrayList dfsSubsequence(String s) {
        ArrayList<String> result = new ArrayList<String>();
        char[] s_array = s.toCharArray();
        Arrays.sort(s_array);
        s = new String(s_array);

        for (int i = 0; i < s.length(); ++i){
            dfsHelper(""+s.charAt(i), s.substring(i+1, s.length()), result);
        }
        return result;
    }

    public static void dfsHelper(String pre, String s, ArrayList<String> result) {
        if (result.contains(pre)) return;

        result.add(pre);

        for (int i = 0; i < s.length(); ++i) {
            dfsHelper(pre+s.charAt(i), s.substring(i+1, s.length()), result);
        }
    }

}