import sys, argparse
argParser = argparse.ArgumentParser()
argParser.add_argument("-op", "--calculate", help="Enter core for core power consumption, mem for power consumption of CMG, l2 for l2 cache memory consumption")
argParser.add_argument("-c", "--cycles", help="Value of EA_CORE or EA_MEMORY or EA_L2")
argParser.add_argument("-t", "--time", help="Total execution time")
args = argParser.parse_args()
#print("args=%s" % args)

print("args.calculate=%s" % args.calculate)
#print ('Input file is ', inputfile)
#print ('Output file is ', outputfile)
power = 0.0
cycles = float(args.cycles.replace(",", ""))

if (args.calculate == 'core'):
    power=(float(cycles) * 8.04e-9) / float(args.time)
elif (args.calculate == 'mem'):
    power=(cycles * 271e-9) / float(args.time)
print("Power consumed is "+ str(power) + "W")

