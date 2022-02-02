import { generalRequest, getRequest } from '../../utilities';
import { url, port, entryPoint } from './server';

const URLBase = `http://${url}:${port}`;
const URL2 = `http://${url}:${port}/users`;

const resolvers = {
    Query: {
        getUsers: (_) =>
            getRequest(`${URLBase}/users`, ''),
        getMoviesScore: (_) =>
            getRequest(`${URLBase}/movies_scores`, ''),
        getSeriesScore: (_) =>
            getRequest(`${URLBase}/series_scores`, ''),
        getMovies: (_) =>
            getRequest(`${URLBase}/movies`, ''),
        getSeries: (_) =>
            getRequest(`${URLBase}/series`, ''),
    },
    Mutation: {
        createUser: (_, { user }) =>
            generalRequest(`${URLBase}/${entryPoint}`, 'POST', user),
        createMovieScore: (_, { movieScore }) =>
            generalRequest(`${URLBase}/user/movie_score/create`, 'POST', movieScore),
        createSerieScore: (_, { serieScore }) =>
            generalRequest(`${URLBase}/user/series_score/create`, 'POST', serieScore),
        verifyUser: (_, { authUser }) =>
            generalRequest(`${URLBase}/users/veryUser`, 'POST', authUser),

    }
};

export default resolvers;