# Use the official Node.js image as the base image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the project dependencies
RUN npm install

# Copy the entire project to the working directory
COPY . .

# Expose port 3000 (assuming your application is running on this port)
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
