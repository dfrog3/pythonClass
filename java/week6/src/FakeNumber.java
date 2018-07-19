
public class FakeNumber {
//first outer inner last *
    private double normNumber;
    private double fakeNumber;


    public FakeNumber(double normNumber, double fakeNumber) {
        this.normNumber = normNumber;
        this.fakeNumber = fakeNumber;
    }

    public FakeNumber addFakeNumbers(FakeNumber othaNumba){
        double a = this.normNumber + othaNumba.normNumber;
        double b = this.normNumber + othaNumba.normNumber;

        return new FakeNumber(a,b);

    }

    public FakeNumber subtractFakeNumbers(FakeNumber othaNumba){
        double a = this.normNumber - othaNumba.normNumber;
        double b = this.normNumber - othaNumba.normNumber;
        return new FakeNumber(a,b);

    }


    public FakeNumber multiplyFakeNumbers(FakeNumber othaNumba){

        double first = this.normNumber * othaNumba.normNumber;//norm
        double outer = this.normNumber* othaNumba.fakeNumber; //fake
        double inner = this.fakeNumber * othaNumba.normNumber;//fake
        double last = (this.fakeNumber * othaNumba.fakeNumber)-1;//norm


        double a = first + last;
        double b = outer + inner;
        return new FakeNumber(a,b);
    }


    public FakeNumber divideFakeNumbers(FakeNumber othaNumber){
        double a = ((this.normNumber*othaNumber.normNumber)+(this.fakeNumber+othaNumber.fakeNumber))/ ((othaNumber.normNumber*othaNumber.normNumber)+(othaNumber.fakeNumber*othaNumber.fakeNumber));
        double b = ((this.fakeNumber*othaNumber.normNumber)-(this.normNumber*othaNumber.fakeNumber))/((othaNumber.normNumber*othaNumber.normNumber)+(othaNumber.fakeNumber*othaNumber.fakeNumber));
        return new FakeNumber(a,b);

    }


    public String getFakeNumber() {
        return (this.normNumber + " + "+ this.fakeNumber+"i");
    }
}
