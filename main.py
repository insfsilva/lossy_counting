from demo import WareHouseDemo, RomeoAndJulietDemo, ExponentialDistributionDemo

if __name__ == '__main__':
    print("Random exponential demo")
    randomExponentialDemo = ExponentialDistributionDemo(minSupport=0.01, error=0.001)
    randomExponentialDemo.start()
    randomExponentialDemo.printOutput()
    print("-----------------------------------------\n")

    print("Warehouse demo")
    wareHouseDemo = WareHouseDemo(minSupport=0.01, error=0.001)
    wareHouseDemo.start()
    wareHouseDemo.printOutput()
    print("-----------------------------------------\n")

    print("Paradise, The Divine Comedy")
    paradiseDemo = ParadiseDemo(minSupport=0.01, error=0.001)
    paradiseDemo.start()
    paradiseDemo.printOutput()
    print("-----------------------------------------\n")
