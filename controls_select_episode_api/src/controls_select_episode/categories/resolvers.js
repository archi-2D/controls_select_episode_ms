import { generalRequest, getRequest } from '../../utilities';
import { url, port, entryPoint } from './server';

const URL1 = `http://${url}:${port}/${entryPoint}`;
const URL2 = `http://${url}:${port}/users`;

const resolvers = {
    Query: {
        getUsers: (_) =>
            getRequest(URL2, ''),
    },
    Mutation: {
        createUser: (_, { user }) =>
            generalRequest(`${URL1}`, 'POST', user),
        //generalRequest('http://127.0.0.1/user/create_user', 'POST', user),
    }
};

export default resolvers;