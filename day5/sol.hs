
module Main where

import Data.List (sort, group)

type Point = (Int, Int)
type Line = (Point,Point)

sample :: [Line]
sample =
    [((0,9), (5,9))
    ,((8,0), (0,8))
    ,((9,4), (3,4))
    ,((2,2), (2,1))
    ,((7,0), (7,4))
    ,((6,4), (2,0))
    ,((0,9), (2,9))
    ,((3,4), (1,4))
    ,((0,0), (8,8))
    ,((5,5), (8,2))
    ]
    --[((1,1),(4,4))
    --,((1,3),(1,7))
    --,((5,1),(1,1))
    --,((1,2),(4,8))
    --]

line :: Line -> [Point]
line ((x0, y0), (x1, y1)) = zip (range x0 x1 dx) (range y0 y1 dy)
    where (dx, dy) = slope x0 y0 x1 y1

range :: Int -> Int -> Int -> [Int]
range a b d | d == 0 && a == b = [a,a..]
            | d > 0 = [a,(a+d)..b]
            | d < 0 = reverse [b,(b-d)..a]

slope x0 y0 x1 y1 = (dx, dy)
    where dx = (x1 - x0) `div` b
          dy = (y1 - y0) `div` b
          b = gcd (x1 - x0) (y1 - y0)

allPoints = concatMap line

parseLine :: String -> Line
parseLine = read
parse = map parseLine . lines

input = readFile "input.txt" >>= return . parse

dropUniq l = concat [x | x <- group l, length x >= 1]
countOverlaps l = length [x | x <- group (sort l), length x > 1]

-- a line is funky if it is not horizontal or verrtical
funky ((x0,y0), (x1,y1)) =  x0 /= x1 && y0 /= y1

--main = print . map (\(P(x0,y0),P(x1,y1))->slope x0 y0 x1 y1) $ sample
--main = print $ allPoints sample
main = do
    input <- input
    print $ countOverlaps $ allPoints $ filter (not . funky) $ sample
    print $ countOverlaps $ allPoints $ filter (not . funky) $ input
    print $ countOverlaps $ allPoints $ input
