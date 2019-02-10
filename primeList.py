import time, sys

silent = False

def isPrime(number):
    for divider in range(2, int(number/2)):
        if number%divider == 0:
            return False
    return True

def process_prime(number, numbers):
    percentage = int(number/numbers*100)
    if not silent:
        print("Progress: {}                                  ".format(percentage), end='\r', flush=True)
    return isPrime(number)

def getPrimes(begining, end):
    return [n for n in range(begining, end) if process_prime(n, (end - begining))]

def main():
    global silent
    report = False
    s = time.time() 
    if "-s" in sys.argv:
        silent = True
    if "-f" in sys.argv:
        filename = sys.argv[sys.argv.index("-f")+1]
        if filename != '':
            report = True
    try:
        if report:
            f= open(filename,'w',encoding = 'utf-8')
        if not sys.stdin.isatty():
            arguments = sys.stdin.readlines()[0].split()
            if not silent: 
                print("Processing prime numbers in range from {} until {}. Set by a pipe.".format(arguments[0], arguments[1]))
            primes = getPrimes(int(arguments[0]), int(arguments[1]))
        elif len(sys.argv) > 2:
            if not silent: 
                print("Processing prime numbers in range from {} until {}. Set by a arguments.".format(sys.argv[1], sys.argv[2]))
            primes = getPrimes(int(sys.argv[1]), int(sys.argv[2]))
        else:
            print("You need to give 2 arguments.")
            return
        sys.stdout.flush()
        for prime in primes:
            if report:
                f.write("{} ".format(prime))
            else:
                sys.stdout.write("{} ".format(prime))
    except Exception as Argument:
        print("Error! Wrong arguments\n.{}".format(Argument))
    if not silent:
        print("\nTime elapsed: {:.0f} ms".format((time.time() - s)*1000))
    if report:
        f.close()

main()