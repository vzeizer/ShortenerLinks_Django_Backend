# URL Shortener - Backend

A modern URL shortener service built with Node.js that allows users to create short links, track analytics, and manage their URLs efficiently.

## 🚀 Features

- **URL Shortening**: Convert long URLs into short, manageable links
- **Custom Aliases**: Create custom short codes for your URLs
- **Analytics**: Track click counts and access statistics
- **User Management**: User registration and authentication
- **API-First**: RESTful API design for easy integration

## 🛠️ Tech Stack

- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: PostgreSQL/MongoDB
- **Authentication**: JWT
- **Validation**: Joi/Zod
- **Environment**: dotenv

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd backend-vagner/server
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the application:
```bash
# Development
npm run dev

# Production
npm start
```

## 🔧 Environment Variables

```env
PORT=3000
DATABASE_URL=your_database_connection_string
JWT_SECRET=your_jwt_secret
NODE_ENV=development
FRONTEND_URL=http://localhost:3000
```

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### URL Management
- `POST /api/urls` - Create short URL
- `GET /api/urls` - Get user's URLs
- `GET /api/urls/:id` - Get specific URL details
- `PUT /api/urls/:id` - Update URL
- `DELETE /api/urls/:id` - Delete URL
- `GET /:shortCode` - Redirect to original URL

### Analytics
- `GET /api/urls/:id/analytics` - Get URL analytics
- `GET /api/analytics/dashboard` - User dashboard data

## 💡 Usage Examples

### Create Short URL
```bash
curl -X POST http://localhost:3000/api/urls \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "originalUrl": "https://example.com/very/long/url",
    "customAlias": "mylink"
  }'
```

### Response
```json
{
  "success": true,
  "data": {
    "id": "123",
    "originalUrl": "https://example.com/very/long/url",
    "shortUrl": "http://localhost:3000/mylink",
    "shortCode": "mylink",
    "clickCount": 0,
    "createdAt": "2024-01-01T00:00:00.000Z"
  }
}
```

## 📁 Project Structure

```
server/
├── src/
│   ├── controllers/     # Route controllers
│   ├── models/         # Database models
│   ├── routes/         # API routes
│   ├── middleware/     # Custom middleware
│   ├── utils/          # Utility functions
│   └── config/         # Configuration files
├── tests/              # Test files
├── .env.example        # Environment template
└── server.js          # Entry point
```

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm run test:coverage
```

## 🚀 Deployment

### Using Docker
```bash
docker build -t url-shortener-backend .
docker run -p 3000:3000 url-shortener-backend
```

### Using PM2
```bash
npm install -g pm2
pm2 start ecosystem.config.js
```

## 📊 API Response Format

### Success Response
```json
{
  "success": true,
  "data": {
    // response data
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "message": "Error description",
    "code": "ERROR_CODE"
  }
}
```

## 🔒 Security Features

- JWT authentication
- Input validation and sanitization
- Rate limiting
- CORS configuration
- SQL injection prevention

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For support, email: [your-email@example.com]
