class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5


"""f(n) = 1/n             -> 1st person picks his own seat
    + 1/n * 0                -> 1st person picks last one's seat
	+ (n-2)/n * (            ->1st person picks one of seat from 2nd to (n-1)th
        1/(n-2) * f(n-1)     -> 1st person pick 2nd's seat
        1/(n-2) * f(n-2)     -> 1st person pick 3rd's seat
        ......
        1/(n-2) * f(2)       -> 1st person pick (n-1)th's seat
	)

=> f(n) = 1/n * ( f(n-1) + f(n-2) + f(n-3) + ... + f(1) )

Now, you can easily get
f(1) = 1
f(2) = 1/2
f(3) = 1/2
Proof for why it's 1/2 when n > 2
From the proof above we know that

when n > 2,
f(n) = 1/n * ( f(n-1) + f(n-2) + ... + f(1) )
f(n-1) = 1/(n-1) * (f(n-2) + f(n-3) + ... + f(1))

because, the 2nd equation requires n-1 > 1
So that

n * f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(1)
(n-1) * f(n-1) = f(n-2) + f(n-3) + ... + f(1)
Substract both sides, we get

n * f(n) - (n-1)*f(n-1) = f(n-1)

=> n * f(n) = n * f(n-1)
=> f(n) = f(n-1) , when n > 2
Then we know,
f(1) =1
f(2) = 1/2
From here
f(n) = f(n-1) = ... = f(2) = 1/2"""
