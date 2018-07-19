public class BankAccount {
    private String user;
    private double balance;


    public BankAccount(String user, double balance) {
        this.user = user;
        this.balance = balance;
    }





    public void makeTransaction(double amount){
        this.balance -= amount;


    }

    public void makeDeposite(double amount){
        this.balance += amount;
    }


    public double getBalance() {
        return balance;
    }






}
