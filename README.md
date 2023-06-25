# Composite

Composite lets clients treat individual objects and compositions of objects uniformly.

Composite Pattern is useful when:
- You want to represent part-whole hierarchies of objects
- You want clients to be able to ignore the difference between compositions of objects and individial objects

**Benefits:**

- Whereever client code expects a primitive object, it can also take a composite object
- Makes the client simple (by being able to treat all objects in the same way)
- Makes it easier to add new kinds of components

**Consequence:**

- Can make the design overly general. It makes it harder to restict the components of a composite.
