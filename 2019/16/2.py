import numpy as np

import math
#inp="12345678"
#inp="03036732577212944063491565474664"
inp="59762574510031092870627555978901048140761858379740610694074091049186715780458779281173757827279664853239780029412670100985236587608814782710381775353184676765362101185238452198186925468994552552398595814359309282056989047272499461615390684945613327635342384979527937787179298170470398889777345335944061895986118963644324482739546009761011573063020753536341827987918039441655270976866933694280743472164322345885084587955296513566305016045735446107160972309130456411097870723829697443958231034895802811058095753929607703384342912790841710546106752652278155618050157828313372657706962936077252259769356590996872429312866133190813912508915591107648889331"#*10000
originalPattern=[0, 1, 0, -1]
size=len(inp)

inpArray=list(map(int,list(inp)))

res = (10000*inpArray)[int(inp[:7]):] # tail for part2
print(int(inp[:7]))
for _ in range(100):
  for i in range(len(res)-1,0,-1): 
    res[i-1] = (res[i-1]+res[i]) % 10
print(''.join(str(x) for x in res[:8]))