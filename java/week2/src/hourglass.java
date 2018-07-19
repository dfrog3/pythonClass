public class hourglass {
    public static void hourglass() {
        for (int i = 6; i > -7; i--) {

            if (i == 6) {
                System.out.print("|");
                for (int x = 0; x < 10; x++) {
                    System.out.print("\"");
                }
                System.out.println("|");
                continue;
            } else if (i == -6) {
                System.out.print("|");
                for (int x = 0; x < 10; x++) {
                    System.out.print("\"");
                }
                System.out.println("|");
                continue;

            } else if (i == 0) {
                System.out.println("     ||");
                continue;
            } else if (i == 1) {
                continue;
            } else if (i == -1) {
                continue;
            } else if (i > 0) {
                for (int j = 0; j < i + 1; j++) {
                    if (j == 0) {
                        for (int k = 0; k < 6 - i; k++) {
                            System.out.print(" ");
                        }
                        System.out.print("\\");
                    } else if (j == i) {
                        System.out.println("/");
                    } else {
                        System.out.print("::");
                    }
                }
            } else if (i < -1) {
                for(int j = 0; j > i - 1; j--) {
                    if (j == 0) {
                        for (int k = 0; k < 6 + i; k++) {
                            System.out.print(" ");
                        }
                        System.out.print("/");
                    } else if (j == i) {
                        System.out.println("\\");
                    } else {
                        System.out.print("::");
                    }

                }


            }
        }



    }




    public static void main(String[] args) {
        hourglass();



    }
}
