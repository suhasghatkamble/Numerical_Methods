from numpy.random import SeedSequence, default_rng
ss = SeedSequence(12345)
# Spawn off 10 child SeedSequences to pass to child processes.
child_seeds = ss.spawn(10)
streams = [default_rng(s) for s in child_seeds] # Check
grandchildren = child_seeds[0].spawn(4)
grand_streams = [default_rng(s) for s in grandchildren]
print (grandchildren[0].pool)
print (grandchildren[1].pool)
print (grandchildren[2].pool)
print(grand_streams)

#10 children every children every children has 