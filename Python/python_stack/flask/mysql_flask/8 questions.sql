-- 1. What query would you run to get all the countries that speak Slovene?
-- Your query should return the name of the country, language and language percentage. 
-- Your query should arrange the result by language percentage in descending order. (1)
-- 
-- use world;
-- select c.name, l.language, l.percentage from languages l
-- left join countries c on l.country_code = c.code
-- where l.language = 'Slovene'
-- order by l.percentage desc

-- 2. What query would you run to display the total number of cities for each country? 
-- Your query should return the name of the country and the total number of cities. 
-- Your query should arrange the result by the number of cities in descending order. (3)
-- 
-- select co.name as country_name, count(ci.name) as city_count from countries co
-- left join cities ci on co.code = ci.country_code
-- group by co.name
-- order by city_count desc
 
-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? 
-- Your query should arrange the result by population in descending order. (1)

-- select ci.name, ci.population from cities ci left join
-- countries co on co.code = ci.country_code
-- where co.name = 'Mexico' and ci.population > 500000
-- order by population desc

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? 
-- Your query should arrange the result by percentage in descending order. (1)

-- select co.name, l.language, l.percentage from countries co left join
-- languages l on l.country_code = co.code
-- where l.percentage > 89
-- order by l.percentage desc

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)

-- select name as country_name, surface_area, population from countries where surface_area < 501 and population > 100000

-- 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)

-- select name as country_name, government_form, life_expectancy from countries where government_form like '%monarch%' and government_form like '%const%' and life_expectancy > 75
-- 
-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? 
-- The query should return the Country Name, City Name, District and Population. (2)

-- select co.name as country_name, ci.name as city_name, ci.district, ci.population from cities ci
-- left join countries co on co.code = ci.country_code
-- where ci.district like '%aires%' and ci.population > 500000
-- order by ci.population desc
-- 
-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
-- 
-- select region, count(name) as country_count  from countries 
-- group by region
-- order by country_count desc