CREATE TABLE donuts AS
  SELECT "cake" AS kind, "chocolate" AS flavor UNION
  SELECT "cake"        , "lemon" UNION
  SELECT "cake"        , "vanilla" UNION
  SELECT "raised"      , "cinnamon" UNION
  SELECT "raised"      , "chocolate";

CREATE TABLE prices AS
  SELECT "cake" as dough, 2 as price UNION
  SELECT "raised"       , 3;

CREATE TABLE quantity AS 
  SELECT "chocolate" AS choice, 6 as k UNION
  SELECT "cinnamon"           , 3 UNION
  SELECT "vanilla"            , 3;

CREATE TABLE result AS
  SELECT "chocolate" AS flavor, 12 as total UNION
  SELECT "cinnamon"           , 9 UNION
  SELECT "vanilla"            , 6; 

SELECT flavor, MIN(k * price) AS total FROM quantity, donuts, prices WHERE kind = dough AND flavor = choice GROUP BY flavor;

CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" AS course UNION
  SELECT "Wheeler"    , "61A" UNION
  SELECT "RSF"        , "61B";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 AS seats UNION
  SELECT "Wheeler"    , 700 UNION
  SELECT "310 Soda"   , 40;

SELECT course, SUM(seats) AS seats FROM finals, sizes WHERE hall = room GROUP BY course HAVING COUNT(*) > 1;

CREATE TABLE s AS
  SELECT 979 as num UNION SELECT 1721 UNION SELECT 366 UNION SELECT 299 UNION SELECT 677 UNION SELECT 1456;

SELECT a.num, b.num FROM s AS a, s AS b WHERE a.num < b.num AND a.num + b.num = 2020;

