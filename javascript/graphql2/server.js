const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLString,
  GraphQLList,
  GraphQLInt,
  GraphQLNonNull
} = require('graphql')
const app = express();

const authors = [
  { id: 1, name: 'J. K. Rowling' },
  { id: 2, name: 'J. R. R. Tolkien' },
  { id: 3, name: 'Brent Weeks' },
]

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

const AuthorType = new GraphQLObjectType({
  name: 'Author',
  description: 'This reprents an author of a book',
    fields: () => ({
    id: { type: GraphQLNonNull(GraphQLInt) },
    name: { type: GraphQLNonNull(GraphQLString) },
    books: {
      type: GraphQLList(BookType),
      resolve: (author) => {
        return books.filter(book => author.id === book.authorId)
      }
    }
  })
})

const BookType = new GraphQLObjectType({
  name: 'Book',
  description: 'This represents a book writen by an author',
  fields: () => ({
    id: { type: GraphQLNonNull(GraphQLInt) },
    name: { type: GraphQLNonNull(GraphQLString) },
    authorId: { type: GraphQLNonNull(GraphQLInt) },
    author: {
      type: AuthorType,
      resolve: (book) => {
        //console.log(book)
        //console.log(book.id)
        //console.log(authors.find(author => author.id === book.authorId))
        return authors.find(author => author.id === book.authorId)
      }
    }
  })
})

const RootQueryType = new GraphQLObjectType({
  name: 'Query',
  description: 'Root Query',
  fields: () => ({
    book: {
      type: BookType,
      description: "A Single Book",
      args: {
        id: { type: GraphQLInt },
      },
      resolve: (parent, args) => books.find(book => book.id === args.id),
    },
    books: {
      type: GraphQLList(BookType),
      description: "List of All Books",
      resolve: () => books
    },
    author: {
      type: AuthorType,
      description: "A Single Author",
      args: {
        id: { type:  GraphQLInt },
      },
      resolve: (parent, args) => authors.find(author => author.id === args.id),
    },
    authors: {
      type: new GraphQLList(AuthorType),
      description: "List of All Authors",
      resolve: () => authors
    }
  })
})

const RootMutationType = new GraphQLObjectType({
  name: "Mutation",
  description: "Root Mutation",
  fields: () => ({
    addBook: {
      type: BookType,
      description: "Add a book",
      args: {
        name: { type: GraphQLNonNull(GraphQLString) },
        authorId: { type: GraphQLNonNull(GraphQLInt) },
      },
      resolve: (parent, args) => {
        const book = {
          id: books.length + 1,
          name: args.name,
          authorId: args.authorId
        };
        books.push(book);
        return book;
      }
    },
    deleteBook: {
      type: BookType,
      description: "Delete a book",
      args: {
        id: { type: GraphQLInt },
      },
      resolve: (parent, args) => {
        const bookIndex = books.indexOf(books.find(book => book.id === args.id))
        console.log("args.id:", args.id, "index: ", bookIndex);
        if( bookIndex != -1 ) {
          //const book = books[bookIndex];
          //console.log("book: ", book);
          console.log("bookIndex: ", bookIndex);
          const dBook = books.splice(bookIndex, 1)[0]; //splice returns an array
          console.log("Deleted Book: ", dBook);
          console.log("Remained Books: ", books);
          return dBook;
        } else {
          console.log("ERROR: There is no book with id: ", args.id);
        }
      }
    },
    updateBook: {
      type: BookType,
      description: "Update a book",
      args: {
        id: { type: GraphQLInt },
        name: { type: GraphQLString },
        authorId: { type: GraphQLInt },
      },
      resolve: (parent, args) => {
        const bookIndex = books.indexOf(books.find(book => book.id === args.id))
        console.log("args.id:", args.id, "index: ", bookIndex);
        if( bookIndex != -1 ) {
          console.log("args.name: ", args.name);
          console.log("args.authorId: ", args.authorId);
          if( args.name !== undefined ) {
            books[bookIndex].name = args.name;
          }
          if( args.authorId !== undefined ) {
            checkAuthor = authors.find(auth => auth.id === args.authorId);
            console.log("checkAuthor: ", checkAuthor);
            if( checkAuthor !== undefined ) {
              console.log("HERE");
              books[bookIndex].authorId = args.authorId;
            } else {
              console.log("Unknown authorId: ", args.authorId, ". Not changing the initial value");
            }
          }
          return books[bookIndex];
        } else {
          console.log("ERROR: There is no book with id: ", args.id);
        }
      }
    }
  })
})

const schema = new GraphQLSchema({
  query: RootQueryType,
  mutation: RootMutationType,
})

app.use('/graphql', graphqlHTTP({
  schema: schema,
  graphiql: true
}));
app.listen(5500, () => console.log('Server is running on: http://localhost:5500/graphql'));
