.mode column
.headers ON
SELECT title, name from book
INNER JOIN bookCreator  on bookCreator.bookId = book.id
INNER JOIN  creator on bookCreator.creatorId = creator.id
WHERE bookId = '4';
