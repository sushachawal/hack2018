def FTP():
    FTP = input("input your FTP: ")
    #input FTP

    twentymin = input("input your 20 minute avg power: ")
    #input 20min avg power

    time_est = input("input an estimated time of completion in seconds: ")
    #input rough estimate of time to complete course

    avg_power = FTP + (60 - time_est/60) * (twentymin - FTP)/40
    #avg Power: 20 mins power = FTP/0.95

    energy = avg_power * time_est

    return {"avg_power": avg_power, "energy": energy}
