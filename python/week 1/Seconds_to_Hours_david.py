def main():
    print("please enter the seconds you would like to convert.")
    totalSeconds = int(input())
    totalHours = totalSeconds // 3600
    remainingSeconds = totalSeconds % 3600
    totalMinuets = remainingSeconds // 60
    remainingSeconds = remainingSeconds % 60
    print(totalSeconds, "seconds", "=", totalHours ," hours, ", totalMinuets, " minuets, and ", remainingSeconds, " seconds.")
    main()
main()
