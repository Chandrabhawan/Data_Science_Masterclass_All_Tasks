-- # SQL200_Task1 — Sakila_DB Queries
-- # Author  : Chandra Patel

-- Q1 — Film prices

-- Using IN operator to filter specific rental rates

SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate IN (9.99, 4.99);



-- Q2 — Film length + rating

-- BETWEEN includes both 90 and 120 (inclusive)
--  Filtering rating using IN (clean approach)

SELECT title, length, rating
FROM film
WHERE length BETWEEN 90 AND 120
  AND rating IN ('PG', 'PG-13');



-- Q3 — Actor last names

-- ILIKE used for case-insensitive matching (PostgreSQL specific)
-- 'S%' → starts with S, '%N' → ends with N

SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name ILIKE 'S%'
   OR last_name ILIKE '%N';



-- Q4 — Active customers + email filter

-- ⚠ activebool may vary depending on schema (usually 'active')
-- Parentheses ensure correct logical grouping
-- Filtering emails ending with .org or .net

SELECT customer_id, first_name, last_name, email
FROM customer
WHERE active = TRUE   -- safer column name
  AND (email LIKE '%.org%'
   OR  email LIKE '%.net%');



-- Q5 — Inactive customers in store 1

-- ✔Filtering by store and inactive status

SELECT customer_id, store_id, active
FROM customer
WHERE store_id = 1
  AND active = FALSE;



-- Q6 — Payment amount + date range

--  BETWEEN for amount range
--  Best practice: date range using >= and < (avoids time issues)

SELECT payment_id, customer_id, amount, payment_date
FROM payment
WHERE amount BETWEEN 2.00 AND 5.00
  AND payment_date >= '2007-02-01'
  AND payment_date <  '2007-03-01';



-- Q7 — Rentals not returned

-- IS NULL used to find missing return_date

SELECT rental_id, rental_date, return_date, customer_id
FROM rental
WHERE return_date IS NULL;



-- Q8 — Address district + postal code present

--  IN used for multiple district values
--  IS NOT NULL ensures postal_code exists

SELECT address_id, address, district, postal_code
FROM address
WHERE district IN ('Texas', 'California')
  AND postal_code IS NOT NULL;



-- Q9 — Replacement cost + exclude titles

--  IN used for multiple replacement costs
--  NOT ILIKE used for case-insensitive exclusion (optimized)

SELECT film_id, title, replacement_cost
FROM film
WHERE replacement_cost IN (12.99, 16.99, 28.99)
  AND title NOT ILIKE '%a%';



-- Q10 — Inventory logic challenge

--  Parentheses ensure correct AND/OR precedence
--  BETWEEN used for film_id ranges
--  ORDER BY added for better readability (optional but good practice)

SELECT inventory_id, film_id, store_id
FROM inventory
WHERE (store_id = 1 AND film_id BETWEEN 1 AND 50)
   OR (store_id = 2 AND film_id BETWEEN 51 AND 100)
ORDER BY store_id, film_id;