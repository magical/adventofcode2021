import Debug.Trace (trace)

die = cycle [1..100]
moves = map sum $ chunk 3 die

chunk n a = take n a : chunk n (drop n a)

pair (a:b:rest) = (a,b):pair rest
unpair ((a,b):rest) = a:b:unpair rest
split = unzip . pair

double :: (a -> b) -> ((a,a) -> (b,b))
double f (x,x') = (f x, f x')

double2 :: (a -> b -> c) -> ((a,a) -> (b,b) -> (c,c))
double2 f (x,x') (y,y') = (f x y, f x' y')

mod10 x = ((x-1) `mod` 10) + 1

spaces start = map (double mod10) . scanl (double2 (+)) start
play start x = scanl (double2 (+)) (0,0) $ tail $ spaces start x

part1 start = trace (show score) $trace (show dieRolls)$ score*dieRolls
    where scores = unpair $ tail $ play start $ pair moves
          (scores',rest) = span (<1000) scores
          n = length scores'
          dieRolls = n*3 + 3
          score = last scores'

main =  do
    print $ part1 (4,8) -- sample
    print $ part1 (4,1) -- input
