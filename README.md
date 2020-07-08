# Number2Word Certi Challenge
Technical leader code challenge for Fundação Certi.

## Introduction
Number2Word is an application used to convert integer numbers to its word. It has a Python back-end, which generates an API responsible for the word output. For practical reasons, Docker was used to create a container for the application, making it easier to use it.

Additionally, a simple interface was built using Angular, displaying the number-2-word conversions done according to the timestamp.

![number2wordGif](https://i.imgur.com/GfxQpMX.gif)

### Architecture
#### Design Pattern
The design pattern used for this project was the [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern) due to the non-exposition of the implementation and sequential manipulations done with the elements sent from the client side. Therefore, its easier to handle objects collections by decoupling it through the several business rules of the application.

However, by following the SOLID principles and good code practices, the [Factory pattern](https://en.wikipedia.org/wiki/Factory_method_pattern) was also implemented in order to set the application as much as easy to integrate new features, if necessary. This pattern has a great approach to create an object without exposing its logic to the client by using a shared interface. Therefore, the factory is responsible for deciding which will be the class to handle the received container according to the input parameters.

#### Class UML
The Class UML structure is the one displayed below:

![Diagrama UML](https://i.imgur.com/EZlHcyD.png)

#### Virtual Environment
Since Python has no option for global or local installation like NPM, a virtual environment was created for this application. Therefore, the modules (dependencies) installed are already set in the virtual environment, without affecting the machine installations.

#### Definitions
##### APIServer
This class is responsible for the HTTP Server, which will be accessible from out sources in order to get the requests sent to it. It has only one route (the one used for sending the number). Due to the Angular visual interface, the CORS policy was changed to accept the requests sent from there.

##### NumberSeparatorFactory
Responsible for handling the instantiation of the separators according to the input parameters. Although there is only one kind of separator in this application, this makes future implementations easier to be developed, as described in the Design Patterns section.

##### Separator
Abstract class responsible for the first manipulation of the input number. It separates the digits of
each block (each hundreds, tens and units) and calls for a collection in order to store it.

##### NumberBlockSeparator
Concrete implementation of the Separator class. Specifically designed for this block-approach selected for the application.

##### Container
Abstract class where data will be stored. This class is accessed in order to be iterated by the Iterator class.

##### NumberBlocksCollection
Concrete implementation of the Container class. It calls the iterator factory for instantiating an iterator object.

##### IteratorFactory
Responsible for handling the instantiation of the separators according to the input parameters. Although there is only one kind of iterator in this application, this makes future implementations easier to be developed, as described in the Design Patterns section.

##### Iterator
Abstract class responsible for iterating between the elements of the container concrete implementation and calling the necessary methods to deal with them.

##### NumberBlocksIterator
This concrete implementation of the Iterator abstract class iterates between number blocks and send each one of them
to the Block Handler, where the number block will get its specific word. After that, the Composer Handler is responsible for
joining the two blocks applying or not any modifications in the sentences (e.g. "e", "mil").

##### BlockHandler
The Block Handler class is responsible for deciding which will be the word associated to each digit. It checks each
one of them and associates a word to it. In the end, having the word specified for each digit, it calls
Block Word Handler to define if any change in the block sentence is necessary (e.g. applying "e")

##### BlockWordHandler
Block word handler is responsible for manipulating the sentence of each block by adding the connectors to the words
of each digit, if necessary.

##### ComposerHandler
The Composer Handler verifies both sentences: [hundreds, tens, units] and [thousand hundreds, thousand tens and
thousand units]. It sets the manipulation necessary in both of them (such as adding "mil" and spaces) in order to
generate the final word for the number.

### Instructions
For executing this application, a docker image was created. Therefore, no dependencies installation is necessary. The dockerfile is already at the root folder of the repository.

- **First step**: Start Docker
- **Second step**: Inside the repository folder, open a terminal and execute *docker build . -t doc-number2word:v1.0*
- **Third step**: After building the image, run the container: *docker run -d -p 5000:5000 doc-number2word:v1.0*

***From this point on, the HTTP server is already running.***

To test it, you can execute *curl http://localhost:5000/x*, where "x" is the number you want to convert to word.

If you prefer to use the interface, after running the previous instructions:

- **First step**: Inside the repository folder, open a terminal and execute *npm start*
- **Second step**: Wait for the application to be loaded
- **Third step**: Open your browser and type *http://localhost:4200*

##### Resources
* Angular 8
* RxJS 6.5
* HTML5
* Javascript
* Bootstrap
* Python 3.7
* Flask
* PyTest
* Docker
