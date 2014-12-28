Fun with hashmaps
=

Once upon a time in an interview I did a HashMap implementation on the whiteboard.
I would like to remember what I did, because it was pretty cool.

It started with a small mask applied to the hash of the immutable key, giving an index
into a table. Each table entry is a pair of things, one the hash of the key, and the other
a pointer to the data. Dictionaries in Python do not use linked lists so hash collisions
are not permitted. Table size is 2**n for an n-bit mask of the hash, and when a collision
results from an insertion, you need to increase n until there is no longer a collision.
Hashes are long enough to ensure that nonidentical keys always have nonidentical hashes.

When you grow the size of the list, you probably need to move some objects to the new
area. That's an order-N operation. You can grow the table with realloc, and then you
need to zero the new memory.

Here's a Python reference implementation. It would be good to put together a C
implementation when I get a moment.