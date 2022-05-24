const express = require('express');
const { createServer } = require('http');
const { ApolloServer } = require('apollo-server-express');
const { gql } = require('apollo-server')

const authors = [
  { id: 1, name: 'J. K. Rowling' },
  { id: 2, name: 'J. R. R. Tolkien' },
  { id: 3, name: 'Brent Weeks' },
]
/*


*/

const books = [
  { id: 1, name: 'Harry Potter and the Chanber of Secrets', authorId: 1 },
  { id: 2, name: 'Harry Potter and the Prisoner of Azkaban', authorId: 1 },
  { id: 3, name: 'Harry Potter and the Goblet of Fire', authorId: 1 },
  { id: 4, name: 'The Fellowship of the Ring', authorId: 2 },
  { id: 5, name: 'The Two Towers', authorId: 2 },
  { id: 6, name: 'The Return of the King', authorId: 2 },
  { id: 7, name: 'The Way of Shadows', authorId: 3 },
  { id: 8, name: 'Beyond the Shadows', authorId: 3 },
]

//
//

const typeDefs = gql`
  "A book, identified by some parameters"
  type Book {
    "Unique identifier"
    id: Int!
    "The name of the book"
    name: String!
    "The ID of the author"
    authorId: Int!
    "A link to Author record / object"
    author: Author
  }

  type Author {
    id: Int!
    name: String!
    books: [Book]
  }

  type Query {
    book(id: Int): Book
    books: [Book]
    authors: [Author]
    author(id: Int): Author
  }

  type Mutation {
    addBook(name: String!, authorId: Int): Book
    updateBook(id: Int!, name: String, authorId: Int): Book
    deleteBook(id: Int!): Book
  }
`;

const resolvers = {
  Query: {
    book: (parent, { id } ) => {
      console.log("book:", parent, id)
      return books.find(book => book.id === id)
    },
    books: () => {
      console.log("books: ", books)
      return books
    },
    authors: () => authors,
    author: (_, id) => (authors.find(author => author.id === id)),
  },

  Author: {
    books: (author) => {
      console.log("author:", author);
      return books.filter((book) => book.authorId === author.id);
    }
  },

  Book: {
    author: (book) => {
      console.log("book:", book)
      return authors.find((author) => author.id === book.authorId);
    }
  },

  Mutation: {
    addBook: (parent, args) => {
      console.log("addBook", parent, args)
      const book = {
        id: books.length + 1,
        name: args.name,
        authorId: args.authorId
      }
      console.log(book)
      books.push(book)
      return book
    },
    deleteBook: (parent, args) => {
      console.log("deleteBook", args.id);
      book = books.find((book) => book.id === args.id)
      books.pop(book);
      return book
    }
  },

}

async function startApolloServer(typeDefs, resolvers) {
  //Express Server
  const app = express();
  const httpServer = createServer(app);

  //Apollo Server
  const apolloServer = new ApolloServer({
    typeDefs,
    resolvers,
    context: ({ req, connection }) => ({
      token: req ? req.headers.authorization : connection.context.authorization,
    }),
  });

  await apolloServer.start();

  apolloServer.applyMiddleware({ app, path: "/graphql" });

  //const httpServer = createServer(app);
  //server.installSubscriptionHandlers(httpServer);

  await new Promise(resolve => httpServer.listen({ port: 5500 }, resolve));
  console.log("Apollo Server is running on: http://localhost:5500/graphql");
}

startApolloServer(typeDefs, resolvers);
