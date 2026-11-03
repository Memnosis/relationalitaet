"""Synthetic MINI-OBS-01 test. No autonomous intelligence demonstrated."""
import time
def faulty_skill(x):return x*x+(1 if x%17==0 else 0)
def independent_check(x,y):return y==x*x
xs=range(1,10001)
start=time.perf_counter();base=[faulty_skill(x) for x in xs];base_time=time.perf_counter()-start
start=time.perf_counter();observed=[(faulty_skill(x),independent_check(x,faulty_skill(x))) for x in xs];obs_time=time.perf_counter()-start
assert sum(y!=x*x for x,y in zip(xs,base))==588
assert sum(not ok for _,ok in observed)==588
print(dict(cases=10000,incorrect=588,detected=588,base_seconds=base_time,observed_seconds=obs_time))
