# Use Node 20 as base
FROM node:20-slim

# Set working directory
WORKDIR /app

# Install yarn (already included in node images, but just in case)
# Copy package.json and yarn.lock
COPY frontend/package.json ./
# If yarn.lock exists, copy it. Otherwise skip.
# Note: In docker we should be careful with paths if we copy from root.
# Let's assume we copy from the frontend directory's context later in compose or here.
# For simplicity, we'll copy the whole frontend folder.

# Copy package.json first for better caching
COPY frontend/package.json ./
# Install dependencies
RUN yarn install

# Copy the rest of the frontend code
COPY frontend/ .

# Expose frontend port
EXPOSE 4200

# Start the application
CMD ["yarn", "start", "--host", "0.0.0.0"]
