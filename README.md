# Project Title

Monte Carlo Simulation

### Getting Started

Monte Carlo methods are essentially algorithms to utilize randomness to solve problems through _brute force_ methods. They are commonly used when it's difficult to model a situation using pure mathematical approaches. They give us the possibility to test multiple outcome possibilities to determine the best outcome. This is possible because all outcomes have _in theory_ a finite possibility to occur. With respect to finance, Monte Carlo simulations can be used to evaluate investments and risk analysis.

### Consider this gambling scenario

Where a user can roll a dice for an outcome of 1-100:

* If the user rolls a number between 1-50 the "house" wins
* If the user rolls a number between 51-99 the user wins
* If the user rolls a 100, the "house" wins

With this, the house holds a mere 1% edge over the long run. We can first create our __Simple Bettor__. His role is basically to bet a set amount each and every time. If he wins he will bet _x_ amount. If he loses, he will bet _x_ amount. Notice how his bet is independent of the result of the previous round.

Alternatively, we can create a __better bettor__ that actually utilizes a Martingale Betting Strategy to improve his odds. We can have two versions of him/her. The first iteration would be utilizing a simple double betting strategy. If he loses the previous round, he will bet _2x_ his previous wager.

The second iteration is our __multiple bettor__. He is where we can utilize a Monte Carlo simulation to determine the best multiple we can utilize to maximize the profit one makes, and minimize the given risk that they could go broke.

 If he loses the previous round, he will bet _y(x)_ amount based upon the previous wager amount. This ___y___ multiple is determined by our simulation because we can simulate numerous worlds where the best multiple can be determined. _Important_: We are utilizing the result of our __bettor bettor__ as a benchmark to determine if we did better.

## Results

__Simple Bettor__:

Given the preset odds of the game space, its understandable that the __simple bettor__ is going to fail. It's just a question of how long. Over a long enough time horizon, all players utilizing this strategy will go broke. It's fairly easy to visualize as well

![Simple_bettor](https://github.com/jaredconnor301/Monte_Carlo_Sim/blob/master/simple_bettor.png?raw=true)

__Double Bettor__:

The results of our __better bettor__ improves quite a bit. We can incorporate a functionality that breaks the bettor off after they go broke. Visualizing the results of multiple simulations of this kind of bettor gives us a vastly different understanding of the game's result.

![Double_bettor](https://raw.githubusercontent.com/jaredconnor301/Monte_Carlo_Sim/master/double_bettor.png?raw=true)

__Multiple Bettor__:

We can visualize that utilizing the martingale strategy changes the aspect of risk that we should care about. In the short run, multiple players actually makes quite a bit more than the __simple bettor__ game, but assumed more risk. Over the long run, what comes into question is the _life expectancy_ of the bettors. The simulation life is substantially higher than the previous game, but still with a limited horizon. We could incorporate another simulation even to understand how long this time horizon is.

#### Stats:

We can generate general statistics that we can utilize as a benchmark for the next simulation we'll run. The __double bettor__ simulation yielded us these stats:

__Bust rate (the rate at attrition): 31.325__
__Profit rate (rate which bettors earn a profit): 63.208__

Now is where the fun comes. By utilizing these statistics, we can run multiple world simulations by adjusting the multiple (remember the _y(x)_) to maximize these statistics.

![Multiple_bettor](https://github.com/jaredconnor301/Monte_Carlo_Sim/blob/master/Results.png?raw=true)

So we can see that the best multiple is .4432 and yields the stats of:

* __Bust rate: 8__
* __Profit rate: 28900.00__

---------------------------------------------------------------------------------------------------------------------------









## TD;DL

We simulated a Martingale Betting strategy with a Monte_Carlo_Sim to find the bettor can maximize risk-adjusted returns by betting .4432 of the previous bet.

# Further Research

* [Monte Carlo Simulations](https://en.wikipedia.org/wiki/Monte_Carlo_method)
* [Martingale Betting System](https://en.wikipedia.org/wiki/Martingale)
* Investigate the average time horizon of our Martingale Strategy

### Built With

* [Python 3.6](https://docs.python.org/3/)

* [jaredconnor301](https://github.com/jaredconnor301)

### Acknowledgments

* Harrison - *Initial Build* - [sentdex](https://github.com/Sentdex)
* [sentdex YouTube](https://www.youtube.com/results?search_query=sentdex)
