use sakila;

-- 1a. Display the first and last names of all actors from the table actor. 

SELECT first_name ,last_name FROM actor ;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

SELECT upper(concat_ws (" ", first_name ,last_name)) as 'Actor name' FROM actor ;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?

select actor_id as ID , first_name as 'first name', last_name as 'last name'
from actor
where first_name = 'joe';

-- 2b. Find all actors whose last name contain the letters GEN:

select actor_id as ID , first_name as 'first name', last_name as 'last name'
from actor
where last_name like '%gen%';

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:

select actor_id as ID , first_name as 'first name', last_name as 'last name'
from actor
where last_name like '%li%'
order by last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:

select country_id, country
from country
where country in ('Afghanistan', 'Bangladesh', 'China');

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.

ALTER TABLE `sakila`.`actor` 
ADD COLUMN `middle_name` VARCHAR(45) NULL AFTER `first_name`;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.

ALTER TABLE `sakila`.`actor` 
CHANGE COLUMN `middle_name` `middle_name` BLOB NULL DEFAULT NULL ;

-- 3c. Now delete the middle_name column.

ALTER TABLE `sakila`.`actor` 
DROP COLUMN `middle_name`;

-- 4a. List the last names of actors, as well as how many actors have that last name.

select last_name, count(*) 
from actor
group by last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names 
-- that are shared by at least two actors

select last_name, count(*) 
from actor
group by last_name
having count(*) >= 2;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name 
-- of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

update actor 
set first_name = 'HARPO'
where last_name = 'WILLIAMS' and first_name = 'GROUCHO';

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after 
-- all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change 
-- the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT 
-- TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)

UPDATE actor 
	set first_name = CASE WHEN first_name = 'HARPO' THEN 'GROUCHO' else 'MUCHO GROUCHO'  END
 WHERE actor_id = 172 ;
 

 
-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?

show CREATE table actor;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

select first_name , last_name, address, district, postal_code
from staff s
left join address a on s.address_id = a.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.

select  last_name, first_name, sum(amount) as 'Total Amount Rung-Up'
from staff s
left join payment p  on s.staff_id = p.staff_id
where p.payment_date between '2005-08-01' and  '2005-08-31'
group by s.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

select f.title, count(*) as 'Number of Actors'
from film f 
inner join film_actor fa on f.film_id = fa.film_id
group by fa.film_id;


-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?

select count(*) as 'Number of Copies of ''Hunchback Impossible'' '
from inventory i
inner join film f on i.film_id = f.film_id 
where f.title='Hunchback Impossible';

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:

select first_name, last_name , sum(p.amount) as 'Total Amount Paid'
from customer c
inner join payment p on c.customer_id = p.customer_id
group by c.customer_id
order by last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
-- films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of 
-- movies starting with the letters K and Q whose language is English.

select title from film 
where (title like 'K%' or title like  'Q%')
and language_id in (select language_id from language where name ='English');


-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.

select first_name, last_name 
from actor a
where actor_id in (
	select actor_id 
    from film_actor 
	where film_id in (
		select film_id 
        from film 
        where title='Alone Trip'
        )
	);


-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all 
-- Canadian customers. Use joins to retrieve this information.
select last_name, first_name, email from customer where address_id in (
select address_id 
from address where city_id in (
	select city_id 
    from city 
    where country_id in (select country_id from country where country ='Canada')
)
);

select  last_name, first_name, email 
from customer 
inner join address on customer.address_id = address.address_id
	inner join city on address.city_id = city.city_id
		inner join country on city.country_id = country.country_id
			where country = 'Canada';
 
 
-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all 
-- movies categorized as famiy films.

select f.title 
from film f
inner join film_category fc on f.film_id = fc.film_id
	inner join category c on fc.category_id = c.category_id
    where upper(c.name) = 'FAMILY';
		

-- 7e. Display the most frequently rented movies in descending order.

select title , rental_date
from rental 
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on inventory.film_id = film.film_id
order by rental_date desc, title;



-- 7f. Write a query to display how much business, in dollars, each store brought in.

select store.store_id, address.address, city.city, sum(amount)

from payment 
	inner join staff on payment.staff_id = staff.staff_id
    inner join store on staff.store_id = store.store_id
    inner join address on store.address_id = address.address_id
    inner join city on address.city_id = city.city_id
group by payment.staff_id;


-- 7g. Write a query to display for each store its store ID, city, and country.


select store.store_id, city.city, country.country
from store 
    inner join address on store.address_id = address.address_id
    inner join city on address.city_id = city.city_id
    inner join country on city.country_id = country.country_id;


-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, 
-- film_category, inventory, payment, and rental.)

select category.category_id, category.name, sum(amount) as revenue
from payment
	inner join rental  on payment.rental_id = rental.rental_id
    inner join inventory on rental.inventory_id = inventory.inventory_id
    inner join film_category  on  inventory.film_id = film_category.film_id
	inner join category  on  film_category.category_id = category.category_id
group by category.category_id, category.name
order by sum(amount) desc
limit 5;



-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

create view vw_top_five_genres as
select category.category_id, category.name, sum(amount) as revenue
from payment
	inner join rental  on payment.rental_id = rental.rental_id
    inner join inventory on rental.inventory_id = inventory.inventory_id
    inner join film_category  on  inventory.film_id = film_category.film_id
	inner join category  on  film_category.category_id = category.category_id
group by category.category_id, category.name
order by sum(amount) desc
limit 5;


-- 8b. How would you display the view that you created in 8a?

select * from vw_top_five_genres;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.

drop view vw_top_five_genres;
