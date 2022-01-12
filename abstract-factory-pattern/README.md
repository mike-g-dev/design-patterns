# ABSTRACT FACTORY PATTERN

# TOP LEVEL 
This is a "creational" design pattern which
lets users create entire "product" families without
directly specifying their implementation when there is 
a need to create them. Fully decouples creation of products from 
their use. 

We use an abstract factory class to specify an 
interface for creating products that we let 
concrete factories implement. This allows 
use cases of products to depend upon this abstract factory
and not its specific implementations. It nicely encapsulates the
objects used to satisfy a use case from the actual procedural use of 
them. Each concrete factory allows designers to create specific variations of
the products. 

To create a new product, simply extend the abstract factory and pass it
to the application code. 