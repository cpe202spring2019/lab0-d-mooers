def weight_on_planets():
    earth_weight = int(input("What do you weigh on earth? "))
    jupiter_weight = earth_weight * 2.34
    mars_weight = earth_weight * .38
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars_weight, jupiter_weight))   
   
   
if __name__ == '__main__':
   weight_on_planets()
