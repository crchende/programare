const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLString
} = require('graphql')
const app = express();

const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: "HelloWorld",
    fields: () => ({
      message1: {
        type: GraphQLString,
        resolve: () => 'Hello world'
      }
    })
  })
})

app.use('/graphql', graphqlHTTP({
  schema: schema,
  graphiql: true
}));
app.listen(5500, () => console.log('Server Running'));
