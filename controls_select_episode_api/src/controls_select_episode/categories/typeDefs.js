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
  type user{
    id : Int!
    user_name : String!
    firstName : String!
    lastName : String!
    password : String!
  }

  type movie{
    id : Int!
    name : String!
    director : String!
    averge_score : String!
  }

  type serie{
    id : Int!
    name : String!
    director : String!
    averge_score : String!
  }
  
  type score{
    user_name : String!
    moive_serie_name : String!
    score : Float!
    description : String!
  }
  input UserInput {
    user_name : String!
    firstName : String!
    lastName : String!
    password : String!
  }
  input SerieScore {
    user_name : String!
    serie_name : String!
    score : Float!
    description : String!
  }
  input MovieScore {
    user_name : String!
    moive_name : String!
    score : Float!
    description : String!
  }`;
export const userQueries = `
      getUsers: [user]!
      getMovies: [movie]!
      getSeries: [serie]!
      getMoviesScore: [score]!
      getSeriesScore: [score]!
  `;
export const UserMutations = `
    createUser(user: UserInput!): Response!
    createMovieScore(movieScore: MovieScore!): Response!
    createSerieScore(serieScore: SerieScore!): Response!
`;

export const authTypeDef = `

type AuthResponse {
  message: String!
}
type tokenResponse{
  id : Int!
  username : String!
  firstName : String!
  lastName : String!
  password : String!
  token : String!
  error: String!
}

input AuthCreateUser{
  username : String!
  firstName : String!
  lastName : String!
  password : String!
}

input AuthUser{
  username : String!
  password : String!
}



 `;
export const authQueries = `
     
  `;
export const authMutations = `
    createAuthUser(authCreateUser:AuthCreateUser!): AuthResponse
    verifyUser(authUser:AuthUser!): tokenResponse
`;