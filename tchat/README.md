## Completion style model vs Conversational style

An LLM is a computer program that has been fed enough examples to be able to recognize and interpret human language or other types of complex data. Many LLMs are trained on data that has been gathered from the Internet — thousands or millions of gigabytes' worth of text. But the quality of the samples impacts how well LLMs will learn natural language, so an LLM's programmers may use a more curated data set.

LLMs use a type of machine learning called deep learning in order to understand how characters, words, and sentences function together. Deep learning involves the probabilistic analysis of unstructured data, which eventually enables the deep learning model to recognize distinctions between pieces of content without human intervention.

LLMs are then further trained via tuning: they are fine-tuned or prompt-tuned to the particular task that the programmer wants them to do, such as interpreting questions and generating responses, or translating text from one language to another.

Completion style model tries to assume what could the whole sentence possibly be if it's incomplete. The LLM normally follows the completion model. A lot of LangChain assumes you are using a completion model.

Conversational style model needs more work since we need to send entire chat history.

User/Human -> the message that user types
Assistant/AI -> The chatbot
System -> the system is how developer control chatbot to behave in a certain way. It customizes the response we get.


## Memory

the ability to store information about past interactions "memory". LangChain provides a lot of utilities for adding memory to a system. These utilities can be used by themselves or incorporated seamlessly into a chain.

1. ConversationTokenBufferMemory - Completion
2. CombinedMemory - Completion
3. ConversationBufferWindowMemory - Completion
4. ConversationBufferMemory - Conversational(AI and Human messages are stored)

