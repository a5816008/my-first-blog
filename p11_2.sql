.mode column
.headers ON
SELECT bookId, name from bookCreator
INNER JOIN creator on bookCreator.creatorId = creator.id WHERE bookId = '4';
