
module Main where
import Data.Char (digitToInt, intToDigit, isHexDigit)
import Data.Bits (testBit)
import Data.List (findIndex)
import Control.Monad (ap)
import Debug.Trace (trace)

-- hex

unhex :: Char -> [Int]
unhex c = [fromEnum $ testBit (digitToInt c) e | e <- [3,2,1,0]]
unhexStr = concatMap unhex . filter isHexDigit

bitsToInt = foldl (\a b->a*2+b) 0

printBits = print . map intToDigit

-- parsing

data Packet = Lit Int Int Int
            | Op Int Int [Packet]
    deriving (Eq, Ord, Show)

version (Lit v _ _) = v
version (Op v _ _) = v

parse :: [Int] -> Packet
parse = fst . parse1
parse1 l = case t of
        4 -> (Lit v t x, r2)
        _ -> (Op v t s, r3)
    where (v, r0) = parseVersion l
          (t, r1) = parseType r0
          (x, r2) = readLiteral r1
          (s, r3) = parseSubpackets r1

readInt n l = (bitsToInt $ take n l, drop n l)

parseVersion = readInt 3
parseType = readInt 3
readLiteral l = (bitsToInt bs, rest)
    where (bs, rest) = readChunked l
readChunked (x:rest) | x == 0 = (take 4 rest, drop 4 rest)
                     | x == 1 = (take 4 rest ++ bs, rest')
    where (bs, rest') = readChunked $ drop 4 rest

parseSubpackets (0:rest) = (pkts', rest')
    where (len, r0) = readInt 15 rest
          (pktdata, rest') = splitAt len r0
          pkts = iterState parse1 pktdata
          Just index = findIndex (null . snd) pkts
          pkts' = map fst $ take (index+1) pkts

parseSubpackets (1:rest) = (pkts, rest')
    where (count, r0) = readInt 11 rest
          pkts = take count $ map fst $ iterState parse1 r0
          rest' = snd (iterState parse1 r0 !! (count-1))
          --take count parsePackets rest
          --(pkts, r1) = parse rest:(parse r1)

iterState f s = (x,s'):iterState f s' where (x,s') = f s

--

versionSum :: Packet -> Int
versionSum (Lit v _ _) = v
versionSum (Op v _ s) = v + sum (map versionSum s)

eval :: Packet -> Int
eval (Lit _ _ v) = v
eval (Op _ 0 s) = sum (map eval s)
eval (Op _ 1 s) = product (map eval s)
eval (Op _ 2 s) = foldr1 min (map eval s)
eval (Op _ 3 s) = foldr1 max (map eval s)
eval (Op _ 5 [a,b]) = if eval a > eval b then 1 else 0
eval (Op _ 6 [a,b]) = if eval a < eval b then 1 else 0
eval (Op _ 7 [a,b]) = if eval a == eval b then 1 else 0

--

input = readFile "input"
main = do
    ap trace (print . parse      . unhexStr) $ "D2FE28"
    ap trace (print . parse      . unhexStr) $ "38006F45291200"
    ap trace (print . versionSum . parse . unhexStr) $ "A0016C880162017C3686B18A3D4780"
    input <- input
    print . versionSum . parse . unhexStr $ input
    print . eval       . parse . unhexStr $ input
