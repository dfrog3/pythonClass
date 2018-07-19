public class test {
    public static int lastTwo(int x) {
        String out ="";
        for (int i = 0; i<2; i++){
            int jar = x %10;
            x = x/10;
            out = out + String.valueOf(jar);
        }
        return Integer.valueOf(out);
    }

    public static String Two(int x) {
        String out ="";
        for (int i = 0; i<1; i++){
            int jar = x %100;
            x = x/100;
            jar = jar /10;
            out = out + String.valueOf(jar);
        }
        return ("The" + (out+"0's"));
    }







    public static void main(String[] args) {
        System.out.println(Two(199989));






    }
}
