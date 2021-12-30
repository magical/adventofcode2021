import Debug.Trace (trace)
import Data.List

die = [1,2,3]
thrice = do
    a <- die
    b <- die
    c <- die
    return (a+b+c)

type Qstate a = [(a,Integer)]

qstate a = map (\a->(head a, fromIntegral $ length a)) . group . sort $ a
single a = [(a,1)]
zero = [] :: Qstate a

bind :: (Ord a,Ord b) => Qstate a -> (a -> Qstate b) -> Qstate b
bind s f = foldr merge zero [[(y,n*m) | (y,m) <- f x] | (x,n) <- s]

qmap :: (Ord a, Ord b) => (a -> b) -> Qstate a -> Qstate b
qmap f q = foldr merge zero $ map (\(x,n) -> [(f x,n)]) q


-- doesn't work. can't class constrain a monad
-- see eg https://stackoverflow.com/questions/22313903/class-contraints-for-monads-and-monad-functions

--newtype Qstate a = Qstate [(a,Int)]
--get (Qstate a) = a
--
--instance Ord a => Monad (Qstate a) where
--    return x = Qstate [(x,1)]
--    (Qstate a) >>= f = Qstate $ bind a (get . f)

mod10 x = ((x-1) `mod` 10) + 1

threshold = 21
play start = do
    let d = qstate thrice
    let f a = a `bind` \(x,s) ->
                if s >= threshold then zero else
                    d `bind` \y ->
                        let z = mod10 (x+y) in single (z,s+z)
    let states = iterate f (single (start,0))
    let scores = map (qmap snd) states
    takeWhile (not . null) $ scores

-- precondition: as and bs must be sorted
merge as [] = as
merge [] bs = bs
merge ((a,an):as) ((b,bn):bs) =
    case compare a b of
        EQ -> (a,an+bn):merge as bs
        LT -> (a,an):merge as ((b,bn):bs)
        GT -> (b,bn):merge ((a,an):as) bs

main = do
    let d = qstate thrice
    print $ foldl1 merge (take 100 $ repeat d)
    print $ d
    print $ d `bind` (\x-> d `bind` \y -> qstate [(x,y)])
    --putStrLn ""
    --sequence $ map print $ takeWhile (not . null) $ play 4
    --putStrLn ""
    --sequence $ map print $ takeWhile (not . null) $ play 8
    let playerA = play 4
    let playerB = play 1
    let f a b = flip map (zip a b) (\(a,b) ->
                    a `bind` \x ->
                        b `bind` \y ->
                            if y >= threshold && x < threshold then single () else zero)
    print $ f playerA playerB
    let wins a b = sum $ map snd $ concat $ f a b
    print $ wins ([]:playerB) playerA
    print $ wins playerA playerB
