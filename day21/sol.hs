import Debug.Trace (trace)
import Data.List (group,sort)

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

---------------------------

dice = [1,2,3]
thrice = do
    a <- dice
    b <- dice
    c <- dice
    return (a+b+c)

-- qstate is a set of states and the number of worldlines which lead to that state
type Qstate a = [(a,Integer)]

qstate a = map (\a->(head a, fromIntegral $ length a)) . group . sort $ a
single a = [(a,1)]
zero = [] :: Qstate a

bind :: (Ord a,Ord b) => Qstate a -> (a -> Qstate b) -> Qstate b
bind s f = foldr merge zero [[(y,n*m) | (y,m) <- f x] | (x,n) <- s]

qmap :: (Ord a, Ord b) => (a -> b) -> Qstate a -> Qstate b
qmap f q = foldr merge zero $ map (\(x,n) -> [(f x,n)]) q

-- precondition: as and bs must be sorted
merge as [] = as
merge [] bs = bs
merge ((a,an):as) ((b,bn):bs) =
    case compare a b of
        EQ -> (a,an+bn):merge as bs
        LT -> (a,an):merge as ((b,bn):bs)
        GT -> (b,bn):merge ((a,an):as) bs

-- a qstate is almost a monad, but not quite:
-- a monad must be able to contain any type, but our
-- merge function requires that the state type be orderable.
-- this means that you can have a Qstate of a function, for
-- instance, which would severely limit the kinds of monadic
-- operations that we could use.
--
-- see eg https://stackoverflow.com/questions/22313903/class-contraints-for-monads-and-monad-functions
--
--      newtype Qstate a = Qstate [(a,Int)]
--      get (Qstate a) = a
--
--      instance Ord a => Monad (Qstate a) where
--          return x = Qstate [(x,1)]
--          (Qstate a) >>= f = Qstate $ bind a (get . f)
--
-- the upshot is that we can't use do notation with qstate
-- and instead have to write out the bind applications manually.
-- kind of clunky but it works well enough.

-- players' actions don't affect the other player at all
-- so we can just run each player independently and combine them later.
threshold = 21
dirac start = do
    let d = qstate thrice
    let f a = a `bind` \(x,s) ->
                if s >= threshold then zero else
                    d `bind` \y ->
                        let z = mod10 (x+y) in single (z,s+z)
    let states = iterate f (single (start,0))
    let scores = map (qmap snd) states
    takeWhile (not . null) $ scores

part2 start = do
    let d = qstate thrice
    let playerA = dirac (fst start)
    let playerB = dirac (snd start)
    let f a b = flip map (zip a b) (\(a,b) ->
                    a `bind` \x ->
                        b `bind` \y ->
                            if y >= threshold && x < threshold then single () else zero)
    let wins a b = sum $ map snd $ concat $ f a b
    max (wins ([]:playerB) playerA)
        (wins playerA playerB)


main =  do
    print $ part1 (4,8) -- sample
    print $ part1 (4,1) -- input
    putStrLn ""
    print $ part2 (4,8) -- sample
    print $ part2 (4,1) -- input


