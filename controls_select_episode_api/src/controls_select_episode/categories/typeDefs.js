export const categoryTypeDef = `
  type Category {
      id: Int!
      name: String!
  }
  input CategoryInput {
      name: String!
      description: String!
  }`;

export const categoryQueries = `
      allCategories: [Category]!
      categoryById(id: Int!): Category!
  `;

export const categoryMutations = `
    createCategory(category: CategoryInput!): Category!
    updateCategory(id: Int!, category: CategoryInput!): Category!
    deleteCategory(id: Int!): Int
`;


export const usertTypeDef = `
  type Response {
    msj: String!
  }
  input UserInput {
    user_name : String!
    fristName : String!
    lastName : String!
    password : String!
  }`;
export const userQueries = `
      
  `;
export const UserMutations = `
    createUser(user: UserInput!): Response!
`;