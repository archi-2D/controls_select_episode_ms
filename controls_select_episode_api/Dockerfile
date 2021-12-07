FROM node:carbon-slim

# Create app directory
WORKDIR /controls_select_episode_api

# Install app dependencies
COPY package.json /controls_select_episode_api/
RUN npm install

# Bundle app source
COPY . /controls_select_episode_api/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]
