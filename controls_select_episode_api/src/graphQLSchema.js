import merge from 'lodash.merge';
import GraphQLJSON from 'graphql-type-json';
import { makeExecutableSchema } from 'graphql-tools';

import { mergeSchemas } from './utilities';

import {
    categoryMutations,
    categoryQueries,
    categoryTypeDef,
    usertTypeDef,
    userQueries,
    UserMutations,
    authTypeDef,
    authQueries,
    authMutations

} from './controls_select_episode/categories/typeDefs';

import categoryResolvers from './controls_select_episode/categories/resolvers';

// merge the typeDefs
const mergedTypeDefs = mergeSchemas(
    [
        'scalar JSON',
        categoryTypeDef,
        usertTypeDef,
        authTypeDef,
    ], [
        categoryQueries,
        userQueries,
        authQueries,
    ], [
        categoryMutations,
        UserMutations,
        authMutations,
    ]

);

// Generate the schema object from your types definition.
export default makeExecutableSchema({
    typeDefs: mergedTypeDefs,
    resolvers: merge({ JSON: GraphQLJSON }, // allows scalar JSON
        categoryResolvers
    )
});