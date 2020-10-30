class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
        self.computeDifference()

    def computeDifference(self):
        self.maximumDifference = 0

        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                if i != j:
                    difference = abs(self.__elements[i] - self.__elements[j])

                    if difference > self.maximumDifference:
                        self.maximumDifference = difference

        

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)